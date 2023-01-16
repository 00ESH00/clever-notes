from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout

app = QApplication([])
main_window = QWidget()

def plus():
 num1 = First_LineEdit.text()
 num2 = Second_LineEdit.text()
 num1 = float(num1)
 num2 = float(num2)
 result = num1 + num2
 result = str(result)
 Label.setText(result)

def minus():
 num1 = First_LineEdit.text()
 num2 = Second_LineEdit.text()
 num1 = float(num1)
 num2 = float(num2)
 result = num1 - num2
 result = str(result)
 Label.setText(result)

def multiplication():
 num1 = First_LineEdit.text()
 num2 = Second_LineEdit.text()
 num1 = float(num1)
 num2 = float(num2)
 result = num1 * num2
 result = str(result)
 Label.setText(result)

def division():
 num1 = First_LineEdit.text()
 num2 = Second_LineEdit.text()
 num1 = float(num1)
 num2 = float(num2)
 result = num1 / num2
 result = str(result)
 Label.setText(result)

def square():
 num1 = First_LineEdit.text()
 num2 = Second_LineEdit.text()
 num1 = float(num1)
 num2 = float(num2)
 result = num1 ** num2
 result = str(result)
 Label.setText(result)

def remainder():
 num1 = First_LineEdit.text()
 num2 = Second_LineEdit.text()
 num1 = float(num1)
 num2 = float(num2)
 result = num1 // num2
 result = str(result)
 Label.setText(result)




First_LineEdit = QLineEdit()
Second_LineEdit = QLineEdit()
Label = QLabel("Ответик:")
button_note_plus = QPushButton("+")
button_note_minus = QPushButton("-")
button_note_multiply = QPushButton("*")
button_note_divide = QPushButton("/")
button_note_square = QPushButton("**")
button_note_divide_without_remainder = QPushButton("//")

layout_1 = QHBoxLayout()
layout_2 = QHBoxLayout()
layout_3 = QHBoxLayout()
layout_4 = QHBoxLayout()
layout_5 = QHBoxLayout()
main_line = QVBoxLayout()
main_line.addLayout(layout_1)
main_line.addLayout(layout_2)
main_line.addLayout(layout_3)
main_line.addLayout(layout_4)
main_line.addLayout(layout_5)
main_window.setLayout(main_line)
layout_1.addWidget(First_LineEdit, alignment= Qt.AlignCenter)
layout_2.addWidget(Second_LineEdit, alignment= Qt.AlignCenter)
layout_3.addWidget(Label, alignment= Qt.AlignLeft)
layout_4.addWidget(button_note_plus,alignment= Qt.AlignCenter)
layout_4.addWidget(button_note_minus,alignment= Qt.AlignCenter)
layout_4.addWidget(button_note_multiply,alignment= Qt.AlignCenter )
layout_5.addWidget(button_note_divide,alignment= Qt.AlignCenter)
layout_5.addWidget(button_note_square,alignment= Qt.AlignCenter)
layout_5.addWidget(button_note_divide_without_remainder,alignment= Qt.AlignCenter)

button_note_plus.clicked.connect(plus)
button_note_minus.clicked.connect(minus)
button_note_multiply.clicked.connect(multiplication)
button_note_divide.clicked.connect(division)
button_note_square.clicked.connect(square)
button_note_divide_without_remainder.clicked.connect(remainder)


main_window.show()
app.exec_()
