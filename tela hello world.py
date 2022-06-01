from tkinter import*


#funções
def imprimir():
    lb1['text'] = in1.get()
    print(in1.get())


#window
janela = Tk()

#geometria
janela.geometry('300x300+500+500')
janela.minsize(width=400, height=180)
janela.maxsize(width=600, height=600)

#widgets
lb1 =Label(janela, text="Olá mundo!", font='Arial 26')

in1 = Entry(janela, font="Arial 26")
bt1 = Button(janela, text='Sair', font='Arial 26',command=quit)
bt2 = Button(janela, text= "imprimir",font='Arial 26', command=imprimir )

#layout
lb1.pack()
in1.pack()
bt1.pack()
bt2.pack()

#run
janela.mainloop()