import sys
import os
from qt_core import *
from gui.windows.login_window.ui_log import Ui_Window_login

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_login = Ui_Window_login()
        self.ui_login.setup_ui(self)

        self.show()


if __name__ == '__main__':
    from time import time
    time_init = time()
    app = QApplication(sys.argv)
    window = MainWindow()

    print(f'Codigo finalizado em: {time() - time_init}')
    sys.exit(app.exec())