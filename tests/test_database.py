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
        
if __name__ == '__main__':
    unittest.main()
