from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "3706077"))
API_HASH = getenv("API_HASH", "5bec73923f996b3092a4209ac556bc58")
BOT_TOKEN = getenv("BOT_TOKEN","5256670460:AAEXOw4IIoBTZ-Bc2sbn36qCUkbPbmmn-8c")
BOT_NAME = getenv("BOT_NAME","SakuXplincy")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "AQAY72IGhknQqz7kQ1j5qqV-gANouz3RU25GnF3k5DWXVxqJMEvymiMwCTMvcygHdtIAPMQUIA5BJiNNP57_nz1ZyjThLcAMtWfIPf9EPlSvrD-qXd-2siOPL1fHlppts36G-zD5G0OrlxlYPZcbBG_3gP0oMHiACm-QF3YiYmB5uvrtQhBA27KV8VHFVP5TJR4zvU9FNxy8ao7bxgOfqCoc6jR-2Uu0c2hNBCDCJ3Z-h8BHNBfCt0cu4e5iekVFvGQlOhe7TYyWF6493vDwDRYjgKXqff3ORlrkx_qLACkDvDf0d2G5719o4vadeBM6cEWYumGDT6oZLZhOPwMVkFGbAAAAASol1I8A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5304720899").split()))
