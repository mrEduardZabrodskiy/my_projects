from tkinter import *
from random import randint
import datetime
import time
import pyautogui
#import json

root = Tk()
root.title("Numbers")


class Line:

    def __init__(self, root):
        self.frame = LabelFrame(root, text="")
        self.entry = Entry(self.frame)
        self.label = Label(self.frame, text="   :   ")
        self.num = num

    def create_line(self):
        global count_line
        frame = self.frame
        entry = self.entry
        label = self.label
        frame.pack(padx=10, pady=3, ipady=3)
        entry.pack(side=LEFT, padx=3, pady=3)
        label.pack(side=LEFT, padx=3, pady=3)
        entry.bind('<Return>', self.read_line)
        count_line += 1

    def read_line(self, event):
        global count_line, count_step, start_time
        if status_game:
            num = self.num
            value = self.entry.get()
            in_num = 0
            loc_num = 0
            error_line['text'] = ''
            error_line['bg'] = '#F0F0F0'
            while True:
                if not value.isdigit or len(str(value)) != 4:
                    error_line['text'] = "Please enter a FOUR digit number"
                    error_line['bg'] = '#ffaaaa'
                    break
                elif len(set(str(value))) != 4:
                    error_line['text'] = "You cannot repeat numbers."
                    error_line['bg'] = '#ffaaaa'
                    break
                elif count_line == 14:
                    error_line['text'] = f"Are you still playing? \n Just enter {num} and win. "
                    error_line['bg'] = '#ffaaaa'
                    count_step += 1
                    new_line()
                    break
                elif len(value) == 4:
                    for i in value:
                        if i in str(num):
                            in_num += 1
                            if value.find(str(i)) == num.find(str(i)):
                                loc_num += 1
                    if str(value) == str(num):
                        if count_step == 0:
                            start_time = datetime.datetime.now()
                            count_step += 1
                            self.label['text'] = f" {in_num}:{loc_num} "
                            self.wonLabel()
                            break
                        else:
                            count_step += 1
                            self.label['text'] = f" {in_num}:{loc_num} "
                            self.wonLabel()
                            break
                    else:
                        if count_step == 0:
                            start_time = datetime.datetime.now()
                            count_step += 1
                            self.label['text'] = f" {in_num}:{loc_num} "
                            focus()
                            break
                        else:
                            count_step += 1
                            self.label['text'] = f" {in_num}:{loc_num} "
                            if count_step == count_line:
                                new_line()
                            focus()
                            break
                focus()

    def wonLabel(self):
        global count_step, count_finish_label, status_game, button_frame, restart_button, save_button, won_label, game_time
        if count_finish_label == 0:
            finish_time = datetime.datetime.now()
            game_time = finish_time - start_time
            if language_button['text'] == 'en':
                if count_step == 1:
                    won_label = Label(text=f" Вы выиграли \n {count_step} шаг   {game_time}")
                elif count_step in (2, 3, 4):
                    won_label = Label(text=f" Вы выиграли \n {count_step} шагa   {game_time}")
                else:
                    won_label = Label(text=f" Вы выиграли\n {count_step} шагов   {game_time}")
            else:
                if count_step == 1:
                    won_label = Label(text=f" You WIN\n {count_step} step   {game_time}")
                else:
                    won_label = Label(text=f" You WIN\n {count_step} steps   {game_time}")
            won_label.pack()
            button_frame = Frame(root)
            if language_button['text'] == 'en':
                save_button = Button(button_frame, text="Сохранить", width=9)
                restart_button = Button(button_frame, text="Заново", width=9)
            else:
                save_button = Button(button_frame, text="Save", width=9)
                restart_button = Button(button_frame, text="Restart", width=9)
            button_frame.pack(ipady=10)
            save_button.pack(side=LEFT, padx=10)
            save_button.bind("<Button-1>", save_result)
            restart_button.pack(side=RIGHT, padx=10)
            restart_button.bind("<Button-1>", restart)
            count_finish_label += 1
            status_game = False

    def del_line(self):
        self.frame.destroy()
        self.label.destroy()
        self.entry.destroy()
        button_frame.destroy()
        save_button.destroy()
        restart_button.destroy()
        won_label.destroy()


