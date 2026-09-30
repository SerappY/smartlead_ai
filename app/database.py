import sqlite3
from pathlib import Path


# Veritabanı dosyasının konumunu belirler
DATABASE_PATH = Path(__file__).resolve().parent.parent / "smartlead.db"


def get_db_connection():
    # SQLite veritabanına bağlantı açar
    connection = sqlite3.connect(DATABASE_PATH)

    # Sorgu sonuçlarına sütun isimleriyle erişmemizi sağlar
    connection.row_factory = sqlite3.Row

    return connection


def init_db():
    # Veritabanına bağlanır
    connection = get_db_connection()

    # Lead bilgilerini saklayacak tabloyu oluşturur
    connection.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            topic TEXT,
            business_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Yapılan değişiklikleri kaydeder
    connection.commit()

    # Veritabanı bağlantısını kapatır
    connection.close()


def add_lead(name, phone, topic=None, business_name=None):
    # Yeni bir lead kaydı oluşturur
    connection = get_db_connection()

    connection.execute(
        """
        INSERT INTO leads (name, phone, topic, business_name)
        VALUES (?, ?, ?, ?)
        """,
        (name, phone, topic, business_name)
    )

    # Yeni kaydı veritabanına kaydeder
    connection.commit()

    # Bağlantıyı kapatır
    connection.close()