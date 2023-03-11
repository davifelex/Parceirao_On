from sqlite3 import *
import math
from threading import Thread
import sys
sys.path.append('.')
from support_functions.data_base_functions.thread import thread_with_retorn_value



class DataBase:
    def __init__(self, name) -> None:
        self.name = name
    # -------------------------{Funções core}-------------------------
    def conecta(self):
        self.connection = connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except Exception:
            pass

    # -----------------------{Funções de leitura}----------------------
    def reader_table(self, table, columns, conditions=[]):
        sql = f'''SELECT {columns} FROM {table}'''

        if conditions:
                conditional_columns = ''
                conditional_data = ''
                
                for condition in conditions:
                    if len(conditional_columns)>0:
                        conditional_columns += ','
                        conditional_data += ','

                    conditional_columns += str(condition[0])
                    conditional_data += str(condition[1])

                sql += f''' WHERE ({conditional_columns}) = ({conditional_data})'''
        
        cursor = self.connection.cursor()
        cursor.execute(f'{sql};')
        return cursor.fetchall()
    
    # -----------------------{Funções de escrita}----------------------
    def write_row_table(self, table, columns, data, conditions=[]):

        try:
            sql = f'''INSERT INTO {table}({columns}) VALUES({data})'''
            if conditions:
                sql = f'''UPDATE {table} SET ({columns}) = ({data})'''
                conditional_columns = ''
                conditional_data = ''
                
                for condition in conditions:
                    if len(conditional_columns)>0:
                        conditional_columns += ','
                        conditional_data += ','

                    conditional_columns += str(condition[0])
                    conditional_data += str(condition[1])

                sql += f'''WHERE ({conditional_columns}) = ({conditional_data})'''

            cursor = self.connection.cursor()
            cursor.execute(f'{sql};')

        except Exception as e:
            print(f'Data recording error: {e}')
            return False
        else:
            self.connection.commit()
            return True
    
    # -----------------------{Funções de exclusão}----------------------
    def delete_table_row(self, table, conditions):
        try:
            if conditions:
                sql = f'''DELETE FROM {table} '''
                conditional_columns = ''
                conditional_data = ''
                
                for condition in conditions:
                    if len(conditional_columns)>0:
                        conditional_columns += ','
                        conditional_data += ','

                    conditional_columns += str(condition[0])
                    conditional_data += str(condition[1])

                sql += f'''WHERE {conditional_columns} = {conditional_data}'''
            
            cursor = self.connection.cursor()
            cursor.execute(f'{sql};')
            self.connection.commit()

        except Exception as error:
            print(f'error deleting row from database table: {error}')
            return False
        else:
            return True


# -----------------------{Auxiliares de leitura}----------------------
def table_reading_support(database, table, columns, conditions=[]):
    db = DataBase(database)
    db.conecta()
    data = db.reader_table(table, columns, conditions)
    db.close_connection()
    return data

# -----------------------{Auxiliares de escrita}----------------------
def write_row_table_support(database, table, columns, data, conditions=[]):
    db = DataBase(database)
    db.conecta()
    status = db.write_row_table(table, columns, data, conditions)
    db.close_connection()
    return status

# -----------------------{Auxiliares de exclusão}----------------------
def delete_table_row_support(database, table, conditions):
    db = DataBase(database)
    db.conecta()
    status = db.delete_table_row(table, conditions)
    db.close_connection()
    return status

