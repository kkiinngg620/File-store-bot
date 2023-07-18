import os

API_ID = int(os.environ.get("API_ID", "27157998"))
API_HASH = os.environ.get("API_HASH", "45d09c93e37c9b93b6535949c898f906")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6300428067:AAHs7bNn1eFkcRUaWTo3b23Q3YJXfftkvcE")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", "-1001900692143")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID", "1452198353"))
PROTECT_CONTENT = False
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', 'moviieeadda3')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
