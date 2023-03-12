from datetime import *
import sys
sys.path.append('.')
from data_base_functions.data_base import *

def request_task(type_task, database, user, table, data, columns, conditions=None, cryptography=True):
    if not conditions:
        conditions = []
    request_config = ''
    columns = 'user, data, target_table, type_task, status, date'
    date = datetime.datetime.now()
    date = f'{date}'
    
    if cryptography:
        data = encrypt_list_of_lists([data])
    
    data = data[0]

    i=1
    for item in data:
        if i != len(data):
            request_config += rf'{item}¬¬¬¢¢¢£££'
        else:
            request_config += rf'{item}'
        i += 1

    request_config += rf'/¬/*/§/{columns}/¬/*/§/{conditions}'
    data = rf'''"{user}", "{request_config}", "{table}", "{type_task}", 'pending', "{date}"'''

    status = write_row_table_support(database, user, columns, data)
    if not status:
        crate_request_table(database, user)
        status = write_row_table_support(database, user, columns, data)

if __name__ == '__main__':
    database = r"C:\Users\davif\OneDrive\Área de Trabalho\programas\Parceirão_On\DataBase_Virtual_sever\virtual_sever.db"
    user = 'Tester9'
    table = 'test'
    data = ['asdaasad', 'asdadasda']
    columns = 'item, item2'
    type_task = 'insert'
    conditions = [['abc', 'fff'], ['asas', 'asdad']]

    request_task(type_task, database, user, table, data, columns)
