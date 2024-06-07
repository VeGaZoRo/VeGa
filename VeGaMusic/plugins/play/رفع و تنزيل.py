import asyncio
import re
from pyrogram import Client, filters
from datetime import datetime
from pyrogram import enums
from config import OWNER_ID
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from VeGaMusic import app
from VeGaMusic.plugins.play.filters import command
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatMembersFilter
import asyncio
import requests
from VeGaMusic import app
from VeGaMusic.core.call import Zoro
from VeGaMusic.utils.database import set_loop
from VeGaMusic.utils.decorators import AdminRightsCheck
from datetime import datetime
from config import BANNED_USERS, PING_IMG_URL, lyrical, START_IMG_URL, MONGO_DB_URI, OWNER_ID
from VeGaMusic.utils import bot_sys_stats
from VeGaMusic.utils.decorators.language import language
import random
import time
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from aiohttp import ClientSession
from traceback import format_exc
import config
import re
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
from pyrogram import Client, filters
from VeGaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
import sys
import os
from pyrogram.errors import PeerIdInvalid
from os import getenv
from VeGaMusic.misc import SUDOERS
from pyrogram import filters, Client
from telegraph import upload_file
from dotenv import load_dotenv
from VeGaMusic.utils.database import (set_cmode,get_assistant) 
from VeGaMusic.utils.decorators.admins import AdminActual
from VeGaMusic import app
unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False, 
    can_send_other_messages=False,
    can_send_polls=False,
    can_add_web_page_previews=False,
    can_change_info=False,
    can_pin_messages=False,
    can_invite_users=True,
)

welcome_enabled = True


def is_owner(_, __, message):

    return message.from_user.id == OWNER_ID



chat_locked = False
mention_locked = False
video_locked = False
link_locked = False
sticker_locked = False
smsim_locked = False
forward_locked = False
reply_locked = False
photo_locked = False
saap_locked = False
rdods_locked = False


@app.on_chat_member_updated()
async def welcome(client, chat_member_updated):
    if not welcome_enabled:
        return
    
    if chat_member_updated.new_chat_member.status == ChatMemberStatus.BANNED:
        kicked_by = chat_member_updated.new_chat_member.restricted_by
        user = chat_member_updated.new_chat_member.user
        
        if kicked_by is not None and kicked_by.is_self:
            messagee = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة بواسطة البوت"
        else:
            if kicked_by is not None:
                message = f"• المستخدم [{user.first_name}](tg://user?id={user.id}) \n• تم طرده من الدردشة بواسطة [{kicked_by.first_name}](tg://user?id={kicked_by.id})\n• ولقد طردته بسبب هذا"
                try:
                    await client.ban_chat_member(chat_member_updated.chat.id, kicked_by.id)
                except Exception as e:
                    message += f"\n\nعذرًا، لم استطع حظر الإداري بسبب: {str(e)}"
            else:
                message = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة"
            
            
        
        await client.send_message(chat_member_updated.chat.id, message)


mutorn = {}

def is_mutor(user_id):
    return user_id in mutorn and mutorn[user_id] > 0

@app.on_message(command(["رفع ادمن"]), group=3197)
async def mutornn(client, message):
    global mutorn
    user_id = message.reply_to_message.from_user.id
    if user_id in mutorn:
        mutorn[user_id] += 1
    else:
        mutorn[user_id] = 1
    chat_id = message.chat.id
    await app.send_message(chat_id, text="تم الرفع ادمن بنجاح")

@app.on_message(command(["تنزيل ادمن"]), group=396)
async def remove_mutor(client, message):
    global mutorn
    user_id = message.reply_to_message.from_user.id
    if user_id in mutorn and mutorn[user_id] > 0:
        mutorn[user_id] -= 1
        chat_id = message.chat.id
        await app.send_message(chat_id, text="تم الادمن بنجاح")
    else:
        chat_id = message.chat.id
        await app.send_message(chat_id, text="المستخدم ليس لديه صلاحيه")

