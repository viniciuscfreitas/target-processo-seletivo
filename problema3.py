# problema3.py
import json

def calcular_faturamento(dados):
    faturamento_diario = [dia['valor'] for dia in dados if dia['valor'] > 0]

    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)

    dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

if __name__ == '__main__':
    try:
        with open('faturamento.json', 'r') as file:
            dados = json.load(file)
        
        if not dados:
            raise ValueError("O arquivo 'faturamento.json' está vazio.")

        menor, maior, dias_acima_media = calcular_faturamento(dados)
        print(f"Menor faturamento: R${menor:.2f}")
        print(f"Maior faturamento: R${maior:.2f}")
        print(f"Dias acima da média: {dias_acima_media}")
    
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON. Verifique se 'faturamento.json' contém um formato válido.")
    except FileNotFoundError:
        print("O arquivo 'faturamento.json' não foi encontrado.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")