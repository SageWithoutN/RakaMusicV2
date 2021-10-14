from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import BOT_NAME, BOT_USERNAME, GROUP_SUPPORT, OWNER_NAME, UPDATES_CHANNEL
from helpers.decorators import sudo_users_only
from helpers.filters import command

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)



@Client.on_message(
    command(["raka", f"raka@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>⚠️ Tolong banget ya {message.from_user.mention()}</b>
**jangan manggil-manggil raka,raka emang ganteng mending langsung pc aja""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="🌹 klick disini untuk chat raka 🌹", url="https://t.me/rakaaanjayy")]]
        ),
    )


@Client.on_message(
    command(["raka", f"raka@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>⚠️ Tolong banget ya {message.from_user.mention()}</b>
**jangan manggil-manggil raka,raka emang ganteng mending langsung pc aja"""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="🌹 klick disini untuk chat raka 🌹", url="https://t.me/rakaaanjayy")],
            ]
        ),
    )

