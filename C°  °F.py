from lzma import FILTER_LZMA1
from tkinter import *

#criar janela

root = Tk()
fr1 = Frame(root,bg='red')
fr2 = Frame(root,bg='white')



#Calculo

def cn():
    if in1.get().replace('.','',1).isdigit():
        r =float(in1.get())*1.8+32
        lb2['text'] = r
    else:
        lb2['text'] = "Valor invalido"

#criar os widgets

lb1 = Label(fr1, text='C°', font="Arial 20")
in1 = Entry(fr1, font="Arial 16")
bt2 = Button(fr2, text='°F', font="Arial 20", command=cn)
lb2 = Label(fr2, text='Resultado', font="Arial 20")


fr1.pack()
fr2.pack()

#organizar os widgets

lb1.grid(row=0, column=0, sticky=NSEW)
in1.grid(row=0, column=1, sticky=NSEW)

bt2.grid(row=0, column=0, sticky=NSEW)
lb2.grid(row=0, column=1, sticky=NSEW)


#executar a janela
root.mainloop()