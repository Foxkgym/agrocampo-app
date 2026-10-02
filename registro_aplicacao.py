# AgroCampo - registro de aplicacao de defensivos
def registrar_aplicacao(talhao, produto, dose_por_hectare, data, responsavel_tecnico):
    return {
        "talhao": talhao,
        "produto": produto,
        "dose_por_hectare": dose_por_hectare,
        "data": data,
        "responsavel_tecnico": responsavel_tecnico,
        "sincronizado": False,
    }
