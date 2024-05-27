import asyncio
import requests
from VeGaMusic import app
from VeGaMusic.plugins.play.filters import command
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
from pyrogram.types import ChatPermissions, ChatPrivileges
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


muttof = []
@app.on_message(command(["قفل التقيد", "تعطيل التقيد", "تعطيل الحمايه"]), group=419)
async def muttlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in muttof:
        return await message.reply_text("تم معطل من قبل🔒")
      muttof.append(message.chat.id)
      return await message.reply_text("تم تعطيل التقيد بنجاح ✅🔒")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@app.on_message(command(["فتح التقيد", "تفعيل التقيد", "تفعيل الحمايه"]), group=424)
async def muttopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in muttof:
        return await message.reply_text("التقيد مفعل من قبل ✅")
      muttof.remove(message.chat.id)
      return await message.reply_text("تم فتح التقيد بنجاح ✅🔓")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")
        
        
@app.on_message(command(["الغاء تقيد","الغاء لتقيد"]), group=94) 
async def mute(client: Client, message: Message):
   global restricted_users
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6438745713:
    if message.chat.id in muttof:
      return   	   	
    await app.restrict_chat_member(
                       chat_id=message.chat.id,
                       user_id=message.reply_to_message.from_user.id,
                       permissions=unmute_permissions,
                   )
    await app.send_message(message.chat.id, f"✅ ¦ تـم الغاء الكتـم بـنجـاح\n {message.reply_to_message.from_user.mention} ")


restricted_users = []
@app.on_message(command(["تقيد"]), group=62)
async def mute(client: Client, message: Message):
    global restricted_users
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6438745713:
        if message.chat.id in muttof:
            return
        if message.reply_to_message.from_user.id == 6438745713:
            await app.send_message(message.chat.id, "عذرا لا يمكنك تقيد المطور")
        else:
            mute_permission = ChatPermissions(can_send_messages=False)
            await app.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                permissions=mute_permission,
            )
            restricted_user = message.reply_to_message.from_user
            restricted_users.append(restricted_user)
            await app.send_message(message.chat.id, f"✅ ¦ تـم الكتـم بـنجـاح\n {restricted_user.mention} ")

@app.on_message(command(["مسح المقيدين"]), group=40)
async def unmute(client: Client, message: Message):
    global restricted_users
    user_id = message.from_user.id
    count = len(restricted_users)
    for user in restricted_users:
        await client.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user,
            permissions=unmute_permissions,
        )
        restricted_users.remove(user)
    await message.reply_text(f"↢ تم مسح {count} من المقيديد")
    

@app.on_message(command(["المقيدين"]))
async def get_restr_users(client: Client, message: Message):
   global restricted_users
   count = len(restricted_users)
   user_ids = [str(user.id) for user in restricted_users]
   response = f"⌔ قائمة المقيدين وعددهم : {count}\n"
   response += "\n"
   response += "\n".join(user_ids)
   await message.reply_text(response)



gaaof = []
@app.on_message(command(["تعطيل الحظر", "تعطيل الطرد", "تعطيل الحمايه"]), group=504)
async def gaalock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in gaaof:
        return await message.reply_text("تم معطل من قبل🔒")
      gaaof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الطرد و الحظر بنجاح ✅🔒")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@app.on_message(command(["فتح الطرد", "تفعيل الطرد", "تفعيل الحظر", "تفعيل الحمايه"]), group=412)
async def gaaopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in gaaof:
        return await message.reply_text("الطرد و الحظر مفعل من قبل ✅")
      gaaof.remove(message.chat.id)
      return await message.reply_text("تم فتح الطرد و الحظر بنجاح ✅🔓")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")
        
banned_users = []
@app.on_message(command(["حظر", "طرد"]), group=39)
async def mute(client: Client, message: Message):
    global banned_users    
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and message.from_user.id != 6438745713:
        return
    if message.chat.id in gaaof:
        return
    if message.reply_to_message.from_user.id == 6438745713:
        await app.send_message(message.chat.id, "عذرا لا يمكنك طرد المطور")
    else:
        banned_user = message.reply_to_message.from_user
        banned_users.append(banned_user)
        await app.ban_chat_member(message.chat.id, banned_user.id)
        await app.send_message(message.chat.id, f"✅ ¦ تـم الحظر بـنجـاح\n {banned_user.mention} ")

