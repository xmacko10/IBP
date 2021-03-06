

from PyQt5 import QtWidgets, QtCore, Qt
import global_variables
import ovirtsdk4 as sdk


class InputDialog(QtWidgets.QWidget):

    def __init__(self):
        super(InputDialog, self).__init__()
        self.connection = None

        self.initUI()

    def initUI(self):
        self.resize(700, 100)
        self.setWindowTitle('Input')

        if global_variables.USER_LOGIN:
            self.username_input = QtWidgets.QLineEdit(
                global_variables.USER_LOGIN, self
            )
            self.url_input = QtWidgets.QLineEdit(
                global_variables.FQDN, self
            )
        else:
            self.username_input = QtWidgets.QLineEdit(self)
            self.url_input = QtWidgets.QLineEdit(self)

        self.username_input.setPlaceholderText('username')
        self.username_input.returnPressed.connect(self.ok_btn_clicked)
        self.password_input = QtWidgets.QLineEdit(self)

        self.password_input.setPlaceholderText('password')
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.returnPressed.connect(self.ok_btn_clicked)

        self.url_input.setPlaceholderText('url')
        self.url_input.returnPressed.connect(self.ok_btn_clicked)

        self.layout_inputs = QtWidgets.QVBoxLayout(self)
        self.layout_inputs.addWidget(self.username_input)
        self.layout_inputs.addWidget(self.password_input)
        self.layout_inputs.addWidget(self.url_input)

        self.layout_buttons = QtWidgets.QHBoxLayout()

        self.ok_btn = QtWidgets.QPushButton('ok', self)
        self.ok_btn.clicked.connect(self.ok_btn_clicked)
        self.cancel_btn = QtWidgets.QPushButton('cancel', self)
        self.cancel_btn.clicked.connect(self.cancel_btn_clicked)

        self.layout_buttons.addWidget(self.ok_btn)
        self.layout_buttons.addWidget(self.cancel_btn)

        self.layout_inputs.addLayout(self.layout_buttons)

        self.show()

        while not self.connection:
            QtCore.QCoreApplication.processEvents()

        self.ok_btn.setDisabled(True)
        self.cancel_btn.setDisabled(True)

    def ok_btn_clicked(self):
        username = self.username_input.text()
        password = self.password_input.text()
        url = self.url_input.text()

        if '@' not in username:
            username += '@internal'

        if url[:8] != 'https://':
            url = 'https://' + url

        if url[-17:] != '/ovirt-engine/api':
            url += '/ovirt-engine/api'

        connection = sdk.Connection(
            username=username, password=password, insecure=True, url=url
        )
        if connection.test(raise_exception=False):
            self.connection = connection
        else:
            message_box = QtWidgets.QMessageBox(self)
            message_box.setWindowTitle('Connection Error')
            message_box.setText('Wrong credentials')
            message_box.setStandardButtons(Qt.QMessageBox.Ok)

            message_box.open()

        global_variables.USER_LOGIN = self.username_input.text()
        global_variables.FQDN = self.url_input.text()


    def cancel_btn_clicked(self, clicked):
        exit(0)

    def get_connection(self):
        return self.connection

    def closeEvent(self, QCloseEvent):
        exit(0)
