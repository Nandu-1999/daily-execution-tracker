from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./ci.db"
)

SECRET_KEY = os.getenv("SECRET_KEY") or "dev-secret"

ALGORITHM = os.getenv("ALGORITHM") or "HS256"


ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES") or "30"
)