# Import the PyQty5 modules
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox, QApplication


class MortgageCalculator(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(450, 375))  # set the size of the window
        self.setWindowTitle("Mortgage Calculator")

        # create the labels
        head = QLabel("Peter's Mortgage Calculator", self)
        head.setGeometry(100, 25, 330, 50)
        homeCostLabel = QLabel(self)
        homeCostLabel.setText("Home Cost: $")  # home cose label
        homeCostLabel.move(30, 80)
        dPayLabel = QLabel("Down payment: $", self)
        dPayLabel.move(30, 130)
        dPayLabel.resize(200, 25)
        rateLabel = QLabel("Interest rate: %", self)
        rateLabel.move(30, 180)
        rateLabel.resize(200, 25)
        yearsLabel = QLabel("Years on loan: ", self)
        yearsLabel.move(30, 230)
        yearsLabel.resize(200, 25)

        # create the text box that allows for user input
        self.homeCostInput = QLineEdit(self)
        self.homeCostInput.move(160, 80)
        self.dPayInput = QLineEdit(self)
        self.dPayInput.move(160, 130)
        self.rateInput = QLineEdit(self)
        self.rateInput.move(160, 180)
        self.yearsInput = QLineEdit(self)
        self.yearsInput.move(160, 230)

        # Creates the label to show borrowed amount and amount you pay per month
        loanLabel = QLabel("Loan amount:", self)
        loanLabel.move(270, 75)
        loanLabel.resize(200, 25)
        monthlyPaymentLabel = QLabel("Monthly Amount:", self)
        monthlyPaymentLabel.move(270, 175)
        monthlyPaymentLabel.resize(200, 25)

        # Stores the actual amount you need to borrow
        self.loanAmountLabel = QLabel(self)
        self.loanAmountLabel.setText("0")
        self.loanAmountLabel.move(270, 125)

        # Where the monthly payment will be printed
        self.monthlyPaymentOutput = QLabel(self)
        self.monthlyPaymentOutput.setText("0")
        self.monthlyPaymentOutput.move(270, 225)

        # change the font for the labels
        headFont = QFont('Arial', 16)
        headFont.setBold(True)
        head.setFont(headFont)
        labelFont = QFont('Arial', 12)
        homeCostLabel.setFont(labelFont)
        dPayLabel.setFont(labelFont)
        rateLabel.setFont(labelFont)
        yearsLabel.setFont(labelFont)
        loanLabel.setFont(labelFont)
        monthlyPaymentLabel.setFont(labelFont)
        self.homeCostInput.setFont(labelFont)
        self.dPayInput.setFont(labelFont)
        self.rateInput.setFont(labelFont)
        self.yearsInput.setFont(labelFont)
        self.loanAmountLabel.setFont(labelFont)
        self.monthlyPaymentOutput.setFont(labelFont)

        # create the buttons to do the calculations
        calcBut = QPushButton("Calculate", self)
        calcBut.clicked.connect(self.calc)  # calls the calc function to do the calculations
        calcBut.move(30, 280)

        # create a clear button
        clearBtn = QPushButton("Clear", self)
        clearBtn.clicked.connect(self.clearScreen)
        clearBtn.move(160, 280)

        # set the fonts for the buttons
        btnBold = QFont('Arial', 14)
        btnBold.setBold(True)
        calcBut.setFont(btnBold)
        clearBtn.setFont(btnBold)

    # Do the calculations to find how much you pay per month
    def calc(self):
        # check for errors that can occur during data input
        try:
            # Cast the input into numbers that can
            # be used to perform calculations
            homeCost = int(self.homeCostInput.text())
            downPay = int(self.dPayInput.text())
            rate = float(self.rateInput.text())
            years = int(self.yearsInput.text())
            # Do the math to find monthly interest rate,
            # length of the loan in months,
            # loan after downpayment,
            # and monthly payment
            monthlyRate = rate / 12 / 100
            lengthOfLoan = years * 12
            loanAmount = homeCost - downPay
            monthlyPayment = loanAmount * monthlyRate * ((1 + monthlyRate) ** lengthOfLoan) / (
                    (1 + monthlyRate) ** lengthOfLoan - 1)
            # set labels for loanAmountLabel and monthlyPaymentOutput to loanAmount and monthlyPayment
            self.loanAmountLabel.setText(f"${format(loanAmount, '.2f')}")
            self.monthlyPaymentOutput.setText(f"${format(monthlyPayment, '.2f')}")
        except ZeroDivisionError:
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setInformativeText("You are trying to divide by zero")
            message.exec_()
        except TypeError:
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setInformativeText("The data didn't convert properly")
            message.exec_()
        except ValueError:
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setInformativeText("You didn't enter the right data")
            message.exec_()

    def clearScreen(self):
        self.yearsInput.setText(" ")
        self.rateInput.setText(" ")
        self.homeCostInput.setText(" ")
        self.dPayInput.setText(" ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MortgageCalculator()
    window.show()
    sys.exit(app.exec_())