# ---------------------------{Criptografia}----------------------------
def word_crypter(word):
    responce = ''
    pair = 0
    for letter in word:
        pair += 1
        if letter == 'A':
            responce += '30'
        elif letter == 'a':
            responce += '18'
        elif letter == 'B':
            responce += '35'
        elif letter == 'b':
            responce += '14'
        elif letter == 'C':
            responce += '68'
        elif letter == 'c':
            responce += '64'
        elif letter == 'D':
            responce += '70'
        elif letter == 'd':
            responce += '67'
        elif letter == 'E':
            responce += '45'
        elif letter == 'e':
            responce += '28'
        elif letter == 'F':
            responce += '89'
        elif letter == 'f':
            responce += '29'
        elif letter == 'G':
            responce += '12'
        elif letter == 'g':
            responce += '32'
        elif letter == 'H':
            responce += '43'
        elif letter == 'h':
            responce += '36'
        elif letter == 'I':
            responce += '15'
        elif letter == 'i':
            responce += '26'
        elif letter == 'J':
            responce += '20'
        elif letter == 'j':
            responce += '40'
        elif letter == 'K':
            responce += '54'
        elif letter == 'k':
            responce += '10'
        elif letter == 'L':
            responce += '51'
        elif letter == 'l':
            responce += '47'
        elif letter == 'M':
            responce += '52'
        elif letter == 'm':
            responce += '78'
        elif letter == 'N':
            responce += '72'
        elif letter == 'n':
            responce += '75'
        elif letter == 'O':
            responce += '11'
        elif letter == 'o':
            responce += '85'
        elif letter == 'P':
            responce += '33'
        elif letter == 'p':
            responce += '66'
        elif letter == 'Q':
            responce += '44'
        elif letter == 'q':
            responce += '97'
        elif letter == 'R':
            responce += '48'
        elif letter == 'r':
            responce += '96'
        elif letter == 'S':
            responce += '46'
        elif letter == 's':
            responce += '92'
        elif letter == 'T':
            responce += '21'
        elif letter == 't':
            responce += '42'
        elif letter == 'U':
            responce += '23'
        elif letter == 'u':
            responce += '94'
        elif letter == 'V':
            responce += '22'
        elif letter == 'v':
            responce += '91'
        elif letter == 'W':
            responce += '55'
        elif letter == 'w':
            responce += '86'
        elif letter == 'X':
            responce += '88'
        elif letter == 'x':
            responce += '82'
        elif letter == 'Y':
            responce += '99'
        elif letter == 'y':
            responce += '80'
        elif letter == 'Z':
            responce += '74'
        elif letter == 'z':
            responce += '87'
        else:
            # -------{números}--------
            if letter == '1':
                responce += 'A'
            elif letter == '2':
                responce += 'a'
            elif letter == '3':
                responce += 'B'
            elif letter == '4':
                responce += 'b'
            elif letter == '5':
                responce += 'C'
            elif letter == '6':
                responce += 'c'
            elif letter == '7':
                responce += 'D'
            elif letter == '8':
                responce += 'd'
            elif letter == '9':
                responce += 'E'
            elif letter == '0':
                responce += 'I'

            else:
                responce += letter
    return str(responce)

def word_decryptor(wncrypted_word):
    responce = ''
    last = ''
    i = 0
    for letter in wncrypted_word:
        if letter == 'A':
            responce += '1'
        elif letter == 'a':
            responce += '2'
        elif letter == 'B':
            responce += '3'
        elif letter == 'b':
            responce += '4'
        elif letter == 'C':
            responce += '5'
        elif letter == 'c':
            responce += '6'
        elif letter == 'D':
            responce += '7'
        elif letter == 'd':
            responce += '8'
        elif letter == 'E':
            responce += '9'
        elif letter == 'I':
            responce += '0'

        else:
            if letter in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if i == 0:
                    last = letter
                    i += 1
                elif i == 1:
                    d_letter = str(last) + str(letter)
                    i = 0
                    if d_letter == '30':
                        responce += 'A'
                    elif d_letter == '18':
                        responce += 'a'
                    elif d_letter == '35':
                        responce += 'B'
                    elif d_letter == '14':
                        responce += 'b'
                    elif d_letter == '68':
                        responce += 'C'
                    elif d_letter == '64':
                        responce += 'c'
                    elif d_letter == '70':
                        responce += 'D'
                    elif d_letter == '67':
                        responce += 'd'
                    elif d_letter == '45':
                        responce += 'E'
                    elif d_letter == '28':
                        responce += 'e'
                    elif d_letter == '89':
                        responce += 'F'
                    elif d_letter == '29':
                        responce += 'f'
                    elif d_letter == '12':
                        responce += 'G'
                    elif d_letter == '32':
                        responce += 'g'
                    elif d_letter == '43':
                        responce += 'H'
                    elif d_letter == '36':
                        responce += 'h'
                    elif d_letter == '15':
                        responce += 'I'
                    elif d_letter == '26':
                        responce += 'i'
                    elif d_letter == '20':
                        responce += 'J'
                    elif d_letter == '40':
                        responce += 'j'
                    elif d_letter == '54':
                        responce += 'K'
                    elif d_letter == '10':
                        responce += 'k'
                    elif d_letter == '51':
                        responce += 'L'
                    elif d_letter == '47':
                        responce += 'l'
                    elif d_letter == '52':
                        responce += 'M'
                    elif d_letter == '78':
                        responce += 'm'
                    elif d_letter == '72':
                        responce += 'N'
                    elif d_letter == '75':
                        responce += 'n'
                    elif d_letter == '11':
                        responce += 'O'
                    elif d_letter == '85':
                        responce += 'o'
                    elif d_letter == '33':
                        responce += 'P'
                    elif d_letter == '66':
                        responce += 'p'
                    elif d_letter == '44':
                        responce += 'Q'
                    elif d_letter == '97':
                        responce += 'q'
                    elif d_letter == '48':
                        responce += 'R'
                    elif d_letter == '96':
                        responce += 'r'
                    elif d_letter == '46':
                        responce += 'S'
                    elif d_letter == '92':
                        responce += 's'
                    elif d_letter == '21':
                        responce += 'T'
                    elif d_letter == '42':
                        responce += 't'
                    elif d_letter == '23':
                        responce += 'U'
                    elif d_letter == '94':
                        responce += 'u'
                    elif d_letter == '22':
                        responce += 'V'
                    elif d_letter == '91':
                        responce += 'v'
                    elif d_letter == '55':
                        responce += 'W'
                    elif d_letter == '86':
                        responce += 'w'
                    elif d_letter == '88':
                        responce += 'X'
                    elif d_letter == '82':
                        responce += 'x'
                    elif d_letter == '99':
                        responce += 'Y'
                    elif d_letter == '80':
                        responce += 'y'
                    elif d_letter == '74':
                        responce += 'Z'
                    elif d_letter == '87':
                        responce += 'z'

            else:
                responce += letter

    return str(responce)

