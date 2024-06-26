from pyrogram.types import InlineKeyboardButton

import config
from VeGaMusic import app

#──██████──────██████───█████████████──────██████████████───████████████████─────────
#──██──██──────██──██───██─────────██────██────────────██───██────────────██─────────
#──██──██──────██──██───██──█████████───██───████████████───██───███████──██─────────
#──██──██──────██──██───██──██──────────██──██──────────────██───██───██──██─────────
#──██──██──────██──██───██──█▉──────────██──██──────────────██───██───██──██─────────
#──██──██──────██──██───██──██──────────██──██──────────────██───██───██──██─────────
#──██──██──────██──█▉───██──██──────────██──██──────────────██───██───██──██─────────
#──██──██──────██──██───██──█████████───██──█▉───███████────██───███████──██─────────
#──██───██────██───██───██─────────██───██──██───██────██───██────────────██─────────
#───██───██──██───██────██──█████████───██──██───████──██───██───███████──██─────────
#────██───████───██─────██──██──────────██──██─────██──██───██───██───██──██─────────
#─────██───██───██──────██──██──────────██───██────██──██───██───██───██──██─────────
#──────██──────██───────██──██───────────██───██───██──██───██───██───██──██─────────
#───────██────██────────██──█████████─────██──███████──██───██───██───██──██─────────
#────────██──██─────────██─────────█▉──────██──────────██───██───██───██──██─────────
#─────────████──────────█████████████───────████████████────███████───██████─────────


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="المطور", user_id=config.OWNER_ID),
          
        ],
         [InlineKeyboardButton(text=_["S_B_4"], callback_data="zzzback")],
        [
            InlineKeyboardButton(text="CHANNEL", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="GROUP", url=f"https://t.me/GROUPVEGA"),
        ],
        [
         
            InlineKeyboardButton(
                text="⭓ADD✘ME ♪",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="المطور", user_id=config.OWNER_ID),
            
        ],
         [InlineKeyboardButton(text=_["S_B_4"], callback_data="zzzback")],
        [
            InlineKeyboardButton(text="CHANNEL", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="GROUP", url=f"https://t.me/GROUPVEGA"),
        ],
        [
         
            InlineKeyboardButton(
                text="⭓ADD✘ME ♪",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
    ]
    return buttons
