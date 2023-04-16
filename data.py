from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🥶 𝙼𝙰𝙺𝙴  𝚂𝙴𝚂𝚂𝙸𝙾𝙽 🥶", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("🥵 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 🥵️", url="https://t.me/TheNight_City"),
         InlineKeyboardButton("👻 𝙼𝙰𝙳𝙴 𝙱𝚈 👻", url="https://t.me/SuppieNoodles"),
        InlineKeyboardButton("💟 𝙶𝙸𝚃𝙷𝚄𝙱 💟", url="https://github.com/Itzvenomo"),
        InlineKeyboardButton(" ❤ ️𝚄𝙿𝙳𝙰𝚃𝙴𝚂 ❤️", url="https://t.me/Bothub_xD"),
        ],
    ]

    START = """
𝙷ᴇʏ 𝙱𝙰𝙱𝚈 😘 {},

𝚃𝙷𝙸𝚂 𝙸𝚂 {},
𝙰ɴ 𝙾𝙿𝙴𝙽 𝚂𝙾𝚄𝚁𝙲𝙴 𝚂𝚃𝚁𝙸𝙽𝙶 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 𝙱𝙾𝚃, 𝚆𝚁𝙸𝚃𝚃𝙴𝙽 𝙸𝙽  𝙿𝚈𝚃𝙷𝙾𝙽 𝚆𝙸𝚃𝙷 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙾𝙵 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝙰𝙽𝙳 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽.

𝚄𝙿𝙳𝙰𝚃𝙴𝚂 : [⚡𝙲𝙷𝙰𝙽𝙽𝙴𝙻⚡](https://t.me/Bothub_xD)
𝙼𝙰𝙳𝙴 𝙱𝚈 : [✨𝙾𝚆𝙽𝙴𝚁✨](https://t.me/SuppieNoodles) !
    """
