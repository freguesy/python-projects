from sqlite3 import Row
from tkinter import *

#   'criar janela'

root = Tk()
root.configure(bg='white')
root.title('Cadastro')
frame1 = LabelFrame(root,text='Dados Pessoais:',bg='black',font=(30),foreground="white")
frame1.grid(sticky=NSEW)
#frame1.grid(row=5, column=2)
frame1.grid_rowconfigure(0 , weight=1)
frame2 = LabelFrame(root,text='Endereço:',bg='black',font=(30),foreground="white")
frame2.grid(sticky=NSEW)
#frame2.grid(row=5, column=2)
frame3 = LabelFrame(root,text='',bg='black',font=(30),foreground="white")
frame3.grid(sticky=NSEW)
#frame3.grid(row=5, column=2)

#   'Frame1'

lb1_fr1 = Label(frame1, text='Nome',font='algerian 24',background='black',foreground="white").grid(row=0, column=0)
in1 = Entry(frame1, font='algerian 24').grid(row=0, column=1)

lb2_fr2 = Label(frame1, text='idade',font='algerian 24',background='black',foreground="white").grid(row=1, column=0)
in2 = Entry(frame1, font='algerian 24').grid(row=1, column=1)

bt1 = Label(frame1, text='sexo',font='algerian 24',background='black',foreground="white").grid(row=2, column=0)
lb3_fr3 = Entry(frame1, font='algerian 24').grid(row=2, column=1)

#   'Frame2'





#   'Frame3'
Button(frame3,text='Gravar Dados',background='black',foreground="white").pack()
Button(frame3,text='Listar Dados',background='black',foreground="white").pack()



#   'Run'

root.mainloop()