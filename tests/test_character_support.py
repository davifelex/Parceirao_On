import unittest
import sys
sys.path.append('.')
from support_functions.character_support import *


class TestCharacterSupport(unittest.TestCase):
    def test_cpf_mask(self):
        cpf = '00000000000'
        self.assertEqual(cpf_mask(cpf), '000.000.000-00')
    
    def test_cnpj_mask(self):
        cnpj = '00000000000000'
        self.assertEqual(cnpj_mask(cnpj), '00.000.000/0000-00')
    
    def test_money_mask(self):
        money = 123456789.78
        self.assertEqual(money_mask(money), '123.456.789,78')
    
    def test_thousand_mask(self):
        number = 123456789.7894
        self.assertEqual(thousand_mask(number), '123.456.789,7894')
    
    def test_number_input_mask(self):
        number = '123456,451'
        self.assertEqual(number_input_mask(number), '123456.451')
    
    def test_str_input_mask(self):
        word = 'asdsadadasdadas\nasdasd\asda\\\sdasd'
        self.assertEqual(str_input_mask(word), u'asdsadadasdadas\nasdasd\asda\\\sdasd')
 
if __name__ == '__main__':
    unittest.main()