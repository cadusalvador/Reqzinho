import re

def extrair_dados(message: str):
    """
    Extrai ID, quantidade e unidade de mensagens no formato:
    ID00031: 1 UN
    ID 00031 - 1 UN
    Retorna dict: {"id": "00031", "quantidade": 1, "unidade": "UN"}
    """
    texto = (message or "")

    padrao = r"ID\s*(\d+)\s*[:\-]\s*(\d+)\s*([A-Z]{1,4})?"
    m = re.search(padrao, texto)
    if not m:
        return None
    
    return {"id": m.group(1).zfill(5), "quantidade": int(m.group(2)), "unidade": (m.group(3) or "UN")}

# teste
if __name__ == '__main__':
    exemplo = "@Reqzinho\nPoderia criar uma requisição por favor?\nID00042: 1 UN"
    print(extrair_dados(exemplo))
