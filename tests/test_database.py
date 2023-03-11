import unittest
import sys
sys.path.append('.')
from support_functions.data_base_functions.data_base import *


class TestDataBase(unittest.TestCase):

    def test_reader_table(self):
        # Teste de time e resultado
        database = r'.\DataBases\dados.db'
        table = 'cargas'
        columns = '*'

        self.assertNotEqual(len(table_reading_support(database, table, columns)),  0)
    
    def test_write_row_table_support(self):
        database = r'.\DataBases\dados.db'
        table = 'test'
        columns = 'item, item2'
        data = '"test", "ok"'

        self.assertEqual(write_row_table_support(database, table, columns, data), True)
        data = '"ok", "ok"'
        condition = [['item', '"test"']]
        self.assertEqual(write_row_table_support(database, table, columns, data, condition), True)

    def test_delete_table_row(self):
        # Teste de time e resultado
        database = r'.\DataBases\dados.db'
        table = 'test'
        conditions = [['item', '"ok"']]

        self.assertEqual(delete_table_row_support(database, table, conditions),  True)
    
    def test_word_crypter(self):
        word = r'oadsfaosdlca,´pásl´dwqopszlkaos´sd´qwokie!@#$%¨&*()_+12315849788971234567890-=§ªº[]{}~^<>'
        encrypted_word = r'851867922918859267476418,´66á9247´678697856692874710188592´9267´978685102628!@#$%¨&*()_+AaBACdbEDddEDAaBbCcDdEI-=§ªº[]{}~^<>'
        self.assertEqual(word_crypter(word), encrypted_word)

    def test_word_decryptor(self):
        word = r'oadsfaosdlca,´pásl´dwqopszlkaos´sd´qwokie!@#$%¨&*()_+12315849788971234567890-=§ªº[]{}~^<>'
        encrypted_word = r'851867922918859267476418,´66á9247´678697856692874710188592´9267´978685102628!@#$%¨&*()_+AaBACdbEDddEDAaBbCcDdEI-=§ªº[]{}~^<>'
        self.assertEqual(word_decryptor(encrypted_word), word)
    
    def test_decrypt_list_of_lists(self):
        encrypted_list = [['1814646728', '1010104010401040'], ['18146467671892671828', '18181818']]
        self.assertEqual(decrypt_list_of_lists(encrypted_list), [['abcde', 'kkkjkjkj'], ['abcddasdae', 'aaaa']])
        
if __name__ == '__main__':
    unittest.main()
