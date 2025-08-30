from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ButtonUrlInvalid
import asyncio.exceptions

from Database.maindb import mdb
db = mdb
from plugins.string_to_buttons import string_to_buttons

@Client.on_message(filters.command("settings") & filters.private)
async def settings_handler(bot: Client, message: Message):
    buttons = [
        [InlineKeyboardButton("📝 Manage Caption", callback_data="change_caption")],
        [InlineKeyboardButton("🔘 Manage Buttons", callback_data="change_buttons")],
    ]
    await message.reply(
        "**⚙️ Global Settings**\n\n"
        "Here you can set a global caption and buttons for your bot.\n"
        "- Caption → Text that will be added to posts.\n"
        "- Buttons → Inline buttons that appear with posts.",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
