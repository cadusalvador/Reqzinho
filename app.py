from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from chatbot.parser import extrair_dados
from chatbot.seatalk_api import SeatalkClient
from automacao.login import login_erp
from automacao.requisicao import criar_requisicao

load_dotenv()

app = Flask(__name__)
seatalk = SeatalkClient(
    api_url=os.getenv("SEATALK_API_URL"),
    bot_token=os.getenv("SEATALK_BOT_TOKEN")
)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)

    # Exemplo de payload esperado:
    # {
    # "room_id": "...",
    # "sender": {"id": "...", "name": "..."},
    # "text": "@Reqzinho Poderia criar... ID00031: 1 UN"
    # }

    texto = (data.get("text") or "").strip()

    if not texto:
        return jsonify({"ok": True}), 200
    
    if "@Reqzinho" not in texto:
        return jsonify({"ok": True}), 200
    
    dados = extrair_dados(texto)
    if not dados:
        seatalk.send_message(
            room_id=data.get("room_id"),
            text=("❌ Não consegui identificar os dados da requisição. "
"Use o formato: ID00031: 1 UN")
        )
        return jsonify({"ok": True}), 200
    
    try:
        driver = login_erp()
    except Exception as e:
        try:
            driver.quit()
        except:
            pass
        seatalk.send_message(room_id=data.get("room_id"), text=(f"❌ Erro ao criar requisição: {e}"))

    return jsonify({"ok": True}), 200


if __name__ == '__main__':
    host = os.getenv("FLASK_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_PORT", 5000))
    app.run(host=host, port=port)