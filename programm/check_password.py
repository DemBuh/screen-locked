import sys
from PyQt5 import QtWidgets
from design import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
      
        self.pushButton_12.clicked.connect(self.check_password)

    def check_password(self):
     
        entered_password = self.lineEdit.text()

       
        if entered_password == "222":
             result_message = "Пароль введен верно"
        else:
            result_message = "Неверный пароль"

   
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Результат")
        msg_box.setText(result_message)
        msg_box.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())