@app.on_message(command(["قائمة الادمنية", "الادمنيه"]), group=3996)
async def list_mutors(client, message):
    global mutorn
    chat_id = message.chat.id
    mutors = [str(user_id) for user_id, rank in mutorn.items() if rank > 0]
    if mutors:
        mutors_list = "\n".join(mutors)
        await app.send_message(chat_id, text=f"قائمة الأدمنية:\n{mutors_list}")
    else:
        await app.send_message(chat_id, text="لا يوجد أدمنية حالياً")

@app.on_message(command(["مسح الادمنيه"]), group=13681)
async def mutorndv(client, message):
    global mutorn
    count = len(mutorn)
    chat_id = message.chat.id
    failed_count = 0
    for member in list(mutorn.keys()):
        user_id = member
        try:
            del mutorn[member]
        except Exception:
            failed_count += 1
    successful_count = count - failed_count
    if successful_count > 0:
        await message.reply_text(f"↢ تم مسح {successful_count} من الادمنيه")
    else:
        await message.reply_text("↢ لا يوجد ادمنيه ليتم مسحهم")
    if failed_count > 0:
        await message.reply_text(f"↢ فشل في مسح {failed_count} من الادمنيه")


mallekan = {}

def is_malleka(user_id):
    return user_id in mallekan and mallekan[user_id] > 0

@app.on_message(command(["رفع مالك"]), group=3191)
async def mallekann(client, message):
    global mallekan
    user_id = message.reply_to_message.from_user.id
    if user_id in mallekan:
        mallekan[user_id] += 1
    else:
        mallekan[user_id] = 1
    chat_id = message.chat.id
    await app.send_message(chat_id, text="تم الرفع مالك بنجاح")

@app.on_message(command(["تنزيل مالك"]), group=390)
async def remove_malleka(client, message):
    global mallekan
    user_id = message.reply_to_message.from_user.id
    if user_id in mallekan and mallekan[user_id] > 0:
        mallekan[user_id] -= 1
        chat_id = message.chat.id
        await app.send_message(chat_id, text="تم تنزيل مالك بنجاح")
    else:
        chat_id = message.chat.id
        await app.send_message(chat_id, text="المستخدم ليس لديه الصلاحيه")

@app.on_message(command(["قائمة المالكية", "المالكين"]), group=3991)
async def list_mallekas(client, message):
    global mallekan
    chat_id = message.chat.id
    mallekas = [str(user_id) for user_id, rank in mallekan.items() if rank > 0]
    if mallekas:
        mallekas_list = "\n".join(mallekas)
        await app.send_message(chat_id, text=f"قائمة المالكين:\n{mallekas_list}")
    else:
        await app.send_message(chat_id, text="لا يوجد أدمنية حالياً")

@app.on_message(command(["مسح المالكين"]), group=13684)
async def mallekandv(client, message):
    global mallekan
    count = len(mallekan)
    chat_id = message.chat.id
    failed_count = 0
    for member in list(mallekan.keys()):
        user_id = member
        try:
            del mallekan[member]
        except Exception:
            failed_count += 1
    successful_count = count - failed_count
    if successful_count > 0:
        await message.reply_text(f"↢ تم مسح {successful_count} من المالكين")
    else:
        await message.reply_text("↢ لا يوجد مالكيه ليتم مسحهم")
    if failed_count > 0:
        await message.reply_text(f"↢ فشل في مسح {failed_count} من المالكين")
        
        
        
@app.on_message(
    command(["رتبتي"])
    & filters.group
)
async def rotba(client, message):
    dev = (OWNER_ID)
    ze = (6753126490)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if int(message.from_user.id) == ze:
       rotba= "مّمٌَـبـ ـࢪمـج السوࢪس"
    elif message.from_user.id in dev:
        rotba = "مطور اساسي"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمــــن"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "المــــــألك"
    else:
         rotba = "عضــو جميل"
    await message.reply_text(f"رتبتك في هذه المجموعه \nهــي ← «{rotba}»")
