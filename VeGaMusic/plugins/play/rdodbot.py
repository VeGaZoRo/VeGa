import asyncio
import random
from VeGaMusic import app
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, Message)
from pyrogram import filters, Client
from VeGaMusic.plugins.play.filters import command




txt = [


"ها عايز اي 🙄",
"ايوااا جااااي 😂",
"عاوزني اشقطلك مين يروحي 🥺",
"ايوة قول عاوز اي 🤔",
"قلب البوت 🥺",
"يعم تعبتنا معاك 🙁",
"استنا يعم بشقط وجايبك علطول 😂",

        ]


        


@app.on_message(command(["بوت","يا بوت"]))

async def khyrok(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}")
