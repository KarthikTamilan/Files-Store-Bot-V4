# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "0")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
**This is Permanent Files Store Bot V4!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.**

🤖 **My Name :** **[HMTD Files Store Bot V4](https://t.me/{BOT_USERNAME})**

📝 **Language :** **[Python3](https://www.python.org)**

📚 **Library :** **[Pyrogram](https://docs.pyrogram.org)**

📡 **Hosted on :** **[Heroku](https://heroku.com)**

🧑🏻‍💻 **Bot Owner :** **@HMTD_Channels_Owner**

🧑🏻‍ **Feedback :** **@HMTD_Feedback_Bot**

👥 **Discussion Group :** **[HMTD Discussion Group](https://t.me/HMTD_Discussion_Group)**

📢 **Updates Channel :** **[HMTD Links](https://t.me/HMTD_Links)**
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer :** **@HMTD_Channels_Owner**

**Developer is Best Movie Uploader. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://www.paypal.me/KarthiK717) (PayPal)**
"""
	HOME_TEXT = """
**Hi👋, [{}](tg://user?id={})\n\nThis is Permanent HMTD Files Store Bot V4.

I'm an HMTD Official Files Store Bot V4 Maintained by @HMTD_Links.Send me any File I will Give you a Permanent Sharable Link. Keep me Join to Our Official Channel to Receive Bot & Movies Updates in @HMTD_Links. I have Support Channel Also! Check "About Bot" Button.**
"""
