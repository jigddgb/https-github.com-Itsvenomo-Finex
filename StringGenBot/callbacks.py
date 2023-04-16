import traceback
from data import Data
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
from StringGenBot.generate import generate_session, ask_ques, buttons_ques


# Callbacks
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user.mention
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.START.format(callback_query.from_user.mention, mention),
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
    elif query == "generate":
        await callback_query.answer()
        await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await callback_query.answer("👻 𝚃𝙷𝙴 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝚅2 𝚂𝚃𝚁𝙸𝙽𝙶 𝚂𝙴𝚂𝚂𝙸𝙾𝙽   𝚆𝙸𝙻𝙻 𝙾𝙽𝙻𝚈 𝚆𝙾𝚁𝙺 𝙸𝙽 𝚃𝙷𝙴 𝙱𝙾𝚃'𝚂 𝚆𝙷𝙸𝙲𝙷 𝙰𝚁𝙴 𝚄𝙿𝙶𝚁𝙰𝙳𝙴𝙳 𝙰𝚃 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝚅2 👻", show_alert=True)
                await generate_session(bot, callback_query.message)
            elif query == "pyrogram1":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, old_pyro=True)
            elif query == "pyrogram_bot":
                await callback_query.answer("📌 𝚃𝙷𝙴 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 𝙲𝚁𝙴𝙰𝚃𝙸𝙽𝙶 𝚆𝙸𝙻𝙻 𝙱𝙴 𝙾𝙵 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝚅2 📌", show_alert=True)
                await generate_session(bot, callback_query.message, is_bot=True)
            elif query == "telethon_bot":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
            elif query == "telethon":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))


ERROR_MESSAGE = "𝚆𝚃𝙵 𝙶𝙰𝚈 😤 ! 𝚂𝙾𝙼𝙴𝚃𝙷𝙸𝙽𝙶 𝚆𝙴𝙽𝚃 𝚆𝚁𝙾𝙽𝙶. \n\n**𝙴𝚁𝚁𝙾𝚁** : {} " \
            "\n\n** 👀𝙿𝙻𝙴𝙰𝚂𝙴 𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝚃𝙷𝙸𝚂 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 @TheNight_City **, 𝙸𝙵 𝚃𝙷𝙸𝚂 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 🔥" \
            "𝙳𝙾𝙴𝚂𝙽'𝚃 𝙲𝙾𝙽𝚃𝙰𝙸𝙽𝚂 𝙰𝙽𝚈 𝚂𝙴𝙽𝚂𝙸𝚃𝙸𝚅𝙴 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 " \
            "𝙱𝙴𝙲𝙰𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙴𝚁𝚁𝙾𝚁 𝙸𝚂 **𝙽𝙾𝚃 𝙻𝙾𝙶𝙶𝙴𝙳 𝙱𝚈 𝚃𝙷𝙴 𝙱𝙾𝚃** !"
