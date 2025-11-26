import os

API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# DEFAULT LIMITS (0 = unlimited)
DEFAULT_DAILY_COUNT_LIMIT = int(os.getenv("DEFAULT_DAILY_COUNT_LIMIT", "10"))   # uploads per day
DEFAULT_DAILY_SIZE_LIMIT_MB = int(os.getenv("DEFAULT_DAILY_SIZE_LIMIT_MB", "2000"))  # MB per day (2GB)
PREMIUM_DAILY_COUNT_LIMIT = int(os.getenv("PREMIUM_DAILY_COUNT_LIMIT", "100"))
PREMIUM_DAILY_SIZE_LIMIT_MB = int(os.getenv("PREMIUM_DAILY_SIZE_LIMIT_MB", "10000"))  # 10GB

# Telegram bot per-file limit (~2GB)
MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024  # bytes

ADMIN_IDS = [
    int(x) for x in os.getenv("ADMINS", "").split(",") if x.strip().isdigit()
]

LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))  # -100...
BOT_USERNAME = os.getenv("BOT_USERNAME", "MyUploaderBot")

# Proxy support
PROXY_URL = os.getenv("PROXY_URL", "").strip()
PROXIES = {"http": PROXY_URL, "https": PROXY_URL} if PROXY_URL else None

# cookies.txt path (for yt-dlp)
COOKIES_FILE = os.getenv("COOKIES_FILE", "/app/cookies.txt")
