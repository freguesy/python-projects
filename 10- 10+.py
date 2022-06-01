from tkinter import *


#   'funções'

def soma():
    if lb1['text'] < 10: 
        lb1['text'] +=1

def sub():
    if lb1['text'] >-10:
        lb1['text'] -=1

#   'criar janela'

root = Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

#   'janela tamanho'

root.geometry('400x180')

#   'criar widgets'

bt1 = Button(root, text='-', font='algerian 24', activebackground='red', background='#5F0AF5', command=sub)
bt2 = Button(root, text='+', font='algerian 24', activebackground='green', background='#5F0AF5', command=soma)
lb1 = Label(root, text=0, font='algerian 24', background='#5F0AF5')

#   'organizar widgets'

bt1.grid(row=0, column=0, sticky=NSEW)
bt2.grid(row=0, column=2, sticky=NSEW)
lb1.grid(row=0, column=1, sticky=NSEW)

#   'run'

root.mainloop()