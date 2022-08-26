import unittest 
import copy    

class BubbleSort:
    def __init__(self, numeros):
        self.numeros = numeros

    @staticmethod
    def _swap(x, y, numeros):
        numeros[y], numeros[x] = numeros[x], numeros[y]

    def sort(self, inplace: bool = False):
        numeros = copy.deepcopy(self.numeros) if not inplace else self.numeros
        len_valor= len(numeros) - 1

        swapped = False
        for i in range(len_valor):
            for j in range(len_valor - i):
                if numeros[j] > numeros[j + 1]:
                    self._swap(j + 1, j, numeros)
                    swapped = True

            if not swapped:
                return numeros

        return numeros

class TestBubbleSort(unittest.TestCase):
    def _executando_bubble_sort(self, valores):
        obj = BubbleSort(valores)
        numeros_ordenados = obj.sort()
        return numeros_ordenados

    def test_sort_numeros(self):
        numeros = [64.11, 34, 25.44, 12, 22, 11, 90]
        numeros_ordenados = self._executando_bubble_sort(numeros)
        breakpoint()
        assert numeros_ordenados != numeros

        numeros_esperados = [11, 12, 22, 25.44, 34, 64.11, 90]
        assert numeros_ordenados == numeros_esperados

    def test_sort_numeros_reverted(self):
        numeros = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        numeros_ordenados = self._executando_bubble_sort(numeros)
        breakpoint()
        assert numeros_ordenados != numeros

        assert numeros_ordenados == numeros[::-1]

    def test_sort_numeros_already_ordenados(self):
        numeros = [11, 12, 22, 25, 34, 64, 90]
        numeros_ordenados = self._executando_bubble_sort(numeros)
        breakpoint()
        assert numeros_ordenados == numeros

    def test_sort_numeros_inplace(self):
        numeros = [64, 34, 25, 12, 22, 11, 90]
        numeros_copiado = copy.deepcopy(numeros)

        obj = BubbleSort(numeros)
        numeros_ordenados = obj.sort(inplace=True)
        assert numeros_ordenados != numeros_copiado
        assert numeros_ordenados == numeros
        numeros_esperados = [11, 12, 22, 25, 34, 64, 90]
        assert numeros_ordenados == numeros_esperados

if __name__ == '__main__':
    unittest.main()