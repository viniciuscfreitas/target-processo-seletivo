# test_solucoes.py
import unittest
from problema1 import main as problema1_main
from problema2 import is_fibonacci
from problema3 import calcular_faturamento
from problema4 import calcular_percentual_por_estado
from problema5 import inverter_string

class TestProblemas(unittest.TestCase):

    def test_problema1(self):
        resultado = problema1_main()
        self.assertEqual(resultado, 91, "O valor de SOMA deve ser 91")

    def test_problema2(self):
        self.assertTrue(is_fibonacci(21), "21 deve pertencer à sequência de Fibonacci")
        self.assertTrue(is_fibonacci(0), "0 deve pertencer à sequência de Fibonacci")
        self.assertFalse(is_fibonacci(4), "4 não pertence à sequência de Fibonacci")

    def test_problema3(self):
        faturamento_mock = [
            {"dia": 1, "valor": 1000.0},
            {"dia": 2, "valor": 0.0},
            {"dia": 3, "valor": 2000.0},
            {"dia": 4, "valor": 3000.0},
            {"dia": 5, "valor": 0.0},
            {"dia": 6, "valor": 4000.0}
        ]
        menor, maior, dias_acima_media = calcular_faturamento(faturamento_mock)
        self.assertEqual(menor, 1000.0, "O menor valor de faturamento deve ser 1000.0")
        self.assertEqual(maior, 4000.0, "O maior valor de faturamento deve ser 4000.0")
        self.assertEqual(dias_acima_media, 2, "Deve haver 2 dias com faturamento acima da média")

    def test_problema4(self):
        faturamento_mock = {
            'SP': 67836.43,
            'RJ': 36678.66,
            'MG': 29229.88,
            'ES': 27165.48,
            'Outros': 19849.53
        }
        resultado = calcular_percentual_por_estado(faturamento_mock)
        
        # Arredonda os percentuais para duas casas decimais antes da verificação
        percentual_SP = round(resultado['SP'], 2)
        percentual_RJ = round(resultado['RJ'], 2)
        
        self.assertAlmostEqual(percentual_SP, 37.53, places=2, msg="Percentual de SP incorreto")
        self.assertAlmostEqual(percentual_RJ, 20.29, places=2, msg="Percentual de RJ incorreto")

    def test_problema5(self):
        self.assertEqual(inverter_string("abcd"), "dcba", "A inversão de 'abcd' deve ser 'dcba'")
        self.assertEqual(inverter_string("Target"), "tegraT", "A inversão de 'Target' deve ser 'tegraT'")
        self.assertEqual(inverter_string(""), "", "A inversão de uma string vazia deve ser vazia")

if __name__ == '__main__':
    unittest.main()