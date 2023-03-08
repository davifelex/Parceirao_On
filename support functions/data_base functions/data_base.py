from sqlite3 import *


class DataBase:
    def __init__(self, name = "System.db") -> None:
        self.name = name
    # -------------------------{Funções core}-------------------------
    def conecta(self):
        self.connection = connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except Exception:
            pass