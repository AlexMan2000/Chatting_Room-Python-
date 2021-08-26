import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import db_mysql
import chat.index as chat
import gol

name = ""
gol._init()


class logindialog(QDialog):
    global name

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.setWindowTitle('login windows')
        self.resize(200, 200)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.frame = QFrame(self)
        self.verticalLayout = QVBoxLayout(self.frame)

        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("account")
        self.verticalLayout.addWidget(self.lineEdit_account)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("password")
        self.verticalLayout.addWidget(self.lineEdit_password)

        self.pushButton_enter = QPushButton()
        self.pushButton_enter.setText("login")
        self.verticalLayout.addWidget(self.pushButton_enter)

        self.pushButton_quit = QPushButton()
        self.pushButton_quit.setText("cancel")
        self.verticalLayout.addWidget(self.pushButton_quit)

        ###### 绑定按钮事件
        self.pushButton_enter.clicked.connect(self.on_pushButton_enter_clicked)
        self.pushButton_quit.clicked.connect(QCoreApplication.instance().quit)


    def on_pushButton_enter_clicked(self):
        global name
        db = db_mysql.db1()
        sql = "select password from user where account = %s"
        password = db_mysql.safe_runsql_json(db, sql, self.lineEdit_account.text())
        if len(password) == 0:
            QMessageBox.question(self, "", "you account no exist", QMessageBox.Yes)
        elif password[0]['password'] == self.lineEdit_password.text():
            # 通过验证，关闭对话框并返回1
            name = self.lineEdit_account.text()
            self.accept()

        else:
            QMessageBox.question(self, "", "password error", QMessageBox.Yes)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = logindialog()
    if dialog.exec_() == QDialog.Accepted:
        home_page = QWidget()
        home = chat.Ui_Form()
        home.setupUi(home_page)
        home.UserId.setText(name)
        home_page.show()
    sys.exit(app.exec_())