@app.on_message(command(["مسح المحظورين"]), group=19)
async def unban_all(client: Client, message: Message):
    global banned_users
    count = len(banned_users)
    chat_id = message.chat.id
    failed_count = 0

    for member in banned_users.copy():
        user_id = member.id
        try:
            await client.unban_chat_member(chat_id, user_id)
            banned_users.remove(member)
        except Exception:
            failed_count += 1

    successful_count = count - failed_count

    if successful_count > 0:
        await message.reply_text(f"↢ تم مسح {successful_count} من المحظورين")
    else:
        await message.reply_text("↢ لا يوجد مستخدمين محظورين ليتم مسحهم")

    if failed_count > 0:
        await message.reply_text(f"↢ فشل في مسح {failed_count} من المحظورين")
        
        
@app.on_message(command(["الغاء حظر","/unban"]), group=42)
async def mute(client: Client, message: Message):
   global banned_users
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6438745713:
    await app.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id) 
    banned_users.remove(user)
    await app.send_message(message.chat.id, f"✅ ¦ تـم الغاء الحظر بـنجـاح\n {message.reply_to_message.from_user.mention} ")


@app.on_message(command(["المحظورين"]))
async def get_restricted_users(client: Client, message: Message):
   global banned_users
   count = len(banned_users)
   user_ids = [str(user.id) for user in banned_users]
   response = f"⌔ قائمة المحظورين وعددهم : {count}\n"
   response += "\n"
   response += "\n".join(user_ids)
   await message.reply_text(response)




muted_users = []
@app.on_message(command(["كتم"]), group=39)
async def mute_user(client, message):
    global muted_users    
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and message.from_user.id != 6438745713:
        return
    if message.reply_to_message.from_user.id == 6438745713:
        await app.send_message(message.chat.id, "عذرا لا يمكنك طرد المطور")
    else:	
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            if user_id not in muted_users:
                muted_users.append(user_id)
                await message.reply_text(f"العضو {user_id} تم كتمه بنجاح.")
            else:
                await message.reply_text(f"المستخدم محظور بالفعل")
        else:
            await message.reply_text("قم بعمل ريبلاي")

@app.on_message(command(["الغاء الكتم", "الغاء كتم"]), group=62)
async def unmute_user(client, message):
   global muted_users
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6438745713:	
    user_id = message.reply_to_message.from_user.id
    if user_id in muted_users:
        muted_users.remove(user_id)
        await message.reply_text(f"تم الغاء كتم المستخدم {user_id}")
        
       
        
        
       
@app.on_message(filters.text)
async def handle_message(client, message):
    if message.from_user and message.from_user.id in muted_users:
        await client.delete_messages(chat_id=message.chat.id, message_ids=message.id)

@app.on_message(command(["المكتومين"]), group=137)
async def get_rmuted_users(client, message):
    global muted_users
    count = len(muted_users)
    user_ids = [str(user) for user in muted_users]
    response = f"⌔ قائمة المكتومين وعددهم : {count}\n"
    response += "\n"
    response += "\n".join(user_ids)
    await message.reply_text(response)


@app.on_message(command(["مسح المكتومين"]), group=136)
async def unmute_all(client, message):
    global muted_users
    count = len(muted_users)
    chat_id = message.chat.id
    failed_count = 0

    for member in muted_users.copy():
        user_id = member
        try:
            muted_users.remove(member)
        except Exception:
            failed_count += 1

    successful_count = count - failed_count

    if successful_count > 0:
        await message.reply_text(f"↢ تم مسح {successful_count} من المكتومين")
    else:
        await message.reply_text("↢ لا يوجد مستخدمين مكتومين ليتم مسحهم")

    if failed_count > 0:
        await message.reply_text(f"↢ فشل في مسح {failed_count} من المكتومين")

   
@app.on_message(command(["اطردني"]), group=268)
async def fire_user(client, message):
    await message.reply_text("اطلع برا اصلا مش عايزينك")
    await client.ban_chat_member(message.chat.id, message.from_user.id)




@app.on_message(command(["البوتات"]) & filters.group, group=56555)
async def list_bots(client: Client, message: Message):
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return
    bot_usernames = []
    count = 0 
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.BOTS):
        if member.user.is_bot:
            bot_usernames.append("@" + member.user.username)
            count += 1

    if count > 0:
        bot_list = "\n".join(bot_usernames)
        await message.reply_text(f"عدد البوتات في المجموعة: {count} \n يوزرات البوتات: {bot_list}")
    else:
        await message.reply_text("لا يوجد بوتات في المجموعة.")
        





