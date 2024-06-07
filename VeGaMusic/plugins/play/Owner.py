import asyncio
import os
import time
import requests
import aiohttp
from VeGaMusic.plugins.play.filters import command
from pyrogram import filters
from pyrogram import Client
from pyrogram import enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VeGaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeGaMusic import app
from asyncio import gather
from pyrogram.errors import FloodWait
from pyrogram.enums import ChatMemberStatus


@app.on_message(command(["المالك", "صاحب الخرابه", "المنشي"]), group=222)
async def ownner(client: Client, message: Message):
    x = []
    async for m in client.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
         if m.status == ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
       m = await client.get_users(int(x[0]))
       if m.photo:
         async for photo in app.get_chat_photos(x[0],limit=1):
          await message.reply_photo(photo.file_id,caption=f"**⤄الاسم: {message.from_user.mention}\n⤄اليوزر: @{message.from_user.username}\n⤄ايدي:`{message.from_user.id}`\nʙɪᴏᚐ: {usr.bio}\n⤄جروب: {message.chat.title}\n⤄ايدي الجروب : `{message.chat.id}`**",reply_markup=InlineKeyboardMarkup(
             [              
               [          
                 InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")
               ],             
             ]                 
            )                     
          )
       else:
        await message.reply_text(f"**⤄الاسم: {message.from_user.mention}\n⤄اليوزر: @{message.from_user.username}\n⤄ايدي:`{message.from_user.id}`\nʙɪᴏᚐ: {usr.bio}\n⤄جروب: {message.chat.title}\n⤄ايدي الجروب : `{message.chat.id}`**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")],]))
    else:
        await message.reply_text("الاك محذوف يقلب")



@app.on_message(command("فحص"))
async def get_group_status(_, message: Message):
    if len(message.command) != 2:
        await message.reply("Please provide a group username. Example: `/groupinfo YourGroupUsername`")
        return
    
    group_username = message.command[1]
    
    try:
        group = await app.get_chat(group_username)
    except Exception as e:
        await message.reply(f"Error: {e}")
        return
    
    total_members = await app.get_chat_members_count(group.id)
    group_description = group.description
    premium_acc = banned = deleted_acc = bot = 0  # You should replace these variables with actual counts.

    response_text = (
        f"➖➖➖➖➖➖➖\n"
        f"➲ GROUP NAME : {group.title} ✅\n"
        f"➲ GROUP ID : {group.id}\n"
        f"➲ TOTAL MEMBERS : {total_members}\n"
        f"➲ DESCRIPTION : {group_description or  N/A }\n"
        f"➲ USERNAME : @{group_username}\n"
       
        f"➖➖➖➖➖➖➖"
    )
    
    await message.reply(response_text)


   
@app.on_message(command(["اسمي", "اسمي اي"]) & filters.group )
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""❤️‍🔥 اسمك »»  {message.from_user.mention()}""")
