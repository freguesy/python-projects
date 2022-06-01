from tkinter import *

#   'criar janela'

root = Tk()
root.grid_rowconfigure(0, weight=0)
root.grid_columnconfigure(0, weight=1)

#   'Max e Min da Janela'

root.minsize(width=400, height=200)
root.maxsize(width=600, height=200)


#    'IMC'
def imc():
    if bt1['text']:
         bt1['text'] = float(in2.get()) / (float(in1.get()) * float(in1.get()))




#   'Criar os Widgets'

lb1 = Label(root, text='Altura')
in1 = Entry(root, font="Arial 26")
lb2 = Label(root, text='Peso')
in2 = Entry(root, font="Arial 26")
bt1 = Button(root, text='IMC', command=imc)
lb3 = Label(root, text= "Status", font="Arial 16")

#   'Organizar os Widgets'

lb1.grid(row=0, column=0, sticky=NSEW)
in1.grid(row=1, column=0, sticky=NSEW)

lb2.grid(row=2, column=0, sticky=NSEW)
in2.grid(row=3, column=0, sticky=NSEW)

bt1.grid(row=4, column=0, sticky=NSEW)

lb3.grid(row=5, column=0, sticky=NSEW)


#   'Run'

root.mainloop()