async def PROMOTE_OWNER(c:Client,m:Message):
    ChatID = m.chat.id
    TargetID = m.reply_to_message.from_user.id
    UserID = m.from_user.id
    KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("تغيير معلومات المجموعة",
    callback_data=f"can_change {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("حذف الرسائل",
    callback_data=f"can_delete {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("حظر المستخدمين",
    callback_data=f"can_restrict {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("دعوه المستخدمين عبر الرابط",
    callback_data=f"can_invite {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("تثبيت الرسائل",
    callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("إداره البثوث المباشره",
    callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("إضافه مشرفين جدد",
    callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("مسح الرساله",
	callback_data="delete"),
	InlineKeyboardButton("المزيد",
	callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]])
    
    await m.reply(f"ابشر عيني 「{m.from_user.mention}」\n لديك قائمه يمكنك التحكم فيها في رفع المستخدم مشرف\nاذا ضغط علي زر 1 ترفع فقط صلاحيه\n ضغطت علي زر 2 يرفع زر 1,2\nضغطت علي زر 3 يرفع زر 1,2,3 وهكذا\nلذللك ضفنالك زر المزيد تصفحه",reply_markup=KEYBOARD)


async def PROMOTE(c:Client,m:Message):
    ChatID = m.chat.id
    TargetID = m.reply_to_message.from_user.id
    UserID = m.from_user.id
    KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("تغيير معلومات المجموعة",
    callback_data=f"can_change {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("حذف الرسائل",
    callback_data=f"can_delete {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("حظر المستخدمين",
    callback_data=f"can_restrict {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("دعوه المستخدمين عبر الرابط",
    callback_data=f"can_invite {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("تثبيت الرسائل",
    callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("إداره البثوث المباشره",
    callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("مسح الرساله",
	callback_data="delete"),
	InlineKeyboardButton("المزيد",
	callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]])
    
    await m.reply(f"ابشر عيني 「{m.from_user.mention}」\n لديك قائمه يمكنك التحكم فيها في رفع المستخدم مشرف\nمع العلم اذا ضغط علي زر 1 ترفع فقط صلاحيه\n ضغطت علي زر 2 يرفع زر 1+ 2\nضغطت علي زر 3 يرفع زر 1 + 2 +  3 وهكذا",reply_markup=KEYBOARD)





@app.on_message(command(["رفع"]),group=1)
async def New(c:Client,m:Message):
	Ra = await m.chat.get_member(m.from_user.id)
	if Ra.status == ChatMemberStatus.OWNER:
		if m.reply_to_message and m.reply_to_message.from_user:
			if m.command[1] == "مشرف":
				await PROMOTE_OWNER(c,m)
				
				
	elif Ra.status == ChatMemberStatus.ADMINISTRATOR:
		if m.reply_to_message and m.reply_to_message.from_user:
			if m.command[1] == "مشرف":
				await PROMOTE(c,m)
			
	elif Ra.status == ChatMemberStatus.MEMBER:
		if m.reply_to_message and m.reply_to_message.from_user:
			if m.command[1] == "مشرف":
				await m.reply(f"عزيزي 「{m.from_user.mention}」\nانت مجرد عضو في هذه المجموعة")

@app.on_callback_query(~filters.regex('^delete$'),group=2)
async def MoreAndSet(c:Client,m:Message):
	ChatID = m.message.chat.id
	TargetID = m.message.reply_to_message.from_user.id
	UserID = m.from_user.id
	msg = m.data
	PromoteList = msg.split(" ")
	ChatID = m.message.chat.id
	TargetID = int(PromoteList[2])
	UserID = int(PromoteList[3])
	
	MORE_PROMOTE = InlineKeyboardMarkup([
    [InlineKeyboardButton("1,2,3,4,5,6,7",
    callback_data=f"Seven {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("1,2,4,5,6",
    callback_data=f"Five {ChatID} {TargetID} {UserID}"),
    InlineKeyboardButton("2,4,5,6",
    callback_data=f"Four {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("1,3,6",
    callback_data=f"Three {ChatID} {TargetID} {UserID}"),
    InlineKeyboardButton("4,6",
    callback_data=f"Two {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("4",
    callback_data=f"One {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("مسح الرساله",
    callback_data="delete")]])

	
	if m.data == f"MoreAndMore {ChatID} {TargetID} {UserID}":
		return await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n",
		reply_markup=MORE_PROMOTE)
		
	if m.data == "delete":
		await m.message.delete()
		
    
    



