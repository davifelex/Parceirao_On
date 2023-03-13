import sys
sys.path.append('.')
from support_functions.data_base_functions.data_base import *
from time import time
import random
from datetime import datetime

def request_task(type_task, database, user, table, data, columns, conditions=None, cryptography=True):
    try:
        if not conditions:
            conditions = []
        request_config = ''
        columns = 'user, data, target_table, type_task, status, date'
        date = datetime.now()
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
    except Exception as error:
        print(f'Error when trying to send request: {error}')
        return False
    else:
        return True

def exit_to_the_sever(virtual_database, user):
        try:
            write_row_table_support(virtual_database, 'controller', 'status', '0', [['user', f'"{user}"']])
        except Exception as error:
            print(f'Error in exit sever: {error}')
            return False
        else:
            return True
class Virtual_Sever:
    def __init__(self, user, virtual_sever_database, database):
        # -------------------------------{Defining Paths}-------------------------------
        self.virtual_database = virtual_sever_database + '/virtual_sever.db'
        self.main_database = database
        # -----------------------------{Starting Variables}-----------------------------
        self.user_log = user

        # ---------------------------------{Start Sever}--------------------------------
        login = False
        while login == False:
            login = self.login_to_the_sever()
        
        self.working = True
        while self.working == True:
            self.working = self.check_status()
        
        self.generate_hierarchy('complete')

    # ---------------------------------{Core functions}---------------------------------
    def generate_hierarchy(self, type_task='complete'):
        users = table_reading_support(self.virtual_database, 'controller', 'user, office', [['status', '"1"']])
        manager = random.choice(users)

        if type_task == 'reset':
            write_row_table_support(self.virtual_database, 'controller', 'office', '"manager"', [['user', f'"{manager[0]}"']])
            for user in users:
                if not user == manager:
                    write_row_table_support(self.virtual_database, 'controller', 'office', '"worker"', [['user', f'"{user[0]}"']])
        
        elif type_task == 'complete':
            for user in users:
                if not user[1]:
                    write_row_table_support(self.virtual_database, 'controller', 'office', '"worker"', [['user', f'"{user[0]}"']])


        

    def login_to_the_sever(self):
        time_log = time()
        log = rf'"{user}", 1, "{time_log}"'
        
        test_log = self.check_status()
        try:
            if test_log == 'not_log':
                write_row_table_support(self.virtual_database, 'controller', 'user, status, time',
                                        log)
            if test_log == False:
                write_row_table_support(self.virtual_database, 'controller', 'user, status, time',
                                        log, [['user', f'"{self.user_log}"']])
        except Exception as error:
            print(f'Error when trying to join the server: {error}')
            return False
        else:
            return True
    
    def check_status(self):
        try:
            status = table_reading_support(self.virtual_database, 'controller', 'status', [['user', f'"{self.user_log}"']])[0][0]
            if status == '1':
                status = True
            else:
                status = False
        except Exception as error:
            status = 'not_log'
        return status

if __name__ == '__main__':
    user = 'Tester1'
    database = r'C:\Users\davif\OneDrive\Área de Trabalho\programas\Parceirão_On\DataBases'
    database_virtual = r'C:\Users\davif\OneDrive\Área de Trabalho\programas\Parceirão_On\DataBase_Virtual_sever'
    Virtual_Sever(user, database_virtual, database)
