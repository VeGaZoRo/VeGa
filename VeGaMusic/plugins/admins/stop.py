from pyrogram import filters
from pyrogram.types import Message

from VeGaMusic import app
from VeGaMusic.core.call import Zoro
from VeGaMusic.utils.database import set_loop
from VeGaMusic.utils.decorators import AdminRightsCheck
from VeGaMusic.utils.inline import close_markup
from config import BANNED_USERS

#comand
@app.on_message(
    command(["/stop", "اسكت", "انهاء", "ايقاف"]) & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Zoro.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    user_mention = message.from_user.mention if message.from_user else "المشـرف"
    await message.reply_text(
        _["admin_5"].format(user_mention), reply_markup=close_markup(_)
    )