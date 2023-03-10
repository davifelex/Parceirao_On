import unittest
import sys
sys.path.append('.')
from support_functions.virtual_sever import *


class TestVirtualSever(unittest.TestCase):
    def test_request_task(self):
        database = r"DataBase_Virtual_sever\virtual_sever.db"
        user = 'Tester1'
        table = 'test'
        data = ['asdaasad', 'asdadasda']
        columns = 'item, item2'
        type_task = 'insert'
        conditions = [['abc', 'fff'], ['asas', 'asdad']]
        self.assertEqual(request_task(type_task, database, user, table, data, columns), True)
    
    def test_exit_to_the_sever(self):
        database = r"DataBase_Virtual_sever\virtual_sever.db"
        user = 'Tester1'
        self.assertEqual(exit_to_the_sever(database, user), True)
        

if __name__ == '__main__':
    unittest.main()
