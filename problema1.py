# problema1.py
def main():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K += 1
        SOMA += K

    return SOMA

if __name__ == '__main__':
    resultado = main()
    print("Valor final de SOMA:", resultado)