import asyncio
import os
import time
import requests
import aiohttp
from VeGaMusic.plugins.play.filters import command
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VeGaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeGaMusic import app
from asyncio import gather
from pyrogram.errors import FloodWait

@app.on_message(filters.command(["المالك", "صاحب الخرابه", "المنشي"]) & filters.group)
async def vgdg(client: Client, message: Message):
    if len(message.command) >= 2:
        return 
    else:
        chat_id = message.chat.id
        f = "administrators"
        async for member in client.iter_chat_members(chat_id, filter=f):
            if member.status == "creator":
                id = member.user.id
                key = InlineKeyboardMarkup([[InlineKeyboardButton(member.user.first_name, url=f"tg://user?id={id}")]])
                m = await client.get_chat(id)
                if m.photo:
                    photo = await app.download_media(m.photo.big_file_id)
                    caption = f"🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{m.first_name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{m.username}\n🎃 ¦𝙸𝙳 :{m.id}\n💌 ¦𝙱𝙸𝙾 :{m.bio}\n✨ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n♻️ ¦𝙸𝙳.𝙲𝙷𝙰𝚃 :{message.chat.id}"
                    await message.reply_photo(photo, caption=caption, reply_markup=key)
                else:
                    await message.reply(f"• {member.user.mention}")      
   


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