# functions

def random_number():
    """the function does create a random four digit number without repetition"""
    while True:
        number = ''
        stupid_number = ['1234', '5678', '2345', '3456', '4567', '6789', '1256', '3478', '1278', '3478', '1289']
        while len(number) < 4:
            a = randint(0, 9)
            if str(a) not in number:
                number += str(a)
            if number in stupid_number:
                break
        return number


def info_button_canvas(event):
    """the function shows game information and instructions"""
    global text
    if info_button['text'] == 'Close info' or info_button['text'] == 'Закрыть':
        text.destroy()
        info_canvas.config(width=0)
        if info_button['text'] == 'Close info':
            info_button["text"] = 'Open info'
        else:
            info_button["text"] = 'Открыть'
    elif info_button['text'] == 'Open info' or info_button['text'] == 'Открыть':
        text = Text(info_canvas, width=40, height=10, wrap=WORD, bg='#F0F0F0', bd=0)
        text.delete(1.0, END)
        text.insert(1.0, game_info)
        text.pack(side=TOP, padx=30)
        info_canvas.config(width=300)
        if info_button['text'] == 'Open info':
            info_button["text"] = 'Close info'
        else:
            info_button["text"] = 'Закрыть'


def new_line():
    """the function creates new line every time after reading the number you entered"""
    global l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, num
    if count_line < 4:
        #num = random_number()  # random number which you have to guess
        Label(text=num).pack()
        l1 = Line(root); l1.create_line(); l1.entry.focus_set()
        l2 = Line(root); l2.create_line()
        l3 = Line(root); l3.create_line()
        l4 = Line(root); l4.create_line()
    elif count_line == 4: l5 = Line(root); l5.create_line()
    elif count_line == 5: l6 = Line(root); l6.create_line()
    elif count_line == 6: l7 = Line(root); l7.create_line()
    elif count_line == 7: l8 = Line(root); l8.create_line()
    elif count_line == 8: l9 = Line(root); l9.create_line()
    elif count_line == 9: l10 = Line(root); l10.create_line()
    elif count_line == 10: l11 = Line(root); l11.create_line()
    elif count_line == 11: l12 = Line(root); l12.create_line()
    elif count_line == 12: l13 = Line(root); l13.create_line()
    elif count_line == 13: l14 = Line(root); l14.create_line()
    elif count_line == 14: l15 = Line(root); l15.create_line()


def change_language(event):
    global game_info, save_button, won_label, count_step, game_time, won_label
    if language_button['text'] == 'english':
        language_button['text'] = 'русский'
        game_info = game_info_en
        if info_button['text'] == 'Close info' or info_button['text'] == 'Закрыть':
            text.delete(1.0, END)
            text.insert(1.0, game_info_en)
        if info_button['text'] == 'Закрыть':
            info_button['text'] = 'Close info'
        elif info_button['text'] == 'Открыть':
            info_button['text'] = 'Open info'
        try:
            save_button['text'] = 'Save'
            restart_button['text'] = 'Restart'
            if count_step == 1:
                won_label['text'] = "You WIN\n {0} step {1}".format(count_step, game_time)
            else:
                won_label['text'] = "You WIN\n" + str(count_step) + " steps " + str(game_time)
        except (IndentationError, NameError): pass

    else:
        language_button['text'] = 'english'
        game_info = game_info_ru
        if info_button['text'] == 'Close info' or info_button['text'] == 'Закрыть':
            text.delete(1.0, END)
            text.insert(1.0, game_info_ru)
        if info_button['text'] == 'Open info':
            info_button['text'] = 'Открыть'
        elif info_button['text'] == 'Close info':
            info_button['text'] = 'Закрыть'
        try:
            save_button['text'] = 'Сохранить'
            restart_button['text'] = 'Заново'
            if count_step == 1:
                won_label['text'] = "Вы выиграли\n" + str(count_step) + " шаг " + str(game_time)
            elif count_step in (2, 3, 4):
                won_label['text'] = "Вы выиграли\n" + str(count_step) + " шагa " + str(game_time)
            else:
                won_label['text'] = "Вы выиграли\n" + str(count_step) + " шагов " + str(game_time)
        except (IndentationError, NameError): pass


