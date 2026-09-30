from flask import Flask

from app.database import init_db


def create_app():
    # Flask uygulamasını oluşturur
    app = Flask(__name__)

    # Uygulama ayarlarını yükler
    from config import Config
    app.config.from_object(Config)

    # Veritabanını hazırlar
    init_db()

    # Ana route'ları uygulamaya bağlar
    from app.routes import main
    app.register_blueprint(main)

    return app