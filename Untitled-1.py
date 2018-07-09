#!/usr/bin/env python
#-*-coding:utf-8-*-
from Tkinter import *
import random
import threading
class Uygulama(object):
    def __init__(self, master):
        self.master = master
        self.araclar()
    def multi(self):
        t = threading.Thread(name="kodlar", target=self.kodlar)
        t.start()
    def kodlar(self):
        for i in range(1):
            pencere.after(5000, self.kodlar)
            print "1"

    def araclar(self):
        self.etiket = Label(text="Sayı üretmek için düğmeye basınız!",
        fg="white",
        bg="#61380B",
        font="Helvetica 12 bold")
        self.etiket.pack()

        self.dugme = Button(self.master, text="Yeniden", command = self.multi)
        self.dugme.pack()
pencere = Tk()
uyg = Uygulama(pencere)
pencere.mainloop()
