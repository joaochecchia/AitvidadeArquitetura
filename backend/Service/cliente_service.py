# Função que calcula o núcleo do usuário
def calc_nucleo(cliente: Cliente) -> Resposta:
    c = [cliente.balance, cliente.purchases, cliente.cash_advance, cliente.credit_limit, cliente.payments]
    k = modelo.predict([c])
    resp = {
        "nome": cliente.name,
        "cluster": k[0],
        "resposta": respostas[k[0]]
    }
    r = Resposta(**resp)
    return r