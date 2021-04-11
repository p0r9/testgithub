from tkinter import* 
from random import randint

CorrectNumber = randint(0,1001)
print (CorrectNumber)
def Gamefuntion(event):
    UserGuess = int(TextboxGuess.get())
    if UserGuess < 0 or UserGuess  < 0 :
        LabelText.configure (text='Input Wrong!!!',fg='red')
    elif  UserGuess == CorrectNumber :
        LabelText.configure (text='Correct!! :D',fg='green')
    elif UserGuess > CorrectNumber :
         LabelText.configure (text='มากเกินไป',fg='red')
    elif UserGuess < CorrectNumber :
        LabelText.configure (text='น้อยเกินไป',fg='red')
    else :
        LabelText.configure (text='Input Wrong!!!')

MainWindow = Tk()
LabelGuess = Label(MainWindow,text='ใส่ตัวเลข 1-1000',font=('arial,18'))
LabelGuess.grid(row=0,column=0)
TextboxGuess = Entry(MainWindow,width=('16'))
TextboxGuess.grid(row=1,column=0)
Enterbutton = Button(MainWindow,text='Enter',font=('arial,30'),width=('12'))
Enterbutton.grid(row=2,column=0)
Enterbutton.bind('<Button-1>',Gamefuntion)
LabelText = Label(MainWindow,text='text',font=('arial,18'),fg='green')
LabelText.grid(row=3,column=0)
LabelText.bind ('<Return>',Gamefuntion)
#RoundLabel = Label(MainWindow,text='รอบที่ 1',font=('arial,18'),fg='blue')
#RoundLabel.grid(row=4,column=0)
MainWindow.mainloop()