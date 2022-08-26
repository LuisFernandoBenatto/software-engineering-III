import unittest 

class Palindromo:
    def __init__(self, texto):
        self.texto = texto
        
    def palindromo(self) -> bool:
        if not isinstance(self.texto, str):
            raise ValueError("O texto deve ser uma String")

        textoSemEspacos = self.texto.replace(' ', '')
        textoMinusculo = textoSemEspacos.lower()
        textoInvertido = textoMinusculo[::-1]
        if textoInvertido == textoMinusculo:
            return True
        else:
            return False

class TestPalindromo(unittest.TestCase):
    def _executa_palindromo(self, texto):
        obj = Palindromo(texto)
        return obj.palindromo()

    def test_palindromo_arara_returna_true(self):
        texto = self._executa_palindromo("arara")
        assert texto == True

    def test_palindromo_roma_returna_true(self):
        texto = self._executa_palindromo("Roma me tem amor")
        assert texto == True

    def test_palindromo_sairam_returna_true(self):
        texto = self._executa_palindromo("Sairam o tio e oito Marias")
        assert texto == True
    
    def test_nao_palindromo(self):
        texto = self._executa_palindromo("palindromo")
        assert texto == False
    
    def test_palindromo_de_numeros(self):
        with self.assertRaises(ValueError):
            self._executa_palindromo(123454321)

if __name__ == '__main__':
    unittest.main()