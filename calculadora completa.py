from tkinter import *


#   'funções'

def entrada(valor):
    lb1['text'] += valor

#   'criar grades e colunas'

root = Tk()
root.grid_rowconfigure(0, weight=0)
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

lb1 = Label (root, text='', font='CASTELLAR')
bt1 = Button(root, text='1', font='CASTELLAR', command=lambda: entrada('1'))
bt2 = Button(root, text='2', font='CASTELLAR', command=lambda: entrada('2'))
bt3 = Button(root, text='3', font='CASTELLAR', command=lambda: entrada('3'))
bt4 = Button(root, text='4', font='CASTELLAR', command=lambda: entrada('4'))
bt5 = Button(root, text='5', font='CASTELLAR', command=lambda: entrada('5'))
bt6 = Button(root, text='6', font='CASTELLAR', command=lambda: entrada('6'))
bt7 = Button(root, text='7', font='CASTELLAR', command=lambda: entrada('7'))
bt8 = Button(root, text='8', font='CASTELLAR', command=lambda: entrada('8'))
bt9 = Button(root, text='9', font='CASTELLAR', command=lambda: entrada('9'))
bt10 = Button(root, text='0', font='CASTELLAR', command=lambda: entrada('0'))
bt11 = Button(root, text='+', font='CASTELLAR', command=lambda: entrada('+'))
bt12 = Button(root, text='-', font='CASTELLAR', command=lambda: entrada('-'))
bt13 = Button(root, text='*', font='CASTELLAR', command=lambda: entrada('*'))
bt14 = Button(root, text='/', font='CASTELLAR', command=lambda: entrada('/'))
bt15 = Button(root, text='C', font='CASTELLAR', command=lambda: entrada('C'))
bt16 = Button(root, text='=', font='CASTELLAR', command=lambda: entrada('='))

#   'organizar widgets'

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