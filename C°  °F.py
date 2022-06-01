from tkinter import *



#   'criar janela'

root = Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


#   'Criar os Widgets'

lb1 = Label(root, text='C°',background='#7505D6',foreground='white', font='algerian 24')
in1 = Entry(root, font='algerian 24',background='black',foreground='white')

#   'Organizar os Widgets'

lb1.grid(row=0, column=0, sticky=NSEW)
in1.grid(row=0, column=1, sticky=NSEW)

#   'Run'

root.mainloop()