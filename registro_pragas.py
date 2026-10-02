# AgroCampo - registro de ocorrencia de pragas por talhao
def registrar_praga(talhao, praga, nivel_infestacao, data, foto=None):
    return {
        "talhao": talhao,
        "praga": praga,
        "nivel_infestacao": nivel_infestacao,
        "data": data,
        "foto": foto,
    }
