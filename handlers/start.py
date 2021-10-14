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


@Client.on_message(filters.command(["raka", f"raka@{BOT_USERNAME}"]))
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cfd64e1033266c559e9ef.jpg",
        caption=f"""🔵 Hallo Ini Adalah pembuat saya yang tamvan
🔵 tolong chat dia ya
🔵 Mau akunnya? nih [klick disini](https://t.me/rakaaanjayy)
🔵 Powered By : [Do'a Ibu](https://xxnx.com)
🔵 waktu hidup raka tinggal : {uptime}
Thanks For Using Me ♡""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🚨 Group", url=f"https://t.me/MusicRakaSupport"
                    ),
                    InlineKeyboardButton(
                        "📡 Channel", url=f"https://t.me/aboutraks"
                    )
                ]
            ]
        )
    )
