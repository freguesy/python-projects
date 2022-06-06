import fractions
from tkinter import *

#   'criar janela'

root = Tk()


fr1 = Frame(root, bg='#7505D6')
fr2 = Frame(root, bg='#7505D6')
fr3 = Frame(root, bg='#7505D6')

#   'Max e Min da Janela'

root.minsize(width=400, height=200)
root.maxsize(width=1000, height=400)


#    'IMC'
def imc():
    if bt1['text']:
         bt1['text'] = round (float(in2.get()) / (float(in1.get()) * float(in1.get())),2)




#   'Criar os Widgets'

lb1_fr1 = Label(fr1, text='Altura',background='#7505D6',foreground='white', font='algerian 24')
in1 = Entry(fr1, font='algerian 24',background='black',foreground='white')
lb2_fr2 = Label(fr2, text='Peso',background='#7505D6',foreground='white', font='algerian 24')
in2 = Entry(fr2, font='algerian 24',background='black',foreground='white')
bt1 = Button(fr3, text='IMC', command=imc, background='#7505D6',activebackground='#D62626',foreground='white', font='algerian 24')
lb3_fr3 = Label(fr3, text= "Status", font='algerian 24',background='black',foreground='white')


fr1.pack()
fr2.pack()
fr3.pack()



#   'Organizar os Widgets'

lb1_fr1.grid(row=0, column=0)
in1.grid(row=1, column=0)

lb2_fr2.grid(row=0, column=0)
in2.grid(row=1, column=0)

bt1.grid(row=0, column=0)
lb3_fr3.grid(row=1, column=0)


#   'Run'

root.mainloop()
