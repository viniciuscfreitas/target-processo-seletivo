
# Target Sistemas - Processo Seletivo

Soluções para os desafios do processo seletivo da Target Sistemas, desenvolvidas em Python. O projeto inclui scripts para resolver cada problema proposto, além de testes unitários para verificar o funcionamento correto das soluções.

## Estrutura do Projeto

```
target-sistemas-processo-seletivo/
├── problema1.py          # Cálculo de soma acumulativa
├── problema2.py          # Verificação de número na sequência de Fibonacci
├── problema3.py          # Análise de faturamento diário
├── problema4.py          # Cálculo de percentual de faturamento por estado
├── problema5.py          # Inversão de uma string
├── faturamento.json      # Exemplo de dados para o problema 3
├── test_solucoes.py      # Testes unitários para todas as soluções
└── README.md             # Este arquivo
```

## Descrição dos Problemas

1. **Problema 1**: Cálculo do valor final de uma soma acumulativa.
2. **Problema 2**: Verificação se um número pertence à sequência de Fibonacci.
3. **Problema 3**: Análise do faturamento diário de uma distribuidora para encontrar o menor, o maior valor e a quantidade de dias acima da média.
4. **Problema 4**: Cálculo do percentual de faturamento de uma distribuidora por estado.
5. **Problema 5**: Inversão de uma string.

## Como Executar os Scripts

1. Certifique-se de ter o Python instalado. Você pode verificar a instalação executando:
   ```bash
   python3 --version
   ```

2. Para executar qualquer um dos scripts, use o comando:
   ```bash
   python3 nome_do_script.py
   ```

   Por exemplo, para rodar o `problema1.py`:
   ```bash
   python3 problema1.py
   ```

3. Para o problema 3, certifique-se de que o arquivo `faturamento.json` está presente no diretório e no formato correto.

## Exemplo de Formato do JSON para o Problema 3

O arquivo `faturamento.json` deve ter o seguinte formato:
```json
[
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 0},
    {"dia": 4, "valor": 26139.6134},
    {"dia": 5, "valor": 0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722}
]
```

## Como Executar os Testes Unitários

Para rodar os testes unitários e verificar se todas as soluções estão corretas, utilize o comando:
```bash
python3 -m unittest test_solucoes.py
```

Os testes cobrem todos os problemas e garantem que os resultados estejam de acordo com o esperado.

## Dependências

Nenhuma dependência externa é necessária para executar os scripts e os testes.

## Licença

Este projeto é apenas para fins de avaliação no processo seletivo da Target Sistemas.
