import asyncio
from pyrogram import Client, filters
from VeGaMusic.plugins.play.filters import command
from pyrogram.types import *
from VeGaMusic import app

@app.on_message(filters.video_chat_started)
async def brah(client, message):
       await message.reply("↯︙تم تشغيل ↫ ⦗ المحادثة المرئية ⦘")
@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
       await message.reply("↯︙تم ايقاف ↫ ⦗ المحادثة المرئية ⦘")
@app.on_message(filters.video_chat_members_invited)
async def fuckoff(client, message):
           text = f"↯︙قام الشخص ↫ ⦗ {message.from_user.mention} ⦘"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"\n↯︙بدعوة شخص الى المحادثة المرئية ↫ ⦗ {user.first_name} ⦘"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}")
           except:
             pass  
