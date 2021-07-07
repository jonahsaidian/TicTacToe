import tkinter as tk
import random
import math as m

#this is a simple python script which runs mulitdimensional TicTacToe using a tkinter GUI. All functions are stored within this single file to prevent confusion from rescource placement and orginization

#here are a few external variables to be added into the ui for selection, so far they are just to be adjusted in here
dim=4;
screenwidth=800;
screenheight=600;
boxwidth=int(screenwidth/(dim+1));
boxheight=int(screenheight/(dim+1));
boxfont=int(min(boxheight/10,boxwidth/12))


def nextturn():
    global play, moveslist, diff
    play=0
    if turn%2==1 and win==0 and len(moveslist)>0:
        #changes the note to say that it is the players turn
        note["text"]="It is now your turn, please make a move."
    elif turn%2==0 and win==0 and len(moveslist)>0:
        #here we tell the ai what to do when its turn begins. first is to change the note only if it is in fact the turn of the computer and the game is not over
        note["text"]="It is now the opponents turn, please wait."
        if diff==0:
            #for easy difficulty the AI will simply choose a random square that is available
            play = random.choice(moveslist)
        elif diff==1:
            #If the hard AI was chosen we run the hardai function to determine what the computer should play
            hardai()
        write(play)

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
        mtw=dim+1
        for i in range(len(winlist)):
            if len(xset.intersection(set(winlist[i]))) ==0:
                winmoves.append(list(set(winlist[i]).difference(oset)))
        random.shuffle(winmoves)
        if winmoves==[]:
            play = random.choice(moveslist)
        else:
            for i in range(len(winmoves)):
                if len(winmoves[i])<mtw:
                    winpath = winmoves[i]
                    mtw = len(winmoves)
            play = random.choice(winpath)

def wincheck():
    #here we check to see if either player has won, we run this code after every turn. Additionally we check to see if there are no moves left. in each case we change the note accordingly and may trigger a little flare to accentuate the win
    global xlist, win, olist, winlist, moveslist, note
    for j in range(len(winlist)):
        if set(winlist[j]).issubset(set(xlist)):
            note["text"]="Congratulations, You Win! Press R to restart or Q to Quit"
            win=1;
            winflare(j,win)
        elif set(winlist[j]).issubset(set(olist)):
            note["text"]= "Oh No, You Lose. Press R to restart or Q to Quit"
            win=2;
            winflare(j,win)
        elif moveslist ==[] and win==0:
            note["text"]= "So Close, You Tied. Press R to restart or Q to Quit"

#Below is the function for making moves in any given square. They first check to make sure they are being triggered only at the proper times, then remove the button in the square and replace it with the appropriate letter, we update the lists that track available moves and past moves, check if anyone has won, update the turn count, and last we move to the next turn
def write(i):
    global turn,xlist,olist,moveslist,labels,buttons
    if  win==0 and (i in moveslist):
        buttons[i].destroy()
        if turn % 2 ==1:
            labels[i]["text"]='X'
            xlist.append(i)
        elif turn % 2 ==0:
            labels[i]["text"]='O'
            olist.append(i)
        labels[i].grid(row=m.floor(i/dim) ,column=(i%dim))
        moveslist.remove(i)
        wincheck()
        turn +=1
        nextturn()

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

def setup():
    # here is the first funtion we run, it will create a prompt asking the user what difficulty they would like to play
    global window,askdiff,l1,beasy,bhard
    askdiff = tk.Frame(master=window, height=boxheight,width=boxwidth)
    askdiff.pack()
    l1=tk.Label(master = askdiff, text="Please select your difficulty",font=("Arial",2*boxfont))
    l1.pack()
    beasy = tk.Button(master=askdiff,text="Easy",font=("Arial",2*boxfont),command=easy,relief=tk.RAISED,padx=5,pady=5, borderwidth=3)
    beasy.pack()
    bhard = tk.Button(master=askdiff,text="Hard",font=("Arial",2*boxfont),command=hard,relief=tk.RAISED,padx=5,pady=5, borderwidth=3)
    bhard.pack()

def gamestart():
    # this will start the actual game. it creates the grid and all the buttons for playing. it also creates the notes that display game status, last it checks whose turn it is and starts the game sequence
    global diff, moveslist, xlist, olist, winlist, buttons, turn, footer, note, Game, frame, labels
    Game= tk.Frame(master=window)
    Game.pack(fill="both",expand=True)
    boxwidth=screenwidth/(dim+1)
    boxheight=screenheight/(dim+1)
    buttons=[]
    labels=[]
    for i in range(dim):
        Game.columnconfigure(i, weight=1, minsize=boxwidth)
        Game.rowconfigure(i, weight=1, minsize=boxheight)
        for j in range(dim):
            frame = tk.Frame(master=Game,relief=tk.RAISED,borderwidth=3,bg="Black")
            frame.grid(row=i, column=j,padx=5,pady=5,sticky="nsew")
            button = tk.Button(master=Game, text="Click to Play Here", font=("Arial",boxfont))
            button.grid(row=i,column=j)
            buttons.append(button)
            label = tk.Label(master=Game, text="", font=("Arial",int(boxfont*4)),bg="Black",fg="White")
            labels.append(label)
    footer = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=2)
    footer.pack(fill=tk.X)
    if turn == 1:
        note=tk.Label(master=footer,text="It is now your turn, please make a move.",font=("Arial",int(boxfont)))
    elif turn == 0:
        note=tk.Label(master=footer,text="It is now the opponents turn, please wait.",font=("Arial",int(boxfont)))
    note.pack()
    for i in range(dim*dim):
        buttons[i]["command"]= lambda arg=i: write(arg)
    nextturn()

def reset(r):
    #reset is a simple function which destroys the current game and rebuilds it as new. 
    global turn,xlist,win,olist,moveslist,winlist,askdiff,Game,footer
    Game.destroy()
    askdiff.destroy()
    footer.destroy()
    initialize()
    setup()

def quit(q):
    #here we quit the game
    window.destroy()

def winflare(j,win):
    #winflare is an optional function I included to make the experience a little more interesting when the game ends, it is basic right now but can be expanded. currently it will turn the winning move letters slightly larger and change their color
    global labels
    if win==1:
        color="Yellow"
    elif win==2:
        color ="Red"
    for i in range(dim*dim):
        if (i in winlist[j]):
            labels[i]["font"]=("Arial",int(boxfont*5))
            labels[i]["fg"]=color


def initialize():
    global turn,xlist,win,olist,moveslist,winlist
    #here is the first funstion of the code, we begin by defining our lists and generating a random number to decide who goes first
    turn = random.randint(0,1)
    xlist=[];
    win = 0;
    olist=[];
    moveslist=[];
    for i in range(dim*dim):
        moveslist.append(i)
    winlist=[]
    diagonal=[]
    revdiagonal=[]
    for i in range(dim):
        rows=[]
        columns=[]    
        for j in range(dim):
            rows.append(i*dim+j)
            columns.append(i+dim*j)
        winlist.append(rows)
        winlist.append(columns)
        diagonal.append(i*(dim+1))
        revdiagonal.append((i+1)*(dim-1))
    winlist.append(diagonal)
    winlist.append(revdiagonal)



initialize()

#we build the window used for the game
window = tk.Tk()
window.title("TicTacToe")

#I have chosen to bind the reset and quit commands to the window so they may be used at any time to reset or quit
window.bind('<r>',reset)
window.bind('<R>',reset)
window.bind('<q>',quit)
window.bind('<Q>',quit)

#we setup the starting window which will ask the user their preferred difficulty
setup()

#and finally we begin the mainloop to track any and all user inputs
window.mainloop()
