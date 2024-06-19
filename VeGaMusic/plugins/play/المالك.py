import asyncio
import os
import time
import requests
from pyrogram import enums
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VeGaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeGaMusic import app
from VeGaMusic.plugins.play.filters import command
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait










#المالك ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(command(["المالك", "صاحب الخرابه", "المنشي"]), group=95)
async def ownner(client: Client, message: Message):
    x = []
    async for m in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
         if m.status == ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
       m = await app.get_users(int(x[0]))
       if m.photo:
         async for photo in app.get_chat_photos(x[0],limit=1):
          await message.reply_photo(photo.file_id,caption=f"<b>╭✪ᚐɴᴧᴍᴇ : {m.first_name}\n│᚜✦ᴜsᴇꝛ : @{m.username}\n╰✪ᚐɪᴅ : <code>{m.id}</code>\n╭✪ᚐᴄʜᴧᴛ : {message.chat.title}\n╰✪ᚐɪᴅ.ᴄʜᴧᴛ : <code>{message.chat.id}</code></b>",reply_markup=InlineKeyboardMarkup(
             [              
               [          
                 InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")
               ],             
             ]                 
            )                     
          )
       else:
        await message.reply_text(f"b>╭✪ᚐɴᴧᴍᴇ : {m.first_name}\n│᚜✦ᴜsᴇꝛ : @{m.username}\n╰✪ᚐɪᴅ : <code>{m.id}</code>\n╭✪ᚐᴄʜᴧᴛ : {message.chat.title}\n╰✪ᚐɪᴅ.ᴄʜᴧᴛ : <code>{message.chat.id}</code></b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")],]))
    else:
        await message.reply_text("عزيزي المالك هذا حساب محذوف\n༄")

iddof = []
@app.on_message(command(["قفل الايدي", "تعطيل الايدي"]), group=2272)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in iddof:
        return await message.reply_text("تم معطل من قبل🔒")
      iddof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الايدي بنجاح ✅🔒")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@app.on_message(command(["فتح الايدي", "تفعيل الايدي"]), group=2292)
async def iddopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in iddof:
        return await message.reply_text("الايدي مفعل من قبل ✅")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم فتح الايدي بنجاح ✅🔓")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")




@app.on_message(command(["ايدي","الايدي","ا"]), group=27722)
async def iddd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"""**⤄الاسم: {message.from_user.mention}\n⤄اليوزر: @{message.from_user.username}\n⤄ايدي:`{message.from_user.id}`\nʙɪᴏᚐ: {usr.bio}\n⤄جروب: {message.chat.title}\n⤄ايدي الجروب : `{message.chat.id}`**""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )    



iddof = []
@app.on_message(command(["قفل جمالي", "تعطيل جمالي"]), group=22332)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in iddof:
        return await message.reply_text("جمالي معطل من قبل✅")
      iddof.append(message.chat.id)
      return await message.reply_text(" تم تعطيل جمالي بنجاح✅🔒")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@app.on_message(command(["قفل جمالي", "تعطيل جمالي"]), group=222009)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in iddof:
        return await message.reply_text("جمالي مفعل من قبل✅")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم فتح جمالي بنجاح ✅🔓")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")




@app.on_message(command(["جمالي","جمالو","ج"]), group=22452)
async def iddyyyd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0","10", "15","20", "25","30","35", "40","45", "50","55", "60"," 66", "70","77", "80","85", "90","99", "100","1000" ]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"نسبه جمالك يا مز انت \n│ \n└ʙʏ: {ik} %😂🥀❄️", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
       


@app.on_message(command(["اسمي"]), group=123222)
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""🥀❄️ اسمك »»  `{message.from_user.mention}`""") 





@app.on_message(command(["زو","زورو"]), group=666)
async def kas(client, message):
    usr = await client.get_chat("ToxVeGa")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"ɴᴀᴍᴇᚐ: {name}\nᴜsᴇʀᚐ: @{usr.username}\nɪᴅᚐ: `{usr.id}`\nʙɪᴏᚐ: {usr.bio}", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
                             )



@app.on_message(command(["زيرو","زي"]), group=666)
async def kas(client, message):
    usr = await client.get_chat("TopVeGa")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"ɴᴀᴍᴇᚐ: {name}\nᴜsᴇʀᚐ: @{usr.username}\nɪᴅᚐ: `{usr.id}`\nʙɪᴏᚐ: {usr.bio}", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
