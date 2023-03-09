import unittest
import importlib.util

spec = importlib.util.spec_from_file_location("data_base", "support_functions\data_base_functions\data_base.py")
data_base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(data_base)

class TestDataBase(unittest.TestCase):
    def test_reader_table(self):
        # Teste de time e resultado
        database = r'.\DataBases\dados.db'
        table = 'cargas'
        columns = '*'

        self.assertEqual(len(data_base.table_reading_support(database, table, columns)),  0)

if __name__ == '__main__':
    unittest.main()
