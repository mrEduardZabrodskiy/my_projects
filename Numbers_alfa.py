from tkinter import *
from random import randint
import datetime
import time
from pyautogui import press
import keyword

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
                            self.won_label()
                            break
                        else:
                            count_step += 1
                            self.label['text'] = f" {in_num}:{loc_num} "
                            self.won_label()
                            break
                    else:
                        if count_step == 0:
                            start_time = datetime.datetime.now()
                            count_step += 1
                            self.label['text'] = f" {in_num}:{loc_num} "
                            #self.entry.focus_lastfor()
                            #self.entry.insert(END, keyword)
                            break
                        else:
                            count_step += 1
                            self.label['text'] = f" {in_num}:{loc_num} "
                            if count_step == count_line:
                                new_line()
                            #self.entry.insert(TOP, press('tab'))
                            break
                #self.e.insert(0, press("tab"))

    def won_label(self):
        global count_step, count_finish_label, status_game
        if count_finish_label == 0:
            frame = self.frame
            finish_time = datetime.datetime.now()
            game_time = finish_time - start_time
            label = Label(text=f" You WIN\n {count_step} steps   {game_time}")
            frame.pack()
            label.pack()
            button_frame = Frame(root)
            save_button = Button(button_frame, text="Save", width=9)
            exit_button = Button(button_frame, text="Exit", width=9)
            button_frame.pack(ipady=10)
            save_button.pack(side=LEFT, padx=10)
            save_button.bind("<Button-1>", restart) # restart here only for test
            exit_button.pack(side=RIGHT, padx=10)
            exit_button.bind("<Button-1>", quit)
            count_finish_label += 1
            status_game = False

    def del_line(self):
        self.frame.destroy()
        self.label.destroy()
        self.entry.destroy()


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
    if info_button['text'] == 'Close info':
        info_canvas.config(width=0)
        info_button["text"] = 'Open info'
        text['text'] = ''
        text.config(width=0)
    else:
        info_canvas.config(width=300)
        info_button["text"] = 'Close info'
        text['text'] = 'info'
        text.config(width=20)


def new_line():
    """the function creates new line every time after reading the number you entered"""
    global l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15
    if count_line < 4:
        l1 = Line(root); l1.create_line()
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

def change_language():
    pass
def restart(event):
    pass


# const

num = random_number()# random number which you have to gues
status_game = True # while the number still not found self.read_line continue read next line
count_line, count_step, count_finish_label = 0, 0, 0

# info canvas

info_canvas = Canvas(root, width=300, height=0)
info_canvas.pack(side=RIGHT)
game_info = 'info'
text = Label(info_canvas, text=game_info, width=20)
text.pack()

error_line = Label(text="")
error_line.pack()
l1 = Label(text=num)
#l1.pack() # random number is displayed in the top

# buttons

setting_frame = Frame(root)
setting_frame.pack()
language_button = Button(setting_frame, text='en', width=8)
language_button.pack(side=LEFT, padx=10, pady=5)
language_button.bind('<Button-1>', change_language())

info_button = Button(setting_frame, text='Close info', width=8)
info_button.pack(side=RIGHT, padx=10, pady=5)
info_button.bind("<Button-1>", info_button_canvas)

new_line()
root.mainloop()