def decrypt_list_of_lists(list_of_lists):
    responce = []
    for list in list_of_lists:
        temp = []
        for item in list:
            try:
                temp.append(word_decryptor(str(item)))
            except Exception:
                temp.append(str(item))
        responce.append(temp)
    
    return responce

def encrypt_list_of_lists(list_of_lists):
    responce = []

    for list in list_of_lists:
        temp = []
        for item in list:
            try:
                temp.append(word_crypter(str(item)))
            except Exception:
                temp.append(str(item))
        responce.append(temp)
    return responce

def parallel_decrypt_list_of_lists(list_of_lists):
    # theading
    num_tasks = math.floor(len(list_of_lists) / 3)
    task1 = list_of_lists[:num_tasks]
    task2 = list_of_lists[(num_tasks):(num_tasks + num_tasks)]
    task3 = list_of_lists[(num_tasks+num_tasks):]
    responce = []
    # decrypted_list = decrypt_list_of_lists(task1)
    t1 = thread_with_retorn_value(target=decrypt_list_of_lists, args=([task1]))
    t1.start()
    t2 = thread_with_retorn_value(target=decrypt_list_of_lists, args=([task2]))
    t2.start()
    t3 = thread_with_retorn_value(target=decrypt_list_of_lists, args=([task3]))
    t3.start()
    reponce_task1 = t1.join()
    reponce_task2 = t2.join()
    reponce_task3 = t3.join()
    return reponce_task1 + reponce_task2 + reponce_task3

def parallel_encrypt_list_of_lists(list_of_lists):
    # theading
    num_tasks = math.floor(len(list_of_lists) / 3)
    task1 = list_of_lists[:num_tasks]
    task2 = list_of_lists[(num_tasks):(num_tasks + num_tasks)]
    task3 = list_of_lists[(num_tasks+num_tasks):]
    responce = []
    # decrypted_list = decrypt_list_of_lists(task1)
    t1 = thread_with_retorn_value(target=encrypt_list_of_lists, args=([task1]))
    t1.start()
    t2 = thread_with_retorn_value(target=encrypt_list_of_lists, args=([task2]))
    t2.start()
    t3 = thread_with_retorn_value(target=encrypt_list_of_lists, args=([task3]))
    t3.start()
    reponce_task1 = t1.join()
    reponce_task2 = t2.join()
    reponce_task3 = t3.join()
    return reponce_task1 + reponce_task2 + reponce_task3          

if __name__ == '__main__':
    import math
    from time import time
    database = r'C:\Users\davif\PycharmProjects\ParceiraoOnOficial\DataBase_Virtual_Sever\virtual_sever.db'
    table = 'DaviFelexTobias'
    columns = '*'
    time_init = time()
    list = table_reading_support(database, table, columns)
    time_decrypted_parallel = time() - time_init
    print(f'O tempo para ler foi: {time_decrypted_parallel}')

    # encrypted_list = encrypt_list_of_lists(list)
    time_init = time()
    decrypted_list_parallel = parallel_decrypt_list_of_lists(list)
    time_decrypted_parallel = time() - time_init
    print(f'O tempo para descriptar em paralello foi: {time_decrypted_parallel}')
    time_init = time()
    decrypted_list_seq = decrypt_list_of_lists(list)
    time_decrypted_seq = time() - time_init
    print(f'O tempo para descriptar em sequencial foi: {time_decrypted_seq}')
    print(f'Igualdade de dados: {decrypted_list_parallel == decrypted_list_seq}')