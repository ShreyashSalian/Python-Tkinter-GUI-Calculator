from tkinter import *
import tkinter
class Calculator():
    def addition(self):
        total = float(self.e1.get()) + float(self.e2.get())
        self.e3.delete(0,END)
        self.e3.insert(END,total)

    def subtraction(self):
        total = float(self.e1.get()) - float(self.e2.get())
        self.e3.delete(0, END)
        self.e3.insert(END, total)

    def multiplication(self):
        total = float(self.e1.get()) * float(self.e2.get())
        self.e3.delete(0, END)
        self.e3.insert(END, total)

    def division(self):
        total = float(self.e1.get()) / float(self.e2.get())
        self.e3.delete(0, END)
        self.e3.insert(END, total)

    def clear(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)

    def __init__(self):
        self.t = Tk()
        self.t.geometry("305x300")
        l1 = Label(self.t,text = "Number 1",anchor = tkinter.E)
        self.e1 = Entry(self.t,bd=4,bg="#f7d9d9")
        l2 = Label(self.t,text = "Number 2",anchor = tkinter.E)
        self.e2 = Entry(self.t,bd=4,bg="#f7d9d9")
        l3 = Label(self.t,text = "Result",anchor = tkinter.E)
        self.e3 = Entry(self.t,bd=4,bg="#f7d9d9")
        self.b1 = Button(self.t,text = "Add",command = self.addition,bd=4,bg="#e6bfff")
        self.b2 = Button(self.t,text = "Sub",command = self.subtraction,bd=4,bg="#e6bfff")
        self.b3 = Button(self.t,text = "Mul",command = self.multiplication,bd=4,bg="#e6bfff")
        self.b4 = Button(self.t,text = "Div",command = self.division,bd=4,bg="#e6bfff")
        self.b5 = Button(self.t,text = "clear",command = self.clear,bd=4,bg="#e6bfff")

        l1.place(x = 20,y = 20,width = 60,height = 25)
        self.e1.place(x = 90,y = 20,width = 100,height = 25)

        l2.place(x = 20,y = 55,width = 60,height = 25)
        self.e2.place(x = 90,y = 55,width = 100,height = 25)

        l3.place(x = 20,y = 90,width = 60,height = 25)
        self.e3.place(x = 90,y = 90,width = 100,height = 25)

        self.b1.place(x = 20,y = 125,width = 40,height = 25)
        self.b2.place(x = 70,y = 125,width = 40,height = 25)
        self.b3.place(x = 120,y = 125,width = 40,height = 25)
        self.b4.place(x = 170,y = 125,width = 40,height = 25)
        self.b5.place(x = 220,y = 125,width = 40,height = 25)
        self.t.mainloop()
c = Calculator()