from sqlite3 import *


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

            print(f'{sql};')
        except Exception as e:
            print(f'{sql};')
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
            print(f'{sql};')

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

if __name__ == '__main__':
    database = r'.\DataBases\dados.db'
    table = 'test'
    conditions = [['item', '"ok"']]

    delete_table_row_support(database, table, conditions)