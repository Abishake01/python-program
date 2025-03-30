import tkinter
from tkinter.ttk import Button
page=tkinter.Tk()
page.title('Starting')
lable=tkinter.Label(page,text='working').pack()
bt=Button(page,text='enter').pack()
page.geometry('350x200') 
page.mainloop()

'''
txt=Entry(page,width=10)
txt.grid(column=1,row=0)
def clicked():
    res='welcome'+txt.get()
    l1.configure(text=res)
bt=Button(page,text='Enter',command=clicked)
'''