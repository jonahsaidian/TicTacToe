import tkinter as tk
import random as rand

#this is a simple python script which runs TicTacToe using a tkinter GUI. All functions are stored within this single file to prevent confusion from rescource placement and orginization

#we begin by defining our lists and generating a random number to decide who goes first
turn = rand.randint(0,1)
#turn = 1;

xlist=[];
win = 0;
olist=[];
moveslist=[1,2,3,4,5,6,7,8,9];
winlist=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]];

def xturn():
    #changes the note to say that it is the players turn
    global note
    if win==0 and len(moveslist)>0:
        note["text"]="It is now your turn, please make a move."

def oturn():
    #here we tell the ai what to do when its turn begins. first is to change the note only if it is in fact the turn of the computer and the game is not over
    global note
    global moveslist
    global win
    global play
    if win==0 and len(moveslist)>0:
        note["text"]="It is now the opponents turn, please wait."
        
        if diff==0:
            #for easy difficulty the AI will simply choose a random square that is available
            play = rand.choice(moveslist)
        elif diff==1:
            #If the hard AI was chosen we run the hardai function to determine what the computer should play
            hardai()

        #once the choice of square is made we trigger the actual move here
        if play==1:
            o1()
        elif play==2:
            o2()
        elif play==3:
            o3()
        elif play==4:
            o4()
        elif play==5:
            o5()
        elif play==6:
            o6()
        elif play==7:
            o7() 
        elif play==8:
            o8() 
        elif play==9:
            o9()

def hardai():
    #here is the full hard AI, it follows a relatively simple strategy 
    global xlist, olist, moveslist, winlist, play
    xset = set(xlist)
    oset = set(olist)
    winmoves=[]
    play=0

    #first we check if O can win this turn, if it can then we make the winning move
    for i in range(len(winlist)):
        mtw = list(set(winlist[i]).difference(oset))
        if len(mtw) == 1 and (mtw[0] in moveslist):
            play = mtw[0]

    #if a move was not chosen in the previous section we move on to the next consideration. We check if X can win next turn, if yes we move to block that win
    if play == 0:
        for i in range(len(winlist)):
            mtw = list(set(winlist[i]).difference(xset))
            if len(mtw) == 1 and (mtw[0] in moveslist):
                play = mtw[0]

    #if neither player can win immediately we instead look at possible win paths not already blocked by x, then choose the shortest one at random
    if play ==0:
        mtw=4
        for i in range(len(winlist)):
            if len(xset.intersection(set(winlist[i]))) ==0:
                winmoves.append(list(set(winlist[i]).difference(oset)))
        rand.shuffle(winmoves)
        if winmoves==[]:
            play = rand.choice(moveslist)
        else:
            for i in range(len(winmoves)):
                if len(winmoves[i])<mtw:
                    winpath = winmoves[i]
                    mtw = len(winmoves)
            play = rand.choice(winpath)





def wincheck():
        #here we check to see if either player has won, we run this code after every turn. Additionally we check to see if there are no moves left. in each case we change the note accordingly
    global xlist
    global win
    global olist
    global winlist
    global moveslist
    global note
    for j in range(len(winlist)):
        if set(winlist[j]).issubset(set(xlist)):
            note["text"]="Congratulations, You Win!"
            win=1;
        elif set(winlist[j]).issubset(set(olist)):
            note["text"]= "Oh No, You Lose."
            win=1;
        elif moveslist ==[] and win==0:
            note["text"]= "So Close, You Tied."

#Below are all of the commands for making moves in any given square. They first check to make surethey are being triggered only at the proper times, then remove the button in the square and replace it with the appropriate letter, we update the lists that track available moves and past moves, check if anyone has won, update the turn count, and last we move to the next turn
def x1():
    global turn
    global xlist
    global moveslist
    if turn % 2 == 1 and win==0 and (1 in moveslist):
        b1.destroy()
        x1label = tk.Label(master=Game, text="X", font=("Arial",100),bg="Black",fg="White")
        x1label.grid(row=2,column=0)
        moveslist.remove(1)
        xlist.append(1)
        wincheck()
        turn +=1
        oturn()

def x2():
    global turn
    global xlist
    global moveslist
    if turn % 2 == 1 and win==0 and (2 in moveslist):
        b2.destroy()
        x2label = tk.Label(master=Game, text="X", font=("Arial",100),bg="Black",fg="White")
        x2label.grid(row=2,column=1)
        moveslist.remove(2)
        xlist.append(2)
        wincheck()
        turn +=1
        oturn()

