import os
from typing import List

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "")
DATABASE_CHANNEL_ID = int(os.getenv("DATABASE_CHANNEL_ID", ""))
ADMIN_ID = int(os.getenv("ADMIN_ID", "7961157703"))
LOG_CHNL = int(os.getenv("LOG_CHNL", ""))
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "") # Without @
IS_FSUB = bool(os.environ.get("FSUB", True))
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "").split()))
DATABASE_CHANNEL_LOG = int(os.getenv("DATABASE_CHANNEL_ID", ""))
FREE_VIDEO_DURATION = int(os.getenv("FREE_VIDEO_DURATION", "99999"))


FORCE_MSG = """<b><blockquote>⚠️ Hᴇʏ, {mention} ×</blockquote>
Yᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴀʟʟ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ. Pʟᴇᴀsᴇ ʙᴇ sᴜʀᴇ ᴛᴏ ᴊᴏɪɴ ᴀʟʟ ᴛʜᴇ ᴄʜᴀɴɴᴇʟs ᴘʀᴏᴠɪᴅᴇᴅ ʙᴇʟᴏᴡ, ᴛʜᴇɴ ᴛʀʏ ᴀɢᴀɪɴ.. !</b>"""

PREMIUM_MSG = """
<b>Premium Plans</b>

Rear videos

Contact @owner to upgrade!
"""