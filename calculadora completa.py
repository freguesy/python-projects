from tkinter import *


#   'funções'

def entrada(valor):
    lb1['text'] += valor


def limpar():
    lb1["text"] = ""

def r ():
    x=eval(lb1['text'])
    lb1['text'] = str(x)


#   'criar grades e colunas'

root = Tk()
root.configure(bg='red')
root.title("calculadora")
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)


#   'geometria'

root.geometry('220x400')


#   'janela.config(bg='')'

root.minsize(width=300, height=100)
root.maxsize(width=600, height=600)


#   'criar widgets'

lb1 = Label (root, text='', font='CASTELLAR',background='#5B5B69')
bt1 = Button(root, text='1', font='CASTELLAR', command=lambda: entrada('1'),background='#4B4B4F')
bt2 = Button(root, text='2', font='CASTELLAR', command=lambda: entrada('2'),background='#4B4B4F')
bt3 = Button(root, text='3', font='CASTELLAR', command=lambda: entrada('3'),background='#4B4B4F')
bt4 = Button(root, text='4', font='CASTELLAR', command=lambda: entrada('4'),background='#4B4B4F')
bt5 = Button(root, text='5', font='CASTELLAR', command=lambda: entrada('5'),background='#4B4B4F')
bt6 = Button(root, text='6', font='CASTELLAR', command=lambda: entrada('6'),background='#4B4B4F')
bt7 = Button(root, text='7', font='CASTELLAR', command=lambda: entrada('7'),background='#4B4B4F')
bt8 = Button(root, text='8', font='CASTELLAR', command=lambda: entrada('8'),background='#4B4B4F')
bt9 = Button(root, text='9', font='CASTELLAR', command=lambda: entrada('9'),background='#4B4B4F')
bt10 = Button(root, text='0', font='CASTELLAR', command=lambda: entrada('0'),background='#4B4B4F')
bt11 = Button(root, text='+', font='CASTELLAR', command=lambda: entrada('+'),background='#4B4B4F')
bt12 = Button(root, text='-', font='CASTELLAR', command=lambda: entrada('-'),background='#4B4B4F')
bt13 = Button(root, text='x', font='CASTELLAR', command=lambda: entrada('*'),background='#4B4B4F')
bt14 = Button(root, text='÷', font='CASTELLAR', command=lambda: entrada('/'),background='#4B4B4F')
bt15 = Button(root, text='C', font='CASTELLAR', command=limpar,background='#4B4B4F')
bt16 = Button(root, text='=', font='CASTELLAR',command= lambda: r(),background='#4B4B4F')


#   'organizar widgets'

lb1.grid(row=0, column=0, columnspan= 5)
lb1.grid(row=0, column=1, sticky=NSEW)
bt1.grid(row=1, column=1, sticky=NSEW)
bt2.grid(row=1, column=2, sticky=NSEW)
bt3.grid(row=1, column=3, sticky=NSEW)
bt4.grid(row=2, column=1, sticky=NSEW)
bt5.grid(row=2, column=2, sticky=NSEW)
bt6.grid(row=2, column=3, sticky=NSEW)
bt7.grid(row=3, column=1, sticky=NSEW)
bt8.grid(row=3, column=2, sticky=NSEW)
bt9.grid(row=3, column=3, sticky=NSEW)
bt10.grid(row=4, column=2, sticky=NSEW)
bt11.grid(row=1, column=4, sticky=NSEW)
bt12.grid(row=2, column=4, sticky=NSEW)
bt13.grid(row=3, column=4, sticky=NSEW)
bt14.grid(row=4, column=4, sticky=NSEW)
bt15.grid(row=4, column=1, sticky=NSEW)
bt16.grid(row=4, column=3, sticky=NSEW)


#   'run'

root.mainloop()