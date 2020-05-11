import random as rnd
import re
import string
from tkinter import *


class MyWindow:
    def __init__(self, win):
        self.s = open("unicode.txt", encoding="utf-8")
        self.p = open("plane.txt", encoding="utf-8")
        self.schar, self.model = self.random_name(self.s, self.p)


        self.lbl = Entry()
        self.lbl.place(x=60, y=50)

        self.btn = Button(win, text="Generate!!!", fg='blue', command = self.set_var)
        self.btn.place(x=80, y=100)

    def set_var(self):
        self.lbl.delete(0, 'end')
        self.lbl.insert(END, str(self.return_str(self.schar, self.model)))


    def random_name(self, special, plane):
        schar = []
        for x in special:
            for y in x.split():
                schar.append(y)

        model = []
        for x in plane:
            arr = x.split()[1:]
            for y in arr:
                if re.search(r"\S*\d+\S*", y):
                    if not y.isalnum():
                        model.append(y)

        return schar, model

    def return_str(self, schar, model):
        strrnd = rnd.choice(string.ascii_uppercase)
        scharrnd = rnd.choice(schar).upper()
        modelrnd = rnd.choice(model).upper()

        return strrnd + " " + scharrnd + " " + modelrnd

window = Tk()
mywin=MyWindow(window)
window.title('Elon Musk Name Generator')
window.geometry("400x300+10+10")
window.mainloop()

