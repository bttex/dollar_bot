import telebot
import requests
import time

# Token do seu bot no Telegram
TOKEN = '5047466592:AAFsw00a1QBDP1i7v8W5dw2o1LKSi0EFdWo'

# ID do chat para onde serão enviadas as notificações
CHAT_ID = '571724768'

# URL da API para obter a cotação do dólar em relação ao Real
API_URL = 'https://open.er-api.com/v6/latest/USD'

# Valor de referência para notificar quando o dólar baixar
VALOR_REFERENCIA = 5.0  # Substitua pelo valor desejado

# Inicializa o bot
bot = telebot.TeleBot(TOKEN)

# Função para obter a cotação do dólar
def obter_cotacao_dolar():
    try:
        response = requests.get(API_URL)
        data = response.json()
        return data['rates']['BRL']
    except Exception as e:
        print(f"Erro ao obter cotação: {e}")
        return None

# Função para enviar notificação
def enviar_notificacao(chat_id, mensagem):
    bot.send_message(chat_id, mensagem)

# Função para verificar a cotação do dólar e enviar notificação se baixar
def verificar_cotacao():
    while True:
        cotacao_atual = obter_cotacao_dolar()

        if cotacao_atual is not None and cotacao_atual <= VALOR_REFERENCIA:
            mensagem = f'O valor do dólar baixou para {cotacao_atual:.2f}!'
            enviar_notificacao(CHAT_ID, mensagem)

        # Intervalo de 1 hora (3600 segundos)
        time.sleep(28800)

# Inicia a verificação da cotação em uma thread separada
if __name__ == "__main__":
    import threading
    thread = threading.Thread(target=verificar_cotacao)
    thread.start()

# Mantém o bot rodando
bot.polling(none_stop=True)
