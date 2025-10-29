def formato_sucesso(numero: str, base_url: str):
    return f"✅ Requisição criada com sucesso!\nNº: {numero}\n🔗 {base_url.rstrip('/')}/app/material-request/{numero}"

def formato_erro(erro: str):
    return f"❌ Erro ao criar requisição: {erro}"