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

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

print("\n Starting RiZoeL X Spam ....")
clr()
print(" • RiZoeL X Spam • ")
print("\n\n Enter Valid Details and Continue")

API_ID = int(input("\n Enter api id: "))
API_HASH = str(input("\n Enter Api Hash: "))
ALIVE_PIC = str(input("\n Enter Telegraph Link For alive pic else press enter: ")) 
CMD_HNDLR = input("\n Cmd Handler: ")

print("\n Note: You Have to fill all bot tokens -!\n")
BOT_TOKEN = str(input("Enter Bot Token 1: "))
BOT_TOKEN2 = str(input("Enter Bot Token 2: "))
BOT_TOKEN3 = str(input("Enter Bot Token 3: "))
BOT_TOKEN4 = str(input("Enter Bot Token 4: "))
BOT_TOKEN5 = str(input("Enter Bot Token 5: "))
BOT_TOKEN6 = str(input("Enter Bot Token 6: "))
BOT_TOKEN7 = str(input("Enter Bot Token 7: "))
BOT_TOKEN8 = str(input("Enter Bot Token 8: "))
BOT_TOKEN9 = str(input("Enter Bot Token 9: "))
BOT_TOKEN10 = str(input("Enter Bot Token 10: "))
OWNER_ID = int(input("single Owner id: "))
sudo = str(input("Sudo Users id Space by Space or Press enter: "))


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
