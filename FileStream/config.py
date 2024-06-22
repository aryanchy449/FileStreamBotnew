from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get("API_ID","23080322"))
    API_HASH = str(env.get("API_HASH","b3611c291bf82d917637d61e4a136535"))
    BOT_TOKEN = str(env.get("BOT_TOKEN","6613620736:AAHUWQIPnyn6YRd-zkPzAMsbxs0MogZoI0o"))
    OWNER_ID = int(env.get('OWNER_ID', '6214889840'))
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get("DATABASE_URL","mongodb+srv://chaunisha765:hello@cluster0.v0tm2yj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
    UPDATES_CHANNEL = str(env.get("UPDATES_CHANNEL", "-1002111184944"))
    SESSION_NAME = str(env.get("SESSION_NAME", "FileStream"))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', None)
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', False)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    START_PIC = env.get('START_PIC', "https://graph.org/file/290af25276fa34fa8f0aa.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL","-1002111184944"))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL","-1002111184944"))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "https://bold-locket-bitter-slave-production.pipeops.app"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "120"))
    HAS_SSL = str(env.get("HAS_SSL", "True"))
    NO_PORT = str(env.get("NO_PORT", "False"))
    FQDN = str(env.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN
    )



