import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "14202110").strip()
API_HASH = os.getenv("API_HASH", "45f3a3ac8effd88e42aeabe3cfe4f520").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "5537497510").split()))
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "TheNight_City")

if not API_ID:
    print("𝙽𝚘 𝙰𝙿𝙸_𝙸𝙳 𝚏𝚘𝚞𝚗𝚍. 𝙵𝚄𝙲𝙺 𝙾𝙵𝙵 😏...")
    raise SystemExit
if not API_HASH:
    print("𝙽𝚘 𝙰𝙿𝙸_𝙷𝙰𝚂𝙷 𝚏𝚘𝚞𝚗𝚍. 𝙵𝚄𝙲𝙺 𝙾𝙵𝙵 😏...")
    raise SystemExit
if not BOT_TOKEN:
    print("𝙽𝚘 𝙱𝙾𝚃_𝚃𝙾𝙺𝙴𝙽 𝚏𝚘𝚞𝚗𝚍. 𝙵𝚄𝙲𝙺  𝙾𝙵𝙵 😏...")
    raise SystemExit
if not DATABASE_URL:
    print("𝙽𝚘 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴_𝚄𝚁𝙻 𝚏𝚘𝚞𝚗𝚍. 𝙵𝚄𝙲𝙺 𝙾𝙵𝙵 😏...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("𝙰𝙿𝙸_𝙸𝙳 𝚒𝚜 𝚗𝚘𝚝 𝚊 𝚟𝚊𝚕𝚒𝚍 𝚒𝚗𝚝𝚎𝚐𝚎𝚛. 𝙵𝚄𝙲𝙺 𝙾𝙵𝙵 😏...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
