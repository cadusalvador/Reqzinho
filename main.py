from utils.helpers import load_env, log
from chatbot.handler import handle_message

import time

if __name__ == '__main__':
    config = load_env()
    exemplo = "Por favor, poderia criar uma requisição do:\nID00218 - 65UN,\nID00097 - 25UN! Obrigado!"
    response = handle_message(exemplo, sender='teste_local', config=config)
    print('Resposta gerada: ', response)