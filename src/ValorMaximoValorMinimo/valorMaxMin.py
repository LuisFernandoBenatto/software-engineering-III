import unittest 

from functools import cached_property

class MaxMin:
    def __init__(self, valores):
        self.valores = valores

    def maximo_valor(self):
        numero_maximo = self.valores[0]
        for valor in self.valores:
            if numero_maximo < valor:
                numero_maximo = valor
        return numero_maximo

    @cached_property
    def max(self):
        return self.maximo_valor()

    def minimo_valor(self):
        valor_minimo = self.valores[0]
        for valor in self.valores:
            if valor_minimo > valor:
                valor_minimo = valor
        return valor_minimo

    @cached_property
    def min(self):
        return self.minimo_valor()

    def resultado(self):
        return self.max, self.min

class TesteMaxMin(unittest.TestCase):
    def _executa_max_min(self, valores):
        obj = MaxMin(valores)
        valor_max_e_min = obj.resultado()
        return valor_max_e_min

    def teste_max_e_minimo(self):
        valores = [15.0, 43.0, 17.0, 52.0, 22.55, 5.06, 87.0, 75.0]
        valor_max_e_min = self._executa_max_min(valores)
        assert valor_max_e_min == (87.0, 5.06)

    def teste_max(self):
        valores = [15.0, 43.0, 17.0, 52.0, 22.55, 5.06, 87.0, 75.0]
        obj = MaxMin(valores)
        assert obj.max == 87.0

    def teste_min(self):
        valores = [15.0, 43.0, 17.0, 52.0, 22.55, 5.06, 87.0, 75.0]
        obj = MaxMin(valores)
        assert obj.min == 5.06

    def teste_max_e_min_com_um_valor_na_lista(self):
        valores = 520
        valor_max_e_min = self._executa_max_min([valores])
        assert valor_max_e_min == (valores, valores)

if __name__ == '__main__':
    unittest.main()