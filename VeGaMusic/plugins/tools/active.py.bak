from AFROTOMusic.plugins.play.filters import command
from pyrogram import filters
from pyrogram.types import Message
from unidecode import unidecode

from AFROTOMusic import app
from AFROTOMusic.misc import SUDOERS
from AFROTOMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


@app.on_message(command(["المكالمات الصوتيه", "/activevoice"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("» جـارِ جلب جميـع المكالمـات الصوتيـه في البـوت...")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"»لايوجد محادثات صوتيه جارية الان ع البوت {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» قائمة المحادثات الصوتية الجاريه الان في البوت :</b>\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(command(["المكالمات المرئيه", "/activevideo"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("» جـارِ جلب جميـع مكالمـات الفيديـو المرئيـه في البـوت...")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"»لايوجد محادثات مرئية جارية الان ع البوت {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» قائمة المحادثات المرئية الجاريه الان في البوت :</b>\n\n{text}",
            disable_web_page_preview=True,
        )
