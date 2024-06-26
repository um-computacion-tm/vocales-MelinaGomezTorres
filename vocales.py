import unittest

def contar_vocales(mi_string):
    mi_string = mi_string.lower()  
    vocales = ('a', 'e', 'i', 'o', 'u')
    resultado = {}
    for letra in mi_string:
        if letra in vocales:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    return resultado


class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales('zzz')
        self.assertEqual(resultado, {})

    def test_contar_a(self):
        resultado = contar_vocales('cas')
        self.assertEqual(resultado, {'a': 1})

    def test_contar_aa(self):
        resultado = contar_vocales('casa')
        self.assertEqual(resultado, {'a': 2})

    def test_contar_bese(self):
        resultado = contar_vocales('bese')
        self.assertEqual(resultado, {'e': 2})

    def test_contar_besa(self):
        resultado = contar_vocales('besa')
        self.assertEqual(resultado, {'a': 1, 'e': 1})

    def test_contar_casanova(self):
        resultado = contar_vocales('casanova')
        self.assertEqual(resultado, {'a': 3, 'o': 1})

    def test_contar_aventura(self):
        resultado = contar_vocales('aventura')
        self.assertEqual(resultado, {'a': 2, 'e': 1, 'u': 1}) 

    def test_contar_mUrciElago(self):
        resultado = contar_vocales('mUrciElago')
        self.assertEqual(resultado, {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})

    def test_contar_AErOpUErtO(self):
        resultado = contar_vocales('AErOpUErtO')
        self.assertEqual(resultado, {'a': 1, 'e': 2, 'o': 2, 'u': 1})

    def test_contar_pAraguAs(self):
        resultado = contar_vocales('pAraguAs')
        self.assertEqual(resultado, {'a': 3, 'u': 1})

    def test_contar_ExtranjEro(self):
        resultado = contar_vocales('ExtranjEro')
        self.assertEqual(resultado, {'a': 1, 'e' : 2, 'o': 1})  

    def test_contar_pOEmA(self):
        resultado = contar_vocales('pOEma')
        self.assertEqual(resultado, {'a': 1, 'e': 1, 'o': 1}) 



unittest.main()