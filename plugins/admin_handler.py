from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup
from pyrogram.errors import ButtonUrlInvalid
from Database.maindb import mdb
from vars import ADMIN_ID
from plugins.string_to_buttons import string_to_buttons

@Client.on_message(filters.private & filters.user(ADMIN_ID))
async def admin_message_handler(bot: Client, message: Message):
    admin_state = await mdb.get_admin_state(message.from_user.id)

    if admin_state == "add_caption":
        if message.text.lower() == '/cancel':
            await mdb.set_admin_state(message.from_user.id, None)
            await message.reply('Cancelled', quote=True)
            return

        await mdb.set_caption(message.text.markdown)
        await mdb.set_admin_state(message.from_user.id, None)
        await message.reply('Caption set successfully ✅', quote=True)

    elif admin_state == "add_buttons":
        if message.text.lower() == '/cancel':
            await mdb.set_admin_state(message.from_user.id, None)
            await message.reply('Cancelled', quote=True)
            return
        
        if "-" not in message.text:
            await message.reply('Wrong format! Try again.', quote=True)
            return

        try:
            given_buttons = await string_to_buttons(message.text)
            await message.reply('Preview:', reply_markup=InlineKeyboardMarkup(given_buttons))
            await mdb.set_buttons(message.text)
            await mdb.set_admin_state(message.from_user.id, None)
            await message.reply('Buttons set successfully ✅', quote=True)
        except ButtonUrlInvalid:
            await message.reply('Invalid URL format! Try again.', quote=True)
        except Exception as e:
            await message.reply(f"An error occurred: {e}", quote=True)
