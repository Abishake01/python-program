import tkinter
from tkinter import *
window=tkinter.Tk()
window.title('Calculator')
txt=Entry(window,width=50).pack()
 
but1=Button(window,text='1').pack(side='left')
but2=Button(window,text='2').pack(side='top')
but3=Button(window,text='3').pack(side='right')
but4=Button(window,text='4').pack()
but5=Button(window,text='5').pack()
but6=Button(window,text='6').pack()
but7=Button(window,text='7').pack()
but8=Button(window,text='8').pack()
but9=Button(window,text='9').pack()

#top_f=tkinter.Frame(window).pack()
#bot_f=tkinter.Frame(window).pack(side='bottom')
#b1=tkinter.Button(top_f,text='1',bg='red').pack()
window.mainloop()