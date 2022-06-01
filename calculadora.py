from tkinter import*


def somar():
    lb2['text']=(int(in1.get())+int(in2.get()))
   
janela = Tk()

#geometria
janela.geometry('300x300+500+500')
janela.minsize(width=400, height=180)
janela.maxsize(width=600, height=600)


#widgets
lb1 =Label(janela, text="calculadora", font='Arial 26')
lb2 =Label (janela,text='',font='Arial 26')
lb3 =Label(janela, text='resultado',font='Arial 26')
in2 = Entry()
in1 = Entry()                              
bt1 = Button(janela, text='Somar', font='Arial 26',command=somar)

#layout
lb1.pack()
in1.pack()
in2.pack()
bt1.pack()
lb3.pack()
lb2.pack()

#run
janela.mainloop()




