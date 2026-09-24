import os
import json
import urllib.request

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def enviar_mensagem(texto):
    if not TOKEN or not CHAT_ID:
        print("Erro: Chaves do Telegram não encontradas!")
        return
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = json.dumps({
        "chat_id": CHAT_ID,
        "text": texto,
        "parse_mode": "Markdown"
    }).encode("utf-8")
    
    req = urllib.request.Request(
        url, 
        data=payload, 
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            print("Mensagem enviada com sucesso para o Telegram!")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

if __name__ == "__main__":
    mensagem_teste = (
        "🚨 *SISTEMA DE ARBITRAGEM CONECTADO!*\n\n"
        "Seu robô de alertas está oficial no Telegram.\n"
        "Tudo certo para integrarmos o painel visual!"
    )
    enviar_mensagem(mensagem_teste)
