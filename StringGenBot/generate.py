from data import Data
from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram1 import Client as Client1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram1.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)


ask_ques = "**💘 𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙴𝙻𝙴𝙲𝚃 𝚃𝙷𝙴 𝙿𝚈𝚃𝙷𝙾𝙽 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 𝙵𝙾𝚁 𝚆𝙷𝙸𝙲𝙷 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙲𝚁𝙴𝙰𝚃𝙴 𝚂𝚃𝚁𝙸𝙽𝙶 💘**"
buttons_ques = [
    [
        InlineKeyboardButton("🔥 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼🔥", callback_data="pyrogram1"),
        InlineKeyboardButton("🔥 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝚅2 🔥", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("🥶 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 🥶", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("🤖 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝙱𝙾𝚃 🤖", callback_data="pyrogram_bot"),
        InlineKeyboardButton("👻 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝙱𝙾𝚃 👻", callback_data="telethon_bot"),
    ],
]


@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "🥵 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 🥵"
    else:
        ty = "💘 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 💘"
        if not old_pyro:
            ty += "😘 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝚅2 😘"
    if is_bot:
        ty += "🤖 𝙱𝙾𝚃 🤖"
    await msg.reply(f"💕𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚂𝚃𝙰𝚁𝚃 **{ty}** 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 𝙲𝚁𝙴𝙰𝚃𝙸𝙽𝙶 💕")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "❤ 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 𝙲𝚁𝙴𝙰𝚃𝙸𝙽𝙶 𝙿𝚁𝙾𝙲𝙴𝚂𝚂...\n\n𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙴𝙽𝙳 𝚈𝙾𝚄𝚁 **𝙰𝙿𝙸_𝙸𝙳** 𝚃𝙾 𝙲𝙾𝙽𝚃𝙸𝙽𝚄𝙴 ❤", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply("**𝙰𝙿𝙸_𝙸𝙳** 𝙼𝚄𝚂𝚃 𝙱𝙴 𝙰𝙽 𝙸𝙽𝚃𝙴𝙶𝙴𝚁, 𝚂𝚃𝙰𝚁𝚃 𝙲𝚁𝙴𝙰𝚃𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 𝙰𝙶𝙰𝙸𝙽 😤", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, "👀 𝙽𝙾𝚆 𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙴𝙽𝙳 𝚈𝙾𝚄𝚁 **𝙰𝙿𝙸_𝙷𝙰𝚂𝙷** 𝚃𝙾 𝙲𝙾𝙽𝚃𝙸𝙽𝚄𝙴 👀", filters=filters.text)
    if await cancelled(api_hash_msg):
        return
    api_hash = api_hash_msg.text
    if not is_bot:
        t = "📌 𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙴𝙽𝙳 𝚈𝙾𝚄𝚁 **𝙿𝙷𝙾𝙽𝙴_𝙽𝚄𝙼𝙱𝙴𝚁** 𝚆𝙸𝚃𝙷 𝙲𝙾𝚄𝙽𝚃𝚁𝚈 𝙲𝙾𝙳𝙴 𝙵𝙾𝚁 𝚆𝙷𝙸𝙲𝙷 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙲𝚁𝙴𝙰𝚃𝙴 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 📌. \n : `+910000000000`'"
    else:
        t = "🛡 𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙴𝙽𝙳 𝚈𝙾𝚄𝚁 **𝙱𝙾𝚃_𝚃𝙾𝙺𝙴𝙽** 𝚃𝙾 𝙲𝙾𝙽𝚃𝙸𝙽𝚄𝙴 🛡.\n 𝙴𝚇𝙰𝙼𝙿𝙻𝙴 : `5432198765:abcdvenomterabaaplol`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("👻 𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚂𝙴𝙽𝙳 𝙾𝚃𝙿 𝙰𝚃 𝚃𝙷𝙴 𝙶𝙸𝚅𝙴𝙽 𝙽𝚄𝙼𝙱𝙴𝚁 👻")
    else:
        await msg.reply("🤖 𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙻𝙾𝙶𝙸𝙽 𝚅𝙸𝙰 𝙱𝙾𝚃 𝚃𝙾𝙺𝙴𝙽 🤖")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply("🥶 𝚈𝙾𝚄𝚁 **𝙰𝙿𝙸_𝙸𝙳** 𝙰𝙽𝙳 **𝙰𝙿𝙸_𝙷𝙰𝚂𝙷** 𝙲𝙾𝙼𝙱𝙸𝙽𝙰𝚃𝙸𝙾𝙽 𝙳𝙾𝙴𝚂𝙽'𝚃 𝙼𝙰𝚃𝙲𝙷 𝚆𝙸𝚃𝙷 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙰𝙿𝙸 𝚂𝚈𝚂𝚃𝙴𝙼. \n\n 𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝚃𝙰𝚁𝚃 𝙲𝚁𝙴𝙰𝚃𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 𝙰𝙶𝙰𝙸𝙽 🥶", reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply("🥵 𝚃𝙷𝙴 **𝙿𝙷𝙾𝙽𝙴_𝙽𝚄𝙼𝙱𝙴𝚁** 𝚈𝙾𝚄'𝚅𝙴 𝚂𝙴𝙽𝚃 𝙳𝙾𝙴𝚂𝙽'𝚃 𝙱𝙴𝙻𝙾𝙽𝙶 𝚃𝙾 𝙰𝙽𝚈 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙰𝙲𝙲𝙾𝚄𝙽𝚃.\n\n𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝚃𝙰𝚁𝚃 𝙲𝚁𝙴𝙰𝚃𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 𝙰𝙶𝙰𝙸𝙽 🥵", reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "🥀 𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 **𝙾𝚃𝙿** 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄'𝚅𝙴 𝚁𝙴𝙲𝙴𝙸𝚅𝙴𝙳 𝙵𝚁𝙾𝙼 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙾𝙽 𝚈𝙾𝚄𝚁 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 🥀.\n𝙸𝙵 𝙾𝚃𝙿 𝙸𝚂 `12345`, **𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙴𝙽𝙳 𝙸𝚃 𝙰𝚂** `1 2 3 4 5`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("💫 𝚃𝙸𝙼𝙴 𝙻𝙸𝙼𝙸𝚃 𝚁𝙴𝙰𝙲𝙷𝙴𝙳 𝙾𝙵 10 𝙼𝙸𝙽𝚄𝚃𝙴𝚂.\n\n𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝚃𝙰𝚁𝚃 𝙲𝚁𝙴𝙰𝚃𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 𝙰𝙶𝙰𝙸𝙽 💫", reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply("💞 𝚃𝙷𝙴 𝙾𝚃𝙿 𝚈𝙾𝚄'𝚅𝙴 𝚂𝙴𝙽𝙳 𝙸𝚂 **𝚆𝚁𝙾𝙽𝙶.**\n\n𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝚃𝙰𝚁𝚃 𝙲𝚁𝙴𝙰𝚃𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 𝙰𝙶𝙰𝙸𝙽 💞", reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply("🔥 𝚃𝙷𝙴 𝙾𝚃𝙿 𝚈𝙾𝚄'𝚅𝙴 𝚂𝙴𝙽𝚃 𝙸𝚂 **𝙴𝚇𝙿𝙸𝚁𝙴𝙳.**\n\n𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝚃𝙰𝚁𝚃 𝙲𝚁𝙴𝙰𝚃𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 𝙰𝙶𝙰𝙸𝙽 🔥", reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, "❣️ 𝙿𝙻𝙴𝙰𝚂𝙴 𝙴𝙽𝚃𝙴𝚁 𝚈𝙾𝚄𝚁 **𝚃𝚆𝙾 𝚂𝚃𝙴𝙿 𝚅𝙴𝚁𝙸𝙵𝙸𝙲𝙰𝚃𝙸𝙾𝙽** 𝙿𝙰𝚂𝚂𝚆𝙾𝚁𝙳 𝚃𝙾 𝙲𝙾𝙽𝚃𝙸𝙽𝚄𝙴 ❣️", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("💢 𝚃𝙸𝙼𝙴 𝙻𝙸𝙼𝙸𝚃 𝚁𝙴𝙰𝙲𝙷𝙴𝙳 𝙾𝙵 5 𝙼𝙸𝙽𝚄𝚃𝙴𝚂.\n\n𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝚃𝙰𝚁𝚃 𝙲𝚁𝙴𝙰𝚃𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 𝙰𝙶𝙰𝙸𝙽 💢", reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply("💗 𝚃𝙷𝙴 𝙿𝙰𝚂𝚂𝚆𝙾𝚁𝙳 𝚈𝙾𝚄'𝚅𝙴 𝚂𝙴𝙽𝚃 𝙸𝚂 𝚆𝚁𝙾𝙽𝙶.\n\n𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝚃𝙰𝚁𝚃 𝙲𝚁𝙴𝙰𝚃𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 𝙰𝙶𝙰𝙸𝙽 💗", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**💘 𝚃𝙷𝙸𝚂 𝙸𝚂 𝚈𝙾𝚄𝚁 {ty} 𝚂𝚃𝚁𝙸𝙽𝙶 𝚂𝙴𝚂𝚂𝙸𝙾𝙽 💘** \n\n`{string_session}` \n\n**𝙲𝚁𝙴𝙰𝚃𝙴𝙳 𝙱𝚈 :** @StringGenerator_Bot\n🔓 **𝙽𝙾𝚃𝙴 :** 𝙳𝙾𝙽'𝚃 𝚂𝙷𝙰𝚁𝙴 𝙸𝚃 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁 𝙶𝙸𝚁𝙻𝙵𝚁𝙸𝙴𝙽𝙳 𝙰𝙽𝙳 𝙳𝙾𝙽'𝚃 𝙵𝙾𝚁𝙶𝙾𝚃 𝚃𝙾 𝙹𝙾𝙸𝙽 @TheNight_City 📌"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "💕 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙲𝚁𝙴𝙰𝚃𝙴𝙳 𝚈𝙾𝚄𝚁 {} 𝚂𝚃𝚁𝙸𝙽𝙶 𝚂𝙴𝚂𝚂𝙸𝙾𝙽.\n\n𝙿𝙻𝙴𝙰𝚂𝙴 𝙲𝙷𝙴𝙲𝙺 𝚈𝙾𝚄𝚁 𝚂𝙰𝚅𝙴𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝙶𝙴𝚃 𝙸𝚃 ! \n\n**𝙰 𝚂𝚃𝚁𝙸𝙽𝙶 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 𝙱𝙾𝚃 𝙱𝚈** @TheNight_City 💕".format("🥵 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 🥵" if telethon else "💘 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 💘"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("**❌ 𝙲𝙰𝙽𝙲𝙴𝙻𝙻𝙴𝙳 𝚃𝙷𝙴 𝙾𝙽𝙶𝙾𝙸𝙽𝙶 𝚂𝚃𝚁𝙸𝙽𝙶 𝙲𝚁𝙴𝙰𝚃𝙸𝙾𝙽 𝙿𝚁𝙾𝙲𝙴𝚂𝚂 ❌**", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("**✌ 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝚃𝙷𝙴 𝙱𝙾𝚃 𝙵𝙾𝚁 𝚈𝙾𝚄 ✌**", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("**❌ 𝙲𝙰𝙽𝙲𝙴𝙻𝙻𝙴𝙳 𝚃𝙷𝙴 𝙾𝙽𝙶𝙾𝙸𝙽𝙶 𝚂𝚃𝚁𝙸𝙽𝙶 𝙲𝚁𝙴𝙰𝚃𝙸𝙾𝙽 𝙿𝚁𝙾𝙲𝙴𝚂𝚂 ❌**", quote=True)
        return True
    else:
        return False
