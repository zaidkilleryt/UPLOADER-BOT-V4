import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6009374977:AAEIfV-kp9FhRwUUvH6JNNX1mY2FNn2MRlM")

    API_ID = int(os.environ.get("API_ID", 𝟮𝟴𝟰𝟰𝟭𝟭𝟭𝟴))

    API_HASH = os.environ.get("API_HASH", "𝟯𝗰𝟲𝟴𝗮𝟰𝗰𝗰𝟵𝟭𝟭𝗰𝗰𝟵𝟬𝗯𝗯𝗰𝗮𝗯𝗲𝟲𝗯𝟯𝟰𝟯𝟯𝟯𝟯𝟬𝗯𝟲")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5410723702").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "sony_sab_all_shows_available")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @jdissbh_bot"

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://zaidkilleryt:zaidali@007@cluster0.lwnjeyy.mongodb.net/?retryWrites=true&w=majority

")

    SESSION_NAME = os.environ.get("SESSION_NAME", "jdissbh_bot")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001743813268))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "1405897472"))

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "sony_sab_all_shows_available")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "jdissbh_bot")

    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))

    PRO_USERS.append(OWNER_ID)
