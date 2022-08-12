# RiZoeLXSpam - Spam Userbots
# Copyright © 2021 @RiZoeLX

import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
import logging
import time
from main import API_ID, API_HASH, alivee, BOT_TOKEN, BOT_TOKEN2, BOT_TOKEN3, BOT_TOKEN4, BOT_TOKEN5, BOT_TOKEN6, BOT_TOKEN7, BOT_TOKEN8, BOT_TOKEN9, BOT_TOKEN10, sudo, owner, hndlr

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

rizoelversion = "v2.0.3"

# values

ALIVE_PIC = str(alive)
OWNER_ID = int(owner)
CMD_HNDLR = hndlr

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

SUDO_USERS = []
if sudo:
    SUDO_USERS = make_int(sudo)

#Tokens

Riz = TelegramClient('Riz', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

Riz2 = TelegramClient('Riz2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

Riz3 = TelegramClient('Riz3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

Riz4 = TelegramClient('Riz4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

Riz5 = TelegramClient('Riz5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

Riz6 = TelegramClient('Riz6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

Riz7 = TelegramClient('Riz7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

Riz8 = TelegramClient('Riz8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

Riz9 = TelegramClient('Riz9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

Riz10 = TelegramClient('Riz10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
  
SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append(1517994352)
SUDO_USERS.append(1789859817)
