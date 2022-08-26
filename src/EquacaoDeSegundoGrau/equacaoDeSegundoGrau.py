import unittest 
from functools import cached_property

class EquacaoSegundoGrau:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    @cached_property
    def delta(self):
        return self.b**2-4*self.a*self.c

    def raizes(self):
        if (self.a == 0):
            raise ValueError("O parâmetro a não pode ser igual a 0")
        
        if (self.delta < 0):
            return None, None
        elif (self.delta == 0):
            x1 = (-self.b + self.delta**(1/2)) / (2*self.a)
            return x1, None
        else:
            x1 = (-self.b + self.delta**(1/2)) / (2*self.a)
            x2 = (-self.b - self.delta**(1/2)) / (2*self.a)
            return x1, x2


class TestEquacaoSegundoGrau(unittest.TestCase):
    def _executa_raizes(self, a, b, c):
        obj = EquacaoSegundoGrau(a, b, c)
        return obj.raizes()
    
    def test_duas_raizes_positivas(self):
        raizes = self._executa_raizes(1, -6, 5)
        assert raizes == (5.0, 1.0)
    
    def test_duas_raizes_negativas(self):
        raizes = self._executa_raizes(3, 4, 1)
        assert round(raizes[0], 2) == -0.33
        assert raizes[1] == -1.0
    
    def test_duas_raizes_positiva_negativa(self):
        raizes = self._executa_raizes(1, -3, -10)
        assert raizes == (5.0, -2.0)

    def test_unica_raiz_monos_um(self):
        raizes = self._executa_raizes(1, 2, 1)
        assert raizes == (-1.0, None)
    
    def test_unica_raiz_menos_dois(self):
        raizes = self._executa_raizes(1, 4, 4)
        assert raizes == (-2.0, None)

    def test_sem_raizes_existentes(self):
        raizes = self._executa_raizes(9, 5, 4)
        assert raizes == (None, None)
    
    def test_raizes_com_a_igual_zero(self):
        with self.assertRaises(ValueError):
            self._executa_raizes(0, -6, 5)

    def test_raizes_com_b_igual_zero(self):
        raizes = self._executa_raizes(1, 0, -4)
        breakpoint()
        assert raizes == (2.0, -2.0)

    def test_raizes_com_c_igual_zero(self):
        raizes = self._executa_raizes(1, 2, 0)
        breakpoint()
        assert raizes == (0.0, -2.0)


if __name__ == '__main__':
    unittest.main()