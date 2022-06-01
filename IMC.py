from tkinter import *

#   'criar janela'

root = Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#   'Max e Min da Janela'

root.minsize(width=400, height=200)
root.maxsize(width=600, height=200)


#    'IMC'
def imc():
    if bt1['text']:
         bt1['text'] = float(in2.get()) / (float(in1.get()) * float(in1.get()))




#   'Criar os Widgets'

lb1 = Label(root, text='Altura',background='#7505D6',foreground='white')
in1 = Entry(root, font='algerian 24',background='black',foreground='white')
lb2 = Label(root, text='Peso',background='#7505D6',foreground='white')
in2 = Entry(root, font='algerian 24',background='black',foreground='white')
bt1 = Button(root, text='IMC', command=imc, background='#7505D6',activebackground='#D62626',foreground='white')
lb3 = Label(root, text= "Status", font='algerian 24',background='black',foreground='white')

#   'Organizar os Widgets'

lb1.grid(row=0, column=0, sticky=NSEW)
in1.grid(row=1, column=0, sticky=NSEW)

lb2.grid(row=2, column=0, sticky=NSEW)
in2.grid(row=3, column=0, sticky=NSEW)

bt1.grid(row=4, column=0, sticky=NSEW)

lb3.grid(row=5, column=0, sticky=NSEW)


#   'Run'

root.mainloop()