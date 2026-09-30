from flask import Blueprint, render_template, request, jsonify

from app.services.ai_service import generate_response


# Ana uygulama sayfalarının route'larını burada tutuyoruz
main = Blueprint("main", __name__)


@main.route("/")
def index():
    # Kullanıcı ana adrese geldiğinde giriş sayfasını gösterir
    return render_template("index.html")


@main.route("/chat", methods=["POST"])
def chat():
    # Tarayıcıdan gelen JSON verisini alır
    data = request.get_json()

    # Kullanıcının mesajını alır
    user_message = data.get("message", "").strip()

    # Boş mesaj gönderilmesini engeller
    if not user_message:
        return jsonify({
            "error": "Mesaj boş olamaz."
        }), 400

    try:
        # Kullanıcı mesajını Mira'ya gönderir
        response = generate_response(user_message)

        # Mira'nın cevabını JSON olarak döndürür
        return jsonify({
            "response": response
        })

    except Exception as error:
        # Hata oluşursa sunucu tarafında gösterir
        print(f"Mira hatası: {error}")

        return jsonify({
            "error": "Mira şu anda cevap veremiyor."
        }), 500