def x3():
    global turn
    global xlist
    global moveslist
    if turn % 2 == 1 and win==0 and (3 in moveslist):
        b3.destroy()
        x3label = tk.Label(master=Game, text="X", font=("Arial",100),bg="Black",fg="White")
        x3label.grid(row=2,column=2)
        moveslist.remove(3)
        xlist.append(3)
        wincheck()
        turn +=1
        oturn()

def x4():
    global turn
    global xlist
    global moveslist
    if turn % 2 == 1 and win==0 and (4 in moveslist):
        b4.destroy()
        x4label = tk.Label(master=Game, text="X", font=("Arial",100),bg="Black",fg="White")
        x4label.grid(row=1,column=0)
        moveslist.remove(4)
        xlist.append(4)
        wincheck()
        turn +=1
        oturn()

def x5():
    global turn
    global xlist
    global moveslist
    if turn % 2 == 1 and win==0 and (5 in moveslist):
        b5.destroy()
        x5label = tk.Label(master=Game, text="X", font=("Arial",100),bg="Black",fg="White")
        x5label.grid(row=1,column=1)
        moveslist.remove(5)
        xlist.append(5)
        wincheck()
        turn +=1
        oturn()

def x6():
    global turn
    global xlist
    global moveslist
    if turn % 2 == 1 and win==0 and (6 in moveslist):
        b6.destroy()
        x6label = tk.Label(master=Game, text="X", font=("Arial",100),bg="Black",fg="White")
        x6label.grid(row=1,column=2)
        moveslist.remove(6)
        xlist.append(6)
        wincheck()
        turn +=1
        oturn()

def x7():
    global turn
    global xlist
    global moveslist
    if turn % 2 == 1 and win==0 and (7 in moveslist):
        b7.destroy()
        x7label = tk.Label(master=Game, text="X", font=("Arial",100),bg="Black",fg="White")
        x7label.grid(row=0,column=0)
        moveslist.remove(7)
        xlist.append(7)
        wincheck()
        turn +=1
        oturn()

def x8():
    global turn
    global xlist
    global moveslist
    if turn % 2 == 1 and win ==0 and (8 in moveslist):
        b8.destroy()
        x8label = tk.Label(master=Game, text="X", font=("Arial",100),bg="Black",fg="White")
        x8label.grid(row=0,column=1)
        moveslist.remove(8)
        xlist.append(8)
        wincheck()
        turn +=1
        oturn()

def x9():
    global turn
    global xlist
    global moveslist
    if turn % 2 == 1 and win==0 and (9 in moveslist):
        b9.destroy()
        x9label = tk.Label(master=Game, text="X", font=("Arial",100),bg="Black",fg="White")
        x9label.grid(row=0,column=2)
        moveslist.remove(9)
        xlist.append(9)
        wincheck()
        turn +=1
        oturn()



def o1():
    global turn
    global olist
    global moveslist
    if turn % 2 ==0 and win==0 and (1 in moveslist):
        b1.destroy()
        o1label = tk.Label(master=Game, text="O", font=("Arial",100),bg="Black",fg="White")
        o1label.grid(row=2,column=0)
        moveslist.remove(1)
        olist.append(1)
        wincheck()
        turn +=1
        xturn()

def o2():
    global turn
    global olist 
    global moveslist
    if turn % 2 ==0 and win==0 and (2 in moveslist):
        b2.destroy()
        o2label = tk.Label(master=Game, text="O", font=("Arial",100),bg="Black",fg="White")
        o2label.grid(row=2,column=1)
        moveslist.remove(2)
        olist.append(2)
        wincheck()
        turn +=1
        xturn()

def o3():
    global turn
    global olist
    global moveslist
    if turn % 2 ==0 and win==0 and (3 in moveslist):
        b3.destroy()
        o3label = tk.Label(master=Game, text="O", font=("Arial",100),bg="Black",fg="White")
        o3label.grid(row=2,column=2)
        moveslist.remove(3)
        olist.append(3)
        wincheck()
        turn +=1
        xturn()

def o4():
    global turn
    global olist
    global moveslist
    if turn % 2 ==0 and win==0 and (4 in moveslist):
        b4.destroy()
        o4label = tk.Label(master=Game, text="O", font=("Arial",100),bg="Black",fg="White")
        o4label.grid(row=1,column=0)
        moveslist.remove(4)
        olist.append(4)
        wincheck()
        turn +=1
        xturn()

def o5():
    global turn
    global olist
    global moveslist
    if turn % 2 ==0 and win==0 and (5 in moveslist):
        b5.destroy()
        o5label = tk.Label(master=Game, text="O", font=("Arial",100),bg="Black",fg="White")
        o5label.grid(row=1,column=1)
        moveslist.remove(5)
        olist.append(5)
        wincheck()
        turn +=1
        xturn()

