from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
QApplication,
QWidget, QRadioButton, 
QLabel,
QVBoxLayout, 
QHBoxLayout, 
QMessageBox,
QGroupBox,
QPushButton,
QButtonGroup,
)

class Question:
    def __init__(
        self,
        question,
        right_answer,
        wrongl,
        wrong2,
        wrong3
    ):

        self.question = question
        self.right_answer = right_answer
        self.wrongl = wrongl
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
q1 = Question(
    "Государственный язык России?",
    "Русский",
    "Английский", "Испанский", "Азербайжанский")
question_list.append(q1)
q2 = Question(
    "Сколько градусов в прямом углу?",
    "90",
    "20", "60", "40")
question_list.append(q2)

q3 = Question(
    "Кто написал 'к Чадаеву'?",
    "Пушкин",
    "Есенин", "Лермонтов", "Державин")
question_list.append(q3)

q4 = Question(
    "Где создали балет?",
    "Франция",
    "Англия", "Испания", "Китай")
question_list.append(q4)

q5 = Question(
    "В каком году была варфоломеевская ночь?",
    "1572",
    "1588", "1456", "2000")
question_list.append(q5)

app = QApplication([])

ans_layout1 = QHBoxLayout()
ans_layout2 = QVBoxLayout()
ans_layout3 = QVBoxLayout()


push_bautton = QPushButton("Ответить")

question_label = QLabel('В каком году канал получил "золотую кнопку" от YouTube?')
lb_Result = QLabel("Прав ты или нет?")
lb_Correct = QLabel("Тут ответ")
AnsGroupBox = QGroupBox("Результат теста")
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

r_btn1 = QRadioButton('Вариант 1')
r_btn2 = QRadioButton('Вариант 2')
r_btn3 = QRadioButton('Вариант 3')
r_btn4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(r_btn1)
RadioGroup.addButton(r_btn2)
RadioGroup.addButton(r_btn3)
RadioGroup.addButton(r_btn4)

ans_layout2.addWidget(r_btn1)
ans_layout2.addWidget(r_btn2)

ans_layout3.addWidget(r_btn3)
ans_layout3.addWidget(r_btn4)

ans_layout1.addLayout(ans_layout2)
ans_layout1.addLayout(ans_layout3)

RadioGroupBox = QGroupBox("Варианты ответов")
RadioGroupBox.setLayout(ans_layout1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question_label, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(push_bautton, stretch=2)
layout_line3.addStretch(1)

main_layout = QVBoxLayout()
main_layout.addLayout(layout_line1, stretch=2)
main_layout.addStretch(100)
main_layout.addLayout(layout_line2, stretch=8)
main_layout.addStretch(100)
main_layout.addLayout(layout_line3, stretch=1)
main_layout.addStretch(100)

main_widget = QWidget()
main_widget.setLayout(main_layout)
main_widget.show()
main_widget.total = 0
main_widget.score = 0
main_widget.cur_question = 0

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    push_bautton.setText("Ответить")
    RadioGroup.setExclusive(False)
    r_btn1.setChecked(False)
    r_btn2.setChecked(False)
    r_btn3.setChecked(False)
    r_btn4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    push_bautton.setText("Следующий вопрос")

answer = [r_btn1, r_btn2, r_btn3, r_btn4]
def ask(q):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrongl)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    question_label.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно')
        main_widget.score += 1
        print('Статистика\n Всего вопросов правильно:', main_widget.total)
        print('Всего правильных ответов:', main_widget.score)
        print('Рейтинг:', main_widget.score/main_widget.total *100, '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Не правильно')
            print('Рейтинг:', main_widget.score/main_widget.total *100, '%')

def btn_OK():
    if push_bautton.text() == "Ответить":
        check_answer()
    else:
        next_question()

def next_question():
    main_widget.total += 1
    main_widget.cur_question = randint(0, len(question_list) - 1)
    q = question_list[main_widget.cur_question]
    ask(q)

def show_test():
    if push_bautton.text() == "Ответить":
        show_result()
    else:
        show_question()

q = Question('В каком году канал получил "золотую кнопку" от YouTube?', "В 2005", "2010", "2015", "2020")

next_question()

push_bautton.clicked.connect(btn_OK)
app.exec_()
