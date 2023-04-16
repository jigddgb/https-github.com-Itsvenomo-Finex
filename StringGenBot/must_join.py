from env import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "TheNight_City" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(photo="https://te.legra.ph/file/18a02c44abd00e20643b2.jpg", caption=f"💟 𝙸𝙵 𝚈𝙾𝚄 𝙽𝙾𝚃 𝙹𝙾𝙸𝙽  [❤ 𝙽𝙸𝙶𝙷𝚃 𝙲𝙸𝚃𝚈 ❤]({link}) 𝚃𝙷𝙴𝙽 𝙸 𝚆𝙸𝙻𝙻 𝙽𝙾𝚃 𝚆𝙾𝚁𝙺, 𝙵𝙸𝚁𝚂𝚃 𝚈𝙾𝚄 𝙽𝙴𝙴𝙳 𝚃𝙾 𝙹𝙾𝙸𝙽 [👀 𝙽𝙸𝙶𝙷𝚃 𝙲𝙸𝚃𝚈 👀]({link}) 𝙰𝙽𝙳 𝚂𝚃𝙰𝚁𝚃 𝙼𝙴 𝙰𝙶𝙰𝙸𝙽 💟",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("💘 𝙽𝙸𝙶𝙷𝚃 𝙲𝙸𝚃𝚈 💘", url=f"{link}")]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"😏 𝙿𝚁𝙾𝙼𝙾𝚃𝙴 𝙼𝙴 𝙰𝚂 𝙰𝙽 𝙰𝙳𝙼𝙸𝙽 𝙸𝙽 𝚃𝙷𝙴 MUST_JOIN 𝙲𝙷𝙰𝚃 : {MUST_JOIN} !")
