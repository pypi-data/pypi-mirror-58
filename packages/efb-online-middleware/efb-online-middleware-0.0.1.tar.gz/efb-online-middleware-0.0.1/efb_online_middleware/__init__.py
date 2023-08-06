# coding: utf-8
import io
import os
import re
import time
import sched
import string
import logging
import threading

from typing import Optional
from ruamel.yaml import YAML

from ehforwarderbot import EFBMiddleware, EFBMsg, EFBStatus, \
    EFBChat, coordinator, EFBChannel, utils

from efb_wechat_slave.vendor import wxpy

from .__version__ import __version__ as version

DALAY_HEART_BEAT = 1800     # half an hour
PING_STATUS = 'PING'
PONG_STATUS = 'PONG'

ping_status = ''
failure_time = 0
dalay_heart_beat = DALAY_HEART_BEAT
warn_status = False

echo_mp = ''
ping_text = 'PING'
pong_text = 'PONG'

class OnlineMiddleware(EFBMiddleware):
    """
    EFB Middleware - OnlineMiddleware
    """

    middleware_id = "online.OnlineMiddleware"
    middleware_name = "Online Middleware"
    __version__: str = version

    logger: logging.Logger = logging.getLogger("plugins.%s" % middleware_id)


    def __init__(self, instance_id=None):
        super().__init__()
        self.load_config()

        if hasattr(coordinator, "master") and isinstance(coordinator.master, EFBChannel):
            self.channel = coordinator.master
            self.bot = self.channel.bot_manager
            self.admin = self.channel.config['admins'][0]
            # self.bot.send_message(self.admin, 'msg')

        if hasattr(coordinator, "slaves") and coordinator.slaves['blueset.wechat']:
            self.channel_ews = coordinator.slaves['blueset.wechat']

            self.wxbot = self.channel_ews.bot

            try:
                schedule_heart_beat(self.wxbot, self.bot, self.admin)

            except Exception as e:
                self.logger.log(99, 'failed to schedule: {}'.format(e))

    def load_config(self):
        """
        Load configuration from path specified by the framework.

        Configuration file is in YAML format.
        """
        global echo_mp, ping_text, pong_text, DALAY_HEART_BEAT

        config_path = utils.get_config_path(self.middleware_id)
        if not config_path.exists():
            return

        with config_path.open() as f:
            data = YAML().load(f)

            # Verify configuration
            echo_mp = data.get("echo_mp")
            if not echo_mp:
                raise ValueError("echo mp is needed.")

            DALAY_HEART_BEAT = data.get("interval", DALAY_HEART_BEAT)
            ping_text = data.get("ping", ping_text)
            pong_text = data.get("pong", pong_text)

    def sent_by_master(self, message: EFBMsg) -> bool:
        author = message.author
        return author and author.module_id and author.module_id == 'blueset.telegram'

    def process_message(self, message: EFBMsg) -> Optional[EFBMsg]:
        """
        Process a message with middleware
        Args:
            message (:obj:`.EFBMsg`): Message object to process
        Returns:
            Optional[:obj:`.EFBMsg`]: Processed message or None if discarded.
        """
        global ping_status, failure_time, dalay_heart_beat, warn_status

        if self.sent_by_master(message):
            return message

        author = message.author
        if author:
            # self.logger.log( 99, "message.author: %s", message.author.__dict__)
            if author.chat_name == echo_mp and message.text == pong_text and ping_status == PING_STATUS:
                ping_status = PONG_STATUS
                failure_time = 0
                dalay_heart_beat = DALAY_HEART_BEAT
                warn_status = False
                return None

        return message


def schedule_heart_beat(wxbot, bot, admin):

    schedule = sched.scheduler(time.time, time.sleep)
    schedule.enter(dalay_heart_beat, 0, heart_beat, kwargs={
        'wxbot': wxbot,
        'bot': bot,
        'admin': admin,
    })

    threading.Thread(target=schedule.run).start()


def heart_beat(wxbot, bot, admin):
    global ping_status, failure_time, dalay_heart_beat, warn_status

    if ping_status == PING_STATUS:
        failure_time += 1

        if not warn_status:
            dalay_heart_beat = 10

    if failure_time > 2 and not warn_status:
        bot.send_message(admin, '微信可能已掉线，请检查')
        warn_status = True
        dalay_heart_beat = DALAY_HEART_BEAT

    schedule_heart_beat(wxbot, bot, admin)

    try:
        echo_chat = wxpy.utils.ensure_one(wxbot.mps().search(echo_mp))
        echo_chat.send(ping_text)
        ping_status = PING_STATUS

    except Exception:
        pass
