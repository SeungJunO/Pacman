from tkinter import*

window = Tk()

w = Canvas(window, width=300,height=200)
w.pack()

w.create_text(100,100,text='가나다라')

mainloop()
