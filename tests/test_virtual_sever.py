import unittest
import sys
sys.path.append('.')
from support_functions.virtual_sever import *


class TestVirtualSever(unittest.TestCase):
    def test_request_task(self):
        database = r"DataBase_Virtual_sever\virtual_sever.db"
        user = 'Tester12'
        table = 'test'
        data = ['asdaasad', 'asdadasda']
        columns = 'item, item2'
        type_task = 'insert'
        conditions = [['abc', 'fff'], ['asas', 'asdad']]
        self.assertEqual(request_task(type_task, database, user, table, data, columns), True)
    pass
if __name__ == '__main__':
    unittest.main()
