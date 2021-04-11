from tkinter import* 
from random import randint

def Random(event):
    LottoNumber = randint(0,999999)
    LabelResult.configure(text=LottoNumber)

MainWindow = Tk()
Lottobutton = Button(MainWindow,text='สุ่มเลข',font=('arial,30'),width='20')
Lottobutton.grid(row=1)
Lottobutton.bind('<Button-1>',Random)
LabelResult = Label(MainWindow,text='อธิฐานสิ่งศักดิ์สิทธิขอให้ได้เลขที่ถูกรางวัล',font=('arial,30'))
LabelResult.grid(row=0)
MainWindow.mainloop()
