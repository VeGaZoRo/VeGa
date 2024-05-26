import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from VeGaMusic import LOGGER, app, userbot
from VeGaMusic.core.call import Zoro
from VeGaMusic.misc import sudo
from VeGaMusic.plugins import ALL_MODULES
from VeGaMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS
from VeGaMusic.plugins.play.azan import azkar


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("كود جلسة الحساب المساعد غير مدعوم ...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("VeGaMusic.plugins" + all_module)
    LOGGER("ميــوزك فيجا").info("تم تحميل الاضافات ...✓")
    await userbot.start()
    await Zoro.start()
    try:
        await Zoro.stream_call("https://telegra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("ميــوزك فيجا").info(
            "خطأ .. قم بفتح المكالمة في مجموعة السجل الخاصه بك\n\nجارِ ايقاف بوت الميوزك . . ."
        )
        exit()
    except:
        pass
    await Zoro.decorators()
    LOGGER("ميــوزك فيجا").info("MatrixThon")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ميــوزك فيجا").info("جارِ ايقاف بوت الميوزك . . .")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