@app.on_callback_query(~filters.regex('^delete$'),group=3)
async def SetPromote(c:Client,m:Message):
	msg = m.data
	PromoteList = msg.split(" ")
	ChatID = m.message.chat.id
	TargetID = int(PromoteList[2])
	UserID = int(PromoteList[3])

	
	if m.from_user.id !=UserID:
		await c.answer_callback_query(
		m.id,
		text="هذا الأمر لايخصك",
		show_alert=True)
		
	elif len(PromoteList) == 4 and PromoteList[0] == "can_change":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه تغيير معلومات المجموعه",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("حذف الرسائل",
		callback_data=f"can_delete {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("حظر المستخدمين",
		callback_data=f"can_restrict {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("دعوه المستخدمين عبر الرابط",
		callback_data=f"can_invite {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("تثبيت الرسائل",
		callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إداره البثوث المباشره",
		callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
	elif len(PromoteList) == 4 and PromoteList[0] == "can_delete":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_change_info=True,
		can_delete_messages=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه مسح الرسائل",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("حظر المستخدمين",
		callback_data=f"can_delete {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("دعوه المستخدمين عبر الرابط",
		callback_data=f"can_invite {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("تثبيت الرسائل",
		callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إداره البثوث المباشره",
		callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
	
	elif len(PromoteList) == 4 and PromoteList[0] == "can_restrict":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه حظر المستخدمين",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("دعوه المستخدمين عبر الرابط",
		callback_data=f"can_invite {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("تثبيت الرسائل",
		callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إداره البثوث المباشره",
		callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "can_invite":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_invite_users=True,
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه دعوه المستخدمين",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("تثبيت الرسائل",
		callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إداره البثوث المباشره",
		callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "can_pin":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_pin_messages=True,
		can_invite_users=True,
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه تثبيت الرسائل",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("إداره البثوث المباشره",
		callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
	
	elif len(PromoteList) == 4 and PromoteList[0] == "can_manage":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_manage_video_chats=True,
		can_pin_messages=True,
		can_invite_users=True,
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه التحكم في المحادثه الصوتية",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "can_promote":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_promote_members=True,
		can_manage_video_chats=True,
		can_pin_messages=True,
		can_invite_users=True,
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه رفع مشرفين جدد",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
		
		
@app.on_callback_query(~filters.regex('^delete$'),group=4)
async def SetMorePromote(c:Client,m:Message):
	msg = m.data
	PromoteList = msg.split(" ")
	ChatID = m.message.chat.id
	TargetID = int(PromoteList[2])
	UserID = int(PromoteList[3])
	
	MORE_PROMOTE = InlineKeyboardMarkup([
    [InlineKeyboardButton("1,2,3,4,5,6,7",
    callback_data=f"Seven {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("1,2,4,5,6",
    callback_data=f"Five {ChatID} {TargetID} {UserID}"),
    InlineKeyboardButton("2,4,5,6",
    callback_data=f"Four {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("1,3,6",
    callback_data=f"Three {ChatID} {TargetID} {UserID}"),
    InlineKeyboardButton("4,6",
    callback_data=f"Two {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("4",
    callback_data=f"One {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("مسح الرساله",
    callback_data="delete")]])

    
	
	if m.from_user.id !=UserID:
		await c.answer_callback_query(
		m.id,
		text="هذا الأمر لايخصك",
		show_alert=True)
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "Seven":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_promote_members=True,
		can_manage_video_chats=True,
		can_pin_messages=True,
		can_invite_users=True,
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (1,2,3,4,5,6,7) ",reply_markup=MORE_PROMOTE)
			
	elif len(PromoteList) == 4 and PromoteList[0] == "Five":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_manage_video_chats=True,
		can_pin_messages=True,
		can_invite_users=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (1,2,4,5,6) ",reply_markup=MORE_PROMOTE)
		
	elif len(PromoteList) == 4 and PromoteList[0] == "Four":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_manage_video_chats=True,
		can_pin_messages=True,
		can_invite_users=True,
		can_delete_messages=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (2,4,5,6) ",reply_markup=MORE_PROMOTE)
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "Three":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_manage_video_chats=True,
		can_restrict_members=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (1,3,6) ",reply_markup=MORE_PROMOTE)
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "Two":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_manage_video_chats=True,
		can_invite_users=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (4,6) ",reply_markup=MORE_PROMOTE)
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "One":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_invite_users=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (4) ",reply_markup=MORE_PROMOTE)


@app.on_callback_query(filters.regex("^delete$"),group=5)
async def DelMessage(c:Client,m:Message):
	UserID = m.from_user.id
	if m.from_user.id !=UserID:
		await c.answer_callback_query(
		m.id,
		text="هذا الأمر لايخصك",
		show_alert=True)
	else:
		await m.message.delete()