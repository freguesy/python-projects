from tkinter import *
import tkinter as tk

#   'criar janela'

root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)
root.grid_columnconfigure(6, weight=1)
root.grid_columnconfigure(7, weight=1)
root.grid_columnconfigure(8, weight=1)
root.grid_columnconfigure(9, weight=1)


#   'funçao'


var =StringVar()
def autocap(*arg):
    var.set(var.get().title())
var.trace("w", autocap)


#   'configuraçoes janela'


root.configure(bg='black')
root.title('Cadastro')
frame1 = LabelFrame(root,text='Dados Pessoais:',bg='black',font=(30),foreground="white")
frame1.grid(row=0, column=0, sticky=NSEW)
frame2 = LabelFrame(root,text='Endereço:',bg='black',font=(30),foreground="white")
frame2.grid(row=1, column=0,sticky=NSEW)
frame3 = LabelFrame(root,text='',bg='black',font=(30),foreground="white")
frame3.grid(row=2, column=0,sticky=NSEW)


#   'Frame1'


lb1 = Label(frame1, text='Nome:',font='Bahnschrift',background='black',foreground="white").grid(row=0, column=0,sticky=EW)
in1 = Entry(frame1, font='Bahnschrift',textvariable=var).grid(row=0, column=1,sticky=EW,columnspan=5)

lb2 = Label(frame1, text='CPF:',font='Bahnschrift',background='black',foreground="white").grid(row=1, column=0,sticky=EW)
in2 = Entry(frame1, font='Bahnschrift').grid(row=1, column=1,sticky=EW)

lb3 = Label(frame1, text='Telefone:',font='Bahnschrift',background='black',foreground="white").grid(row=1, column=2,sticky=EW)
in3 = Entry(frame1, font='Bahnschrift').grid(row=1, column=3,sticky=EW)

lb4 = Label(frame1, text='Data Nasc:',font='Bahnschrift',background='black',foreground="white").grid(row=1, column=4,sticky=EW)
in4 = Entry(frame1, font='Bahnschrift').grid(row=1, column=5,sticky=EW)


#   'Frame2'


lb5 = Label(frame2, text='Rua:',font='Bahnschrift',background='black',foreground="white").grid(row=0, column=0,sticky=EW)
in5 = Entry(frame2, font='Bahnschrift').grid(row=0, column=1,sticky=EW,columnspan=7,ipadx=100)

lb6 = Label(frame2, text='N°:',font='Bahnschrift',background='black',foreground="white").grid(row=0, column=4,sticky=EW)
in6 = Entry(frame2, font='Bahnschrift').grid(row=0, column=5,sticky=EW)

lb7 = Label(frame2, text='Bairro:',font='Bahnschrift',background='black',foreground="white").grid(row=1, column=0,sticky=EW)
in7 = Entry(frame2, font='Bahnschrift').grid(row=1, column=1,sticky=EW)

lb8 = Label(frame2, text='Cidade',font='Bahnschrift',background='black',foreground="white").grid(row=1, column=2,sticky=EW)
in8 = Entry(frame2, font='Bahnschrift').grid(row=1, column=3,sticky=EW)

lb9 = Label(frame2, text='UF:',font='Bahnschrift',background='black',foreground="white").grid(row=1, column=4,sticky=EW)
in9 = Entry(frame2, font='Bahnschrift').grid(row=1, column=5,sticky=EW)


#   'Frame3'


Button(frame3,text='Gravar Dados',background='black',foreground="white").grid(sticky=EW)

Button(frame3,text='Listar Dados',background='black',foreground="white").grid(sticky=EW)


#   'Run'


root.mainloop()