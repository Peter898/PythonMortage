from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(504, 427)
        self.downPay = QtWidgets.QTextEdit(Dialog)
        self.downPay.setGeometry(QtCore.QRect(60, 80, 151, 31))
        self.downPay.setObjectName("textEdit")
        self.loan = QtWidgets.QTextEdit(Dialog)
        self.loan.setGeometry(QtCore.QRect(60, 150, 151, 31))
        self.loan.setObjectName("textEdit_2")
        self.years = QtWidgets.QTextEdit(Dialog)
        self.years.setGeometry(QtCore.QRect(60, 220, 151, 31))
        self.years.setObjectName("textEdit_3")
        self.rate = QtWidgets.QTextEdit(Dialog)
        self.rate.setGeometry(QtCore.QRect(60, 290, 151, 31))
        self.rate.setObjectName("textEdit_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 60, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 200, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 270, 101, 16))
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(60, 340, 151, 41))
        self.radioButton.setObjectName("radioButton")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(320, 150, 111, 91))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Mortgage Calculator"))
        self.label.setText(_translate("Dialog", "Down Payment"))
        self.label_2.setText(_translate("Dialog", "Loan"))
        self.label_3.setText(_translate("Dialog", "Years"))
        self.label_4.setText(_translate("Dialog", "Interest"))
        self.radioButton.setText(_translate("Dialog", "Check when finished "))
        self.radioButton.toggled.connect(self.cal)

    def cal(self):
        # annual interest rate
        i = self.label_4.text()
        # checking if fields are empty
        if len(i) == 0 or i == '0':
            return

        y = self.label_3.text()

        # checking if fields are empty
        if len(y) == 0 or y == '0':
            return

        l = self.label_2.text()

        # checking if fields are empty
        if len(l) == 0 or l == '0':
            return

        dp = self.label.text()
        # checking if fields are empty
        if len(dp) == 0 or dp == '0':
            return

        downpayment = self.label.text()
        l = eval(l)
        i = eval(i)
        y = eval(y)

        l = l - dp
        i = (i / 100) / 12
        n = 12 * y
        mortgage = (l * i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)
        self.textBrowser.setText(mortgage)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())