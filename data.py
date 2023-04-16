from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🌐ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ🌐", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("🍁ᴅᴇᴠᴇʟᴏᴘᴇʀ🍁", url="https://t.me/SuppieNoodles"),
        InlineKeyboardButton("💉ꜱᴏᴜʀᴄᴇ💉", url="https://t.me/BotHub_xD/168"),
        InlineKeyboardButton("🐼ꜱᴜᴘᴘᴏʀᴛ🐼", url="https://t.me/TheNight_City"),
        ],
    ]

    START = """
ʜᴇʏᴀ! ᴄᴜᴛɪᴇ {},

ɪᴍ ꜱᴛʀɪɴɢ ᴀɪ {},
ɪᴍ ᴛʜᴇ ᴍᴏꜱᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɪ ʀᴏʙᴏᴛ ɪ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴꜱ ᴏɴʟʏ ꜰᴏʀ ʏᴏᴜ ʙᴀʙᴇ ! 🖤
ʙᴀꜱᴇᴅ ᴏɴ : ᴘʏʀᴏɢʀᴀᴍ
ᴡʀɪᴛᴇɴ ɪɴ : ᴘʏᴛʜᴏɴ

ᴏᴡɴᴇʀ : [ꜰɪɴᴇx_xᴅ !](https://t.me/SuppieNoodles) !
    """