def restart(event):
    global count_step, count_line, status_game, count_finish_label, count_save_canvas
    eval_list = ['l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9', 'l10', 'l11', 'l12', 'l13', 'l14', 'l15']
    if count_line < 5:
        for i in (l1, l2, l3, l4): i.del_line()
        count_line, count_step, count_finish_label, status_game = 0, 0, 0, TRUE
        new_line()
        count_save_canvas = 0
    else:
        for i in eval_list[:count_line]: eval(i).del_line()
        count_line, count_step, count_finish_label, status_game = 0, 0, 0, TRUE
        new_line()
        count_save_canvas = 0


def focus():
    lines_list = ['l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9', 'l10', 'l11', 'l12', 'l13', 'l14', 'l15']
    eval(lines_list[count_step]).entry.focus_set()


def save_result(event):
    global name_entry, save_root, count_save_canvas
    if count_save_canvas == 0:
        save_root = Tk()
        save_canvas = Canvas(save_root, height=200, width=500)
        save_canvas.pack()
        save_frame = Frame(save_canvas, padx=15, pady=15)
        if language_button['text'] == 'english':
            save_label = Label(save_frame, text='Введите ваше имя')
        else:
            save_label = Label(save_frame,  text='Enter your name')
        save_button = Button(save_frame, text='OK', width=8)
        name_entry = Entry(save_frame, width=20)
        save_label.pack(side=LEFT)
        name_entry.pack(side=LEFT, padx=10)
        save_button.pack(side=LEFT)
        save_frame.pack()
        name_entry.bind('<Return>', get_name)
        save_button.bind("<Button-1>", get_name)
        save_label.focus_set()
        count_save_canvas += 1


def get_name(event):
    name = name_entry.get()
    save_root.destroy()
    records_list[name] = [count_step, game_time]


# const

records_list = {}
status_game = True # while the number still not found self.read_line continue read next line
count_line, count_step, count_finish_label, count_save_canvas = 0, 0, 0, 0
game_info_ru = 'Числа\n' \
                    'В этой игре вам необходимо вычислить четырехзначное число. ' \
                    'Цифры в числе не повторяются. Результаты справа: первое число это количество правильных цифр;' \
                    ' второе число это количество правильных цифр на правильном месте.'
game_info_en = 'Numbers\n' \
                    'In this game you need to calculate a four-digit number.' \
                    ' The digits in the number are not repeated. ' \
                    'Results on the right: the first number is the number of valid digits;' \
                    'the second number is the number of correct digits in the right place.'
# info canvas

info_canvas = Canvas(root, height=50)
info_canvas.pack(side=RIGHT)

game_info = game_info_en
text = Text(info_canvas, width=40, height=11, wrap=WORD, bg='#F0F0F0', bd=0, state=NORMAL)
text.insert(1.0, game_info)
text.pack(side=TOP, padx=30)

error_line = Label(text="")
error_line.pack()

# buttons

setting_frame = Frame(root)
setting_frame.pack()
language_button = Button(setting_frame, text='русский', width=8)
language_button.pack(side=LEFT, padx=10, pady=5)
language_button.bind('<Button-1>', change_language)

info_button = Button(setting_frame, text='Close info', width=8)
info_button.pack(side=RIGHT, padx=10, pady=5)
info_button.bind("<Button-1>", info_button_canvas)

new_line()
root.mainloop()

if __name__ == '__main__':
    for i in records_list:
        print(i, records_list[i][0], records_list[i][1])
