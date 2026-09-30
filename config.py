import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Uygulamanın temel Flask ayarları
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

    # Yapay zekâ servisinde kullanılacak API anahtarı
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")