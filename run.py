from app import create_app


# Flask uygulamasını uygulama fabrikasından oluşturur
app = create_app()


if __name__ == "__main__":
    # Yerel geliştirme ortamında uygulamayı çalıştırır
    app.run(port=5000)