from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title('Tic Tac Toe Game')
playerA = StringVar()
playerB = StringVar()
playerA_name = Entry(tk, textvariable=playerA, bd=5)
playerA_name.grid(row=1, column=1, columnspan=8)
playerB_name = Entry(tk, textvariable=playerB, bd=5)
playerB_name.grid(row=2, column=1, columnspan=8)
bclick = False
flags = 0
buttons = []


def button_click(b):
    global bclick, flags
    if (bclick == False and b['text'] == ' '):
        b['text'] = 'X'
        b['fg'] = 'black'
        bclick = True
        flags = flags+1
        win_check()
    if (bclick == True and b['text'] == ' '):
        b['text'] = 'O'
        b['fg'] = 'white'
        bclick = False
        flags = flags+1
        win_check()


def disable_button():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def win_check():
    if(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
       button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
       button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
       button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
       button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
       button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
       button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
       button7['text'] == 'X' and button5['text'] == 'X' and button3['text'] == 'X'):
        for b in buttons:
            if(b['text'] == 'X'):
                b['fg'] = 'green'
        tkinter.messagebox.showinfo(
            'tic tac toe game', playerA.get()+' WON!!! ')
        disable_button()
    if(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
       button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
       button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
       button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
       button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
       button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
       button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
       button7['text'] == 'O' and button5['text'] == 'O' and button3['text'] == 'O'):
        for b in buttons:
            if(b['text'] == 'O'):
                b['fg'] = 'green'
        tkinter.messagebox.showinfo(
            'tic tac toe game', playerB.get()+' WON!!! ')
        disable_button()
    if(flags == 9):
        for b in buttons:
             b['fg'] = 'red'
        tkinter.messagebox.showinfo('tic tac toe game', ' DRAW ')
        disable_button()


labelA = Label(tk, text='playerA : ', font='Times 20 bold',
               bg='white', fg='black', height=1, width=8)
labelA.grid(row=1, column=0)
labelB = Label(tk, text='playerB : ', font='Times 20 bold',
               bg='white', fg='black', height=1, width=8)
labelB.grid(row=2, column=0)


# button
button1 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8, command=lambda: button_click(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8, command=lambda: button_click(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8, command=lambda: button_click(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8, command=lambda: button_click(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8, command=lambda: button_click(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8, command=lambda: button_click(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8, command=lambda: button_click(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8, command=lambda: button_click(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray',
                 fg='white', height=4, width=8, command=lambda: button_click(button9))
button9.grid(row=5, column=2)

buttons = [button1, button2, button3, button4,
           button5, button6, button7, button8, button9]


tk.mainloop()
