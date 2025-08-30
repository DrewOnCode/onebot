from pyrogram.types import InlineKeyboardButton

async def string_to_buttons(string):
    parts = [p.strip() for p in string.replace("\n", "|").split("|") if p.strip()]
    buttons = []
    row = []
    for part in parts:
        if '-' not in part:
            continue
        text, url = part.split('-', 1)
        row.append(InlineKeyboardButton(text.strip(), url=url.strip()))
        if len(row) == 2:  # make 2 buttons per row
            buttons.append(row)
            row = []
    if row:  # leftover single button
        buttons.append(row)
    return buttons