def o6():
    global turn
    global olist
    global moveslist
    if turn % 2 ==0 and win==0 and (6 in moveslist):
        b6.destroy()
        o6label = tk.Label(master=Game, text="O", font=("Arial",100),bg="Black",fg="White")
        o6label.grid(row=1,column=2)
        moveslist.remove(6)
        olist.append(6)
        wincheck()
        turn +=1
        xturn()

def o7():
    global turn
    global olist
    global moveslist
    if turn % 2 ==0 and win==0 and (7 in moveslist):
        b7.destroy()
        o7label = tk.Label(master=Game, text="O", font=("Arial",100),bg="Black",fg="White")
        o7label.grid(row=0,column=0)
        moveslist.remove(7)
        olist.append(7)
        wincheck()
        turn +=1
        xturn()

def o8():
    global turn
    global olist
    global moveslist
    if turn % 2 ==0 and win==0 and (8 in moveslist):
        b8.destroy()
        o8label = tk.Label(master=Game, text="O", font=("Arial",100),bg="Black",fg="White")
        o8label.grid(row=0,column=1)
        moveslist.remove(8)
        olist.append(8)
        wincheck()
        turn +=1
        xturn()

def o9():
    global turn
    global olist
    global moveslist
    if turn % 2 ==0 and win==0 and (9 in moveslist):
        b9.destroy()
        o9label = tk.Label(master=Game, text="O", font=("Arial",100),bg="Black",fg="White")
        o9label.grid(row=0,column=2)
        moveslist.remove(9)
        olist.append(9)
        wincheck()
        turn +=1
        xturn()

#the easy and hard functions simply store the user choice at the start of the game for the difficulty of the AI, and then begin the game
def easy():
    global diff
    diff=0
    askdiff.destroy()
    gamestart()

def hard():
    global diff
    diff=1
    askdiff.destroy()
    gamestart()

#we build the window used for the game
window = tk.Tk()
window.title("TicTacToe")

#create a prompt asking the user what difficulty they would like to play and then start the game
askdiff = tk.Frame(master=window, height=200,width=250)
askdiff.pack()
l1=tk.Label(master = askdiff, text="Please select your difficulty")
l1.pack()
beasy = tk.Button(master=askdiff,text="Easy",command=easy)
beasy.pack()
bhard = tk.Button(master=askdiff,text="Hard",command=hard)
bhard.pack()



def gamestart():
        # this will start the actual game. it creates the grid and all the buttons for playing. it also creates the notes that display game status, last it checks whose turn it is and starts the game sequence
    global diff 
    global moveslist, xlist, olist, winlist
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global turn, footer, note, Game, frame
    Game= tk.Frame(master=window)
    Game.pack()

    for i in range(3):
        Game.columnconfigure(i, weight=1, minsize=250)
        Game.rowconfigure(i, weight=1, minsize=200)
        for j in range(3):
            frame = tk.Frame(
                master=Game,
                relief=tk.RAISED,
                borderwidth=3,
                bg="Black"
            )
            frame.grid(row=i, column=j,padx=5,pady=5,sticky="nsew")



    b1=tk.Button(master=Game, text="Click to Play Here", command=x1)
    b1.grid(row=2,column=0)
    b2=tk.Button(master=Game, text="Click to Play Here", command=x2)
    b2.grid(row=2,column=1)
    b3=tk.Button(master=Game, text="Click to Play Here", command=x3)
    b3.grid(row=2,column=2)
    b4=tk.Button(master=Game, text="Click to Play Here", command=x4)
    b4.grid(row=1,column=0)
    b5=tk.Button(master=Game, text="Click to Play Here", command=x5)
    b5.grid(row=1,column=1)
    b6=tk.Button(master=Game, text="Click to Play Here", command=x6)
    b6.grid(row=1,column=2)
    b7=tk.Button(master=Game, text="Click to Play Here", command=x7)
    b7.grid(row=0,column=0)
    b8=tk.Button(master=Game, text="Click to Play Here", command=x8)
    b8.grid(row=0,column=1)
    b9=tk.Button(master=Game, text="Click to Play Here", command=x9)
    b9.grid(row=0,column=2)


    footer = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=2)
    #footer.rowconfigure(weight=1, minsize=75)
    footer.pack(fill=tk.X)
    note = tk.Label(master = footer, text="")

    if turn == 1:
        note=tk.Label(master=footer,text="It is now your turn, please make a move.")
    elif turn == 0:
        note=tk.Label(master=footer,text="It is now the opponents turn, please wait.")
        oturn()

    note.pack()


#and finally we begin the mainloop to track any and all user inputs
window.mainloop()
