from pyrogram import Client, filters, enums
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ButtonUrlInvalid
import asyncio.exceptions

from Database.maindb import mdb
db = mdb
from plugins.string_to_buttons import string_to_buttons
from vars import ADMIN_ID

@Client.on_message(filters.command("settings") & filters.private & filters.user(ADMIN_ID))
async def settings_handler(bot: Client, message: Message):
    if getattr(bot, "REQFSUB", False):
        reqfsub_button = InlineKeyboardButton("Disable Request ForceSub", callback_data="chng_req")
    else:
        reqfsub_button = InlineKeyboardButton("Enable Request ForceSub", callback_data="chng_req")

    buttons = [
        [InlineKeyboardButton("Manage Caption", callback_data="change_caption")],
        [InlineKeyboardButton("Manage Buttons", callback_data="change_buttons")],
        [reqfsub_button],
    ]

    await message.reply(
        "**⚙️ Global Settings**\n\n"
        "Here you can set a global caption and buttons for your bot.\n"
        "- Caption → Text that will be added to posts.\n"
        "- Buttons → Inline buttons that appear with posts.\n"
        "- ForceSub → Require users to join a channel before using the bot.",
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode=enums.ParseMode.MARKDOWN
    )

