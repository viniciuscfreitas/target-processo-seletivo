# problema5.py
def inverter_string(s):
    resultado = ""
    for char in s:
        resultado = char + resultado
    return resultado

if __name__ == '__main__':
    string_original = input("Digite uma string para inverter: ")
    string_invertida = inverter_string(string_original)
    print("String invertida:", string_invertida)