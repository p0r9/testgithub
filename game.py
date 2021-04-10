from tkinter import* 

def Gamefuntion(event):
    CorrectNumber = 132
    UserGuess = -1
    for i in range (5) : 
        UserGuess = int(TextboxGuess.get())
        if UserGuess >  1000 or UserGuess  < 0 :
            LabelText.configure (text='Input Wrong!!!')
        elif  UserGuess == CorrectNumber :
            LabelText.configure (text='Correct!! :D')
        elif UserGuess > CorrectNumber :
            LabelText.configure (text='มากเกินไป')
        elif UserGuess < CorrectNumber :
            LabelText.configure (text='น้อยเกินไป')
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
LabelText = Label(MainWindow,text='text',font=('arial,18'))
LabelText.grid(row=3,column=0)
LabelText.bind ('<Button-1>',Gamefuntion)
MainWindow.mainloop()