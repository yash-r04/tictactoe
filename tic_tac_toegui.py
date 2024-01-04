from tkinter import *
import random

root = Tk()
root.title("TIC TAC TOE")

#labels
lab1 = Label(root, text="WELCOME TO TIC TAC TOE",font =("helvetica",28))
lab1.grid(row="0",column="0")

labp1= Label(root, text ="ENTER PLAYER 1",font =("helvetica",20))
labp1.grid(row="1",column="0")

labp2= Label(root, text ="ENTER PLAYER 2",font =("helvetica",20))
labp2.grid(row="2",column="0")

#player name entry
entry1 = Entry(root,text="player 1",font =("helvetica",28))
entry1.grid(row="1", column="1")

entry2 = Entry(root,text="player 2",font =("helvetica",28))
entry2.grid(row="2", column="1")
entry1.get()
entry2.get()


play_win = Label(root,font=("helvetica",30))
play_win.grid(row="6",column="1")

players = ["X","O"] 
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(root, font=("helvetica",30))
label.grid(row="4",column="0")
def start_game():  
    frame =Frame(root)
    frame.grid(row="6",column="0")
    player = random.choice(players)
    label.configure(text= player + "turn")
    
    for row in range(3):
      for column in range(3):
          buttons[row][column]= Button(frame,text ="",height=2,width=5,command= lambda row=row, column=column: next_turn(row,column))
          buttons[row][column].grid(row=row,column=column)
          
def new_game():
    global player
    
    player = random.choice(players)
    label.configure(text= player + "turn")
    play_win.config(text="")
    for row in range (3):
        for column in range(3):
            buttons[row][column].configure(text="",bg="#F0F0F0")

#next turn
def next_turn(row,column):
    global player
    play = [entry1.get(), entry2.get()]
    
    if buttons[row][column]['text'] == "" and winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if winner() is False:
                player = players[1]
                label.config(text=(players[1]+ " turn"))
            elif winner() is True:
                label.config(text=(players[0]+ " is the winner"))
                play_win.config(text=(play[0] + " congratsss!!"), fg="green")
            elif winner() =="Tie":
                label.config(text=("tie"))
                play_win.config(text=(play[0]+" and"+play[1]+ " it's a tie!!"), fg="blue")
        else:
        
            buttons[row][column]['text'] = player
            if winner() is False:
                player = players[0]
                label.config(text=(players[0]+ " turn"))
            elif winner() is True:
                label.config(text=(players[1]+ " is the winner"))
                play_win.config(text=(play[1] + " congratsss!!"), fg="green")
                
                #buttons/framework of the game
            elif winner() =="Tie":
                label.config(text=("tie"))
                play_win.config(text=(play[0]+" and"+play[1]+ " it's a tie!!"), fg="blue")
                
def winner():
    
    for row in range(3):
        if buttons[row][0]['text']== buttons[row][1]['text']==buttons[row][2]['text']!="":
            buttons[row][0].config(bg = "green")
            buttons[row][1].config(bg = "green")
            buttons[row][2].config(bg = "green")
            return True
    for column in range(3):
        if buttons[0][column]['text']== buttons[1][column]['text']==buttons[2][column]['text']!="":
            buttons[0][column].config(bg = "green")
            buttons[1][column].config(bg = "green")
            buttons[2][column].config(bg = "green")
            return True
    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text']!="":
        buttons[0][0].config(bg = "green")
        buttons[1][1].config(bg = "green")
        buttons[2][2].config(bg = "green")
        return True
    if buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text']!="":
        buttons[0][2].config(bg = "green")
        buttons[1][1].config(bg = "green")
        buttons[2][0].config(bg = "green")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="blue")
        return "Tie"
    else:
        return False
    
def empty_spaces():
    spaces =9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -=1
    if spaces ==0:
        return False  
    else:
        return True
    
but_start = Button(root, text="START",command= start_game)
but_start.grid(row="3", column="0")

but_new = Button(root, text="NEW GAME", command=new_game)
but_new.grid(row="3", column="1")


root.mainloop()