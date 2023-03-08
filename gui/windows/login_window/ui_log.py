from qt_core import *

class Ui_Window_login(object):
    def setup_ui(self, parent):
        # -----------------{Set caracteristcs}-----------------
        if not parent.objectName():
            parent.setObjectName("WindowLogin")
        parent.resize(600, 400)
        parent.setWindowTitle('Parceirão On Login')
        icon = QIcon()
        icon.addFile("graphic dependencies\window_icon.png")
        parent.setWindowIcon(icon)
        parent.setWindowFlags(Qt.FramelessWindowHint)
        parent.setAttribute(Qt.WA_TranslucentBackground)
        parent.setStyleSheet("border-radius:10px;")

        # ---------------{create central Widget}---------------
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color:#dfe3ed")
        parent.setCentralWidget(self.central_frame)

        # create layout
        self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        # CREATE HEADER
        self.header_frame = QFrame()
        self.header_frame.setStyleSheet("background-color:#05071a;border-radius:5px;")
        self.header_frame.setMaximumHeight(65)
        h_layout_header = QHBoxLayout(self.header_frame)

        logo = QLabel()
        logo.setPixmap(QPixmap(u"graphic dependencies\parceirao_icon.png"))
        logo.setMaximumSize(200,40)
        logo.setScaledContents(True)
        logo.setMargin(-26)

        spacer = QSpacerItem(4,5,QSizePolicy.Expanding)

        title = QLabel()
        title.setText("LOGIN")
        title.setStyleSheet('color:white;border-bottom: 2px solid;border-color:rgb(255, 95, 4);border-radius:0px;')
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        title.setFont(font)
        title.setMinimumWidth(70)
        title.setAlignment(Qt.AlignCenter)

        h_layout_header.addWidget(logo)
        h_layout_header.addItem(spacer)
        h_layout_header.addWidget(title)
        
        
        # CREATE BODY
        self.body_frame = QFrame()
        self.body_frame.setStyleSheet("background-color:#dfe3ed")
        v_layout_body = QVBoxLayout(self.body_frame)

        # title_ apresent
        apresent_text = QLabel()
        apresent_text.setText(QCoreApplication.translate("Form",
                                                u"<html><head/><body><p><span style=\" font-size:18pt; "
                                                u"font-weight:700; color:#a0aac0;\">Bem vindo </span><span "
                                                u"style=\" font-size:18pt; font-weight:700; "
                                                u"color:#20173a;\">de volta!</span></p></body></html>",
                                                None))
        apresent_text.setMaximumSize(300, 30)
        h_spacer = QSpacerItem(25, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        h_layout = QHBoxLayout()
        h_layout.addItem(h_spacer)
        h_layout.addWidget(apresent_text)
        h_layout.addItem(h_spacer)

        # Create input user
        frame_inputs = QFrame()

        inputs_layout = QVBoxLayout(frame_inputs)

        txt_user = QLineEdit()
        txt_user.setStyleSheet('background-color:white;border:1px solid;border-color: silver;border-radius:5px')
        txt_user.setMinimumSize(300,40)
        txt_user.setPlaceholderText('Usuario')
        txt_user.setAlignment(Qt.AlignCenter)
        txt_password = QLineEdit()
        txt_password.setStyleSheet('background-color:white;border:1px solid;border-color: silver;border-radius:5px')
        txt_password.setMinimumSize(300,40)
        txt_password.setPlaceholderText('Senha')
        txt_password.setEchoMode(QLineEdit.Password)
        txt_password.setAlignment(Qt.AlignCenter)

        self.btg_login = QPushButton()
        self.btg_login.setStyleSheet(u"background-color: rgb(255, 95, 4);\n"
                                      "border: none;\n"
                                      "border-radius:10px;\n"
                                      "color: rgb(255, 255, 255);")
        self.btg_login.setText('Entrar')
        self.btg_login.setMinimumSize(QSize(200, 36))
        self.btg_login.setMaximumSize(QSize(200, 36))
        self.btg_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btg_login.setObjectName('btg_login')

        layout_btg = QHBoxLayout()
        layout_btg.addItem(h_spacer)
        layout_btg.addWidget(self.btg_login)
        layout_btg.addItem(h_spacer)

        inputs_layout.addWidget(txt_user)
        inputs_layout.addWidget(txt_password)
        inputs_layout.addLayout(layout_btg)

        layout_center = QHBoxLayout()
        layout_center.addItem(h_spacer)
        layout_center.addWidget(frame_inputs)
        layout_center.addItem(h_spacer)



        v_layout_body.addLayout(h_layout)
        v_layout_body.addLayout(layout_center)



        # ADD WIDGETS TO APP
        self.main_layout.addWidget(self.header_frame)
        self.main_layout.addWidget(self.body_frame)
