# 2 player XOX Game
import random
def choiceCheck(value,acceptableValues): #checking players choice is it valid input
    notAcceptable=True #to enter while loop
    if len(acceptableValues)==0: #on second play acceptable values needs to replaced
        acceptableValues=["1","2","3","4","5","6","7","8","9"] #re-assing values
        
    
    while notAcceptable: 
        if value in acceptableValues: #check player input  
            acceptableValues.remove(value) #remove used input to prevent entering again
            notAcceptable=False #break while
            return value #return correct player input
        else: #ask player to enter correct input
            print("Please enter acceptable number between 0-9 and not entered before")
            value= input()
def showBoard(board): #to show current board
    print(board[7],"|",board[8],"|",board[9])
    print(board[4],"|",board[5],"|",board[6])    
    print(board[1],"|",board[2],"|",board[3])
        
def movePX(acceptableValues,board):#player X move function
    print("Player X Please Choose a position on board:")
    choicePlayer=input() #player enters input here
    choicePlayer=choiceCheck(choicePlayer,acceptableValues) #input checked here
    board[int(choicePlayer)]="X" #writes X choosen position
    showBoard(board) #show new board
    
def movePO(acceptableValues,board): # player O move function similiar to aove
    print("Player O Please Choose a position on board:")
    choicePlayer =input()
    choicePlayer=choiceCheck(choicePlayer,acceptableValues)
    board[int(choicePlayer)]="O"
    showBoard(board)
    
def checkboard(board): #chechs board for any winnings and ends game
    if board[1]==board[2]==board[3]: #conditions of winning
        print(f"Winner is player {board[1]}")
        return False
    elif board[1]==board[5]==board[9]:
        print(f"Winner is player {board[1]}")
        return False
    elif board[1]==board[4]==board[7]:
        print(f"Winner is player {board[1]}")
        return False
    elif board[2]==board[5]==board[8]:
        print(f"Winner is player {board[2]}")
        return False
    elif board[3]==board[5]==board[7]:
        print(f"Winner is player {board[3]}")
        return False
    elif board[3]==board[6]==board[9]:
        print(f"Winner is player {board[3]}")
        return False
    elif board[4]==board[5]==board[6]:
        print(f"Winner is player {board[4]}")
        return False
    elif board[7]==board[8]==board[9]:
        print(f"Winner is player {board[7]}")
        return False
    
    
def playAgain(): #function to ask player he wants to play again
    notAcceptable=True
    acceptableValues=["0","1"]
    print("Do you like to rematch? Please enter 1")
    print("Do you like to exit? Please enter 0")
    value =input()
    while notAcceptable:
        if value in acceptableValues: #checks correct input
            notAcceptable=False
            if value=='0': #if player wants to quit
                return False #return false to exit
            else: #continue to play game
                game(isplaying)
        else: #wrong input ask player to enter again
            print("Please enter acceptable value 0-1")
            value= input()
            
def coinflip(): #if players are cant decide whos first
    print("Hard to decide whos first?")
    print("Enter 1 to flip a coint")
    print("Enter any other to to pass")
    isFlipping=input()
    c=int(5) #random int number to pass second if check
    if isFlipping=='1': c= random.randrange(0, 2) #if they are wan to flip coin
    
    if c==0:
        print("Tails!")
    else:
        print("Heads!")
        
            
        

def intro(): #flavor text
    print("Welcome to 2 Player XOX game")
    
def game(isplaying): #body of the game most important function 
    acceptableValues=["1","2","3","4","5","6","7","8","9"] #positions on board
    board=["0","1","2","3","4","5","6","7","8","9"] #board definition
    while isplaying==True: #while for continious game
        print("Player 1 is Plays as X. Player 2 is plays as O") #general reminders
        print("Board is Like Below Please Remember This")
        print("7|8|9")
        print("4|5|6")
        print("1|2|3")
        movePX(acceptableValues,board) #actual game starts
        movePO(acceptableValues,board)
        movePX(acceptableValues,board)
        movePO(acceptableValues,board)
        movePX(acceptableValues,board)
        isplaying=checkboard(board) #after players moved 3rd time we start to check win conditions
        if isplaying==False:break #if anyone wins ends game
        movePO(acceptableValues,board)
        isplaying=checkboard(board)
        if isplaying==False:break
        movePX(acceptableValues,board)
        isplaying=checkboard(board)
        if isplaying==False:break
        movePO(acceptableValues,board)
        isplaying=checkboard(board)
        if isplaying==False:break
        movePX(acceptableValues,board)
        isplaying=checkboard(board)
        if isplaying==False:break
        print("I's a draw!") #if nobody wins its a draw
    
isplaying=True #gameplay start attribute
running=True #is game running
while running==True:
    intro() # intro function call 
    coinflip() #coinflip function call
    game(isplaying) # game function call
    running=playAgain() #ask player here to wants to play again if he say yes while continues
            