# problema4.py
def calcular_percentual_por_estado(faturamento_por_estado):
    faturamento_total = sum(faturamento_por_estado.values())
    return {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_por_estado.items()}

if __name__ == '__main__':
    faturamento_por_estado = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }
    resultado = calcular_percentual_por_estado(faturamento_por_estado)
    for estado, percentual in resultado.items():
        print(f"{estado}: {percentual:.2f}% do faturamento total")