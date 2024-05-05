import random #IMPORT RANDOM FOR TOSS AND COMPUTER TURNS
#GLOBAL VARIABLES
name_2=True
name_a=True
name_b=True
name=True
name11=''
name12=''
toss=0
n=""
N=''
modee=0
count=0
turn=0
current_player=""#CURRENT PLAYER IS EMPTY IT WILL FILL WHEN PLAYER WILL CHOSE SYMBOL IN DUAL PLAYER MODE
#ASSIGNING 9 variable VALUE TO LIST IT WILL EMPTY
board=["-","-","-",
       "-","-","-",
       "-","-","-"]
#DEFINING FUNCTION FOR BOARD IN LIST
def display_board():
        print(board[0] + "|" + board[1] + "|" + board[2])#BOARD MEANS LIST AND 0 MEANS ITS INDEX AND SO ON
        print(board[3] + "|" + board[4] + "|" + board[5])
        print(board[6] + "|" + board[7] + "|" + board[8])
#FUNTION OF MAIN MENU
def main_menu():
        global modee         #GLOBAL MEANS GLOBAL VARIABLES
        global N

        print('Press 1 for single player mode ')
        print('-------------------------------')   #DASH LINES TO MAKE GAME HANDSOME VIEW ONLY
        print('Press 2 for double player mode ')
        print('-------------------------------')
        print('Press N or n key for Exit ')
        print('-------------------------------')

        num=input('Enter the number to select mode:')
        while num not in ['1','2','N','n']:     #WHILE LOOP WHICH WILL NOT ALLOW WRONG ENTRY
                print("-----------------------------------------------------------------------------")
                print("Invalid number")
                print("-----------------------------------------------------------------------------")
                num=input('Enter the number to select mode:')
                print("-----------------------------------------------------------------------------")
        num=eval(num)
        check=num
        print('-----------------------------------------------------------------------------')
        if num==1:
            Level_selection()
        elif num==2:
                modee=4
                double_player_mode()
        elif num==N or num==n:
                exit()
        else:
            exit()    #EXIT FUNCTION TO END THE GAME
#FUNCTION OF LEVEL SELECTION       
def Level_selection():
        global modee
        global  N
        print("SELECT YOUR MODE")
        print('-------------------------------')
        print("Press 1 for Easy Level")
        print('-------------------------------')
        print("Press 2 for Medium Level")
        print('-------------------------------')
        print("Press 3 for Hard Level")
        print('-------------------------------')
        print('Press N or n key for Exit ')
        print('-------------------------------')
        mode=input("Enter the number to select modde:")
        while mode not in ['1','2','3','N','n']:   #WHILE LOOP WHICH WILL NOT ALLOW WRONG ENTRY
                print("-----------------------------------------------------------------------------")
                print("Invalid number")
                print("-----------------------------------------------------------------------------")
                mode=input('Enter the number to select mode:')
                print("-----------------------------------------------------------------------------")
        mode=eval(mode)
        print('-----------------------------------------------------------------------------')
        if mode==1:
                modee=mode
                easy_mode()
        elif mode==2:
                modee=mode  #storing value put by user for mode in modee
                easy_mode()#small changings only in easy mode to make it medium mode
        elif mode==3:
                modee=mode
                easy_mode()#small changings again in easy mode to make it hard mode
        elif mode==N or mode==n:
                exit()               
        else:
                exit()
        
def Toss():                #DEFINIG TOSS FUNCTION FOR TOSS BETWEEN TWO PLAYER MODE ONLY
        global name11      #NAME1 VALUE ASSIGN TO NAME11 
        global name12      #NAME2 VALUE ASSIGN TO NAME12 
        global toss        #ASSIGNING THE TOSS=0 INITIALLY
        toss=random.randint(0,1)
        toss=toss
        if(toss==0):       #ASSIGNING THE TOSS VALUE tO TOSS.
                print("Hurra!",name11,"won the toss|",name11," Please select your symbol")             
        else:
                print("Hurra!",name12,"won the toss|",name12," please select your symbol")       

def play_again():#ask for player to play again
        global board
        global modee
        global count
        print('Do you want to play again or exit?press y or Y/n or N:')
        print("-----------------------------------------------------------------------------")
        print('Press m or M to return in main_menu :')
        print("-----------------------------------------------------------------------------")
        num=input('')
        while num not in ['Y','y','m','M','N','n']:
                print("-----------------------------------------------------------------------------")
                print("Invalid choice")
                print("-----------------------------------------------------------------------------")
                num=input('')
                print("-----------------------------------------------------------------------------")
        if  num=='n' or num=="N":
                exit()
        elif    num=='y' or num=="Y":
                count=0             #it will make COUNT=0 which is nessary to play again
                                    #it will make variable OF BOARD change
                board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8]="-","-","-","-","-","-","-","-","-"
                if modee==1:
                        start_1()
                elif modee==2:
                        start_1()   #CALLING OF FUNCTION ACCORDING TO CHOICE
                elif modee==3:
                        start_1()
                elif modee==4:
                        start_4()
        elif num=="M" or num=="m":
                count=0            #it will make COUNT=0 which is nessary to play again
                board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8]="-","-","-","-","-","-","-","-","-"
                main_menu()
                play_again()
                
        else:
                exit()
        
                    
def win_check():                  #winnig_loss_draw check
        global count
        global modee

        if (board[0]==board[1]==board[2]=="O") or (board[3]==board[4]==board[5]=="O" ) or (board[6]==board[7]==board[8]=="O" ):
                print("-----------------------------------------------------------------------------")
                if modee==1 or modee==2 or modee==3:
                        print(name11,"has won the game")
                        print("-----------------------------------------------------------------------------")
                else:
                        print("player having symbol 'O' won the game" )
                print("-----------------------------------------------------------------------------")
                play_again()
        elif (board[0]==board[3]==board[6]=="O") or (board[1]==board[4]==board[7]=="O") or (board[2]==board[5]==board[8]=="O"):
                print("-----------------------------------------------------------------------------")
                if modee==1 or modee==2 or modee==3:
                        print(name11,"has won the game")
                        print("-----------------------------------------------------------------------------")
                else:
                        print("player having symbol 'O' won the game" )
                print("-----------------------------------------------------------------------------")
                play_again()
        elif (board[0]==board[4]==board[8]=="O") or (board[6]==board[4]==board[2]=="O"):
                print("-----------------------------------------------------------------------------")
                if modee==1 or modee==2 or modee==3:
                        print(name11,"has won the game")
                        print("-----------------------------------------------------------------------------")
                else:
                        print("player having symbol 'O' won the game" )
                print("-----------------------------------------------------------------------------")
                play_again()     #CALLING PLAYGAME FUNCTION AFTER DECSION
        
        if (board[0]==board[1]==board[2]=="X") or (board[3]==board[4]==board[5]=="X") or (board[6]==board[7]==board[8]=="X" ):
                print("-----------------------------------------------------------------------------")
                if modee==1 or modee==2 or modee==3:
                        print(name12,"has won the game")
                        print("-----------------------------------------------------------------------------")
                else:
                        print("player having symbol 'X' won the game" )
                print("-----------------------------------------------------------------------------")
                play_again()
        elif (board[0]==board[3]==board[6]=="X") or (board[1]==board[4]==board[7]=="X") or (board[2]==board[5]==board[8]=="X"):
                print("-----------------------------------------------------------------------------")
                if modee==1 or modee==2 or modee==3:
                        print(name12,"has won the game")
                        print("-----------------------------------------------------------------------------")
                else:
                        print("player having symbol 'X' won the game" )
                print("-----------------------------------------------------------------------------")
                play_again()
        elif (board[0]==board[4]==board[8]=="X") or (board[6]==board[4]==board[2]=="X"):
                print("-----------------------------------------------------------------------------")
                if modee==1 or modee==2 or modee==3:
                        print(name12,"has won the game")
                        print("-----------------------------------------------------------------------------")
                else:
                        print("player having symbol 'X' won the game" )
                print("-----------------------------------------------------------------------------")
                play_again()
        else:
                if count>=9: #WHEN MOVE ENDS GAME DRAW IF NO PLAYER WIN OR LOSS
                        print("-----------------------------------------------------------------------------")
                        print("Game Draw!")
                        print("-----------------------------------------------------------------------------")
                        play_again() #CALLING PLAY AGAIN FUNCTION
def hard_turn():                   #FUNCTION FOR HARD LEVEL
        global turn         #TO DEFINE WHAT IS TURN TO MAKE GLOBAL TURN IT WAS NECESSARY
        if (board[0]!="X" and  board[0]!="O"):
                turn="1"
        elif (board[2]!="X" and  board[2]!="O"):
                turn="3"
        elif (board[6]!="X" and  board[6]!="O"):
                turn="7"
        elif (board[8]!="X" and  board[8]!="O"):
                turn="9"
        else:
                turn=random.randint(1,9)
                turn=str(turn)
        return

def computer_turn_M():#MEDIUM LEVEL FUNCTION and Artifical Intelligence
        global turn
        if (board[0]=="O" and board[4]!="O"):
                turn="5"
        elif (board[1]=="O" and board[4]!="O"):
                turn="5"
        elif (board[2]=="O" and board[4]!="O"):
                turn="5"
        elif (board[3]=="O" and board[4]!="O"):
                turn="5"
        elif (board[4]=="O"):
                turn="9"
        elif (board[5]=="O" and board[4]!="O"):
                turn="5"
        elif (board[6]=="O" and board[4]!="O"):
                turn="5"
        elif (board[7]=="O" and board[4]!="O"):
                turn="5"
        elif (board[8]=="O" and board[4]!="O"):
                turn="5"
        else:
                turn=random.randint(1,9)
                turn=str(turn)
        return
def computer_turn(): #COMPUTER ARTIFICAL INTELLIGENSE
        global modee
        global turn
        global count

        if (board[2]=="X" and board[4]=="X" and board[6]!="O" or board[2]=="O" and board[4]=="O" and board[6]!="X" ):
                turn = "7"
        elif (board[0]=="X" and board[4]=="X" and board[8]!="O"  or  board[0]=="O" and board[4]=="O" and board[8]!="X"):
                turn ="9"  
        elif (board[0]=="X" and board[1]=="X" and board[2]!="O"  or  board[0]=="O" and board[1]=="O" and board[2]!="X"):
                turn = "3"  
        elif (board[3]=="X" and board[4]=="X" and board[5]!="O"  or  board[3]=="O" and board[4]=="O" and board[5]!="X"):
                turn = "6"
        elif (board[6]=="X" and board[7]=="X" and board[8]!="O"  or  board[6]=="O" and board[7]=="O" and board[8]!="X"):
                turn = "9"  
        elif (board[0]=="X" and board[3]=="X" and board[6]!="O"  or  board[0]=="O" and board[3]=="O" and board[6]!="X"):
                turn = "7"
        elif (board[6]=="X" and board[3]=="X" and board[0]!="O"  or  board[6]=="O" and board[3]=="O" and board[0]!="X"):
                turn = "1"
        elif (board[1]=="X" and board[4]=="X" and board[7]!="O"  or  board[1]=="O" and board[4]=="O" and board[7]!="X"):
                turn = "8"  
        elif (board[2]=="X" and board[5]=="X" and board[8]!="O"  or  board[2]=="O" and board[5]=="O" and board[8]!="X"):
                turn = "9"
        elif (board[0]=="X" and board[8]=="X" and board[4]!="O"  or  board[0]=="O" and board[8]=="O" and board[4]!="X"):
                turn = "5" 
        elif (board[2]=="X" and board[6]=="X" and board[4]!="O"  or  board[2]=="O" and board[6]=="O" and board[4]!="X"):
                turn = "5"  
        elif (board[0]=="X" and board[2]=="X" and board[1]!="O"  or  board[0]=="O" and board[2]=="O" and board[1]!="X"):
                turn = "2"  
        elif (board[3]=="X" and board[5]=="X" and board[4]!="O"  or  board[3]=="O" and board[5]=="O" and board[4]!="X"):
                turn = "5"  
        elif (board[6]=="X" and board[8]=="X" and board[7]!="O"  or  board[6]=="O" and board[8]=="O" and board[7]!="X"):
                turn = "8"  
        elif (board[0]=="X" and board[6]=="X" and board[3]!="O"  or  board[0]=="O" and board[6]=="O" and board[3]!="X"):
                turn = "4" 
        elif (board[1]=="X" and board[7]=="X" and board[4]!="O"  or  board[1]=="O" and board[7]=="O" and board[4]!="X"):
                turn = "5"  
        elif (board[2]=="X" and board[8]=="X" and board[5]!="O"  or  board[2]=="O" and board[8]=="O" and board[5]!="X"):
                turn = "6"
        elif (board[6]=="X" and board[3]=="X" and board[0]!="O"  or  board[6]=="O" and board[3]=="O" and board[0]!="X"):
                turn = "1"  
        elif (board[7]=="X" and board[4]=="X" and board[1]!="O"  or  board[7]=="O" and board[4]=="O" and board[1]!="X"):
                turn = "2"
        elif (board[7]=="X" and board[1]=="X" and board[4]!="O"  or  board[7]=="O" and board[1]=="O" and board[4]!="X"):
                turn = "5" 
        elif (board[8]=="X" and board[5]=="X" and board[2]!="O"  or  board[8]=="O" and board[5]=="O" and board[2]!="X"):
                turn = "3"  
        elif (board[2]=="X" and board[1]=="X" and board[0]!="O"  or  board[2]=="O" and board[1]=="O" and board[0]!="X"):
                 turn = "1"
        elif (board[5]=="X" and board[4]=="X" and board[3]!="O"  or  board[5]=="O" and board[4]=="O" and board[3]!="X"):
                turn = "4" 
        elif (board[8]=="X" and board[7]=="X" and board[6]!="O"  or  board[8]=="O" and board[7]=="O" and board[6]!="X"):
                turn = "7"        
        elif (board[4]=="X" and board[8]=="X" and board[0]!="O"  or board[4]=="O" and board[8]=="O" and board[0]!="X"):
                turn = "1"                
        elif (board[4]=="X" and board[6]=="X" and board[2]!="O"  or board[4]=="O" and board[6]=="O" and board[2]!="X"):
                turn = "3"
        else:
                if modee==3 and count==1:
                        computer_turn_M()
                elif modee==3 and count>1:
                        hard_turn()              #WHEN USER WILL PUT MODE NUM 3 THEN THIS FUNCTION WILL BE CALLED FOR HARD LEVEL
                elif modee==2:
                        computer_turn_M()        #WHEN USER WILL PUT MODE NUM 2 THEN THIS FUNCTION WILL BE CALLED FOR MEDIUM LEVEL
                else:
                        turn=random.randint(1,9)#IF NO CONDITION FULL FIL THEN WE WILL TAKE MOVE FROM RANDOM.RANDINT
                        turn=str(turn)          #CONVERSION INTEGER TO STRING
        return     
        print("-----------------------------------------------------------------------------")
  
def easy_mode():
        global modee
        global count
        global turn
        #ONLY FOR BETTER DISPLAY
        print("-----------------------WELCOME TO TIK TAK TOE GAME---------------------------")
        print('''-----------------------------INSTRUCTION:------------------------------------
Select your desire number in range(1-9) in given grid to replace it with your
symbol.if sequense will get match such as rows,coloums or diagonals have same
symbol then player which was able to put symbol in sequence will be a winner .''')
        print("                                                                             ")
        print("------------------------------Lets Play It-----------------------------------")
        print("                                                                             ")
        print("-------------------------ENTER THE PLAYERS NAME------------------------------")
        print("---------------------------------Then----------------------------------------")
        print("-----------------------CHOSE YOUR BOX FROM GIVEN GRID------------------------")
        if modee==2:#LEVEL NAMES ACCORDING TO LEVEL SELECTION
                print("--------------------------------MEDIUM LEVEL---------------------------------")
                start_1()
        elif modee==3:
                print("---------------------------------HARD LEVEL----------------------------------")
                start_1()
        else:
                print("--------------------------------EASY LEVEL-----------------------------------")
                start_1()
#START OF THE GAME            
def start_1():
        print("1","|","2","|","3")
        print('--+---+---')
        print("4","|","5","|","6")
        print('--+---+---')
        print("7","|","8","|","9")
        print("-----------------------------------------------------------------------------")
        play_easy_game()
#GAME WITH ALL LEVELS
def play_easy_game():
        global toss
        global board
        global name11
        global name12
        global n
        global count
        global name
        global modee
        global turn
        n=""
        name=True                   #INITIALIZE THE LOOP
        while   (name==True) or (name_a==True):
                o = input("Enter Player  name:")
                for i in range(58,128):#maximum two words name
                        while o in chr(i):
                                print("-----------------------------------------------------------------------------")
                                print("Please select Alphabatic Full name")
                                print("-----------------------------------------------------------------------------")
                                o = input("Enter Player name:")
                                print("-----------------------------------------------------------------------------")
                            
                name=o.isdigit()    #TO CHECK IF NAME HAS ONLY NUMBERS
                name_a=o.isspace()  #TO CHECK IF NAME HAS ONLY EMPTY SPACES
                if      name==True:
                        print("-----------------------------------------------------------------------------")
                        print('Name should not consist of only digits!')
                        print("-----------------------------------------------------------------------------")
                else:
                        name=False
                if      name_a==True: 
                        print("-----------------------------------------------------------------------------")
                        print('Name should not consist of only empty spaces!')
                        print("-----------------------------------------------------------------------------")
                        
                else:
                        name_a=False

                
                name11=o
                x = 'computer'
                name12=x
        for i in range(1,10):       #FOR LOOP THAT WILL TAKE MOVE ONE BY ONE 
            #player turn
            print("-----------------------------------------------------------------------------")
            print(name11," ITS YOUR TURN||YOUR SYMBOL IS ' - O - '")  #WHOES TURN
            print("-----------------------------------------------------------------------------")
            print("-----------------------------------------------------------------------------")
            #BOX SELECTION
            turn=input("Select the number in range (1-9) to replace it with your symbol :")
            print("-----------------------------------------------------------------------------")
            valid = False   #TO CHECK SPACE IN BOARD
            while not valid:
                    while  turn not in ['1','2','3','4','5','6','7','8','9']:#TO CHECK VALID NUMBER
                            print("-----------------------------------------------------------------------------")
                            #IF NUM NOT VALID THEN TRY AGAIN 
                            turn=input("Please Select the number in range (1-9) to replace it with your symbol :")
                            print("-----------------------------------------------------------------------------")
                            '''FOR EXAMPLE WHEN TURN CHOICE WILL 9 IT MAKE IT 8 THEN AT LIST INDEX 8 SYMBOL
                                            WILL BE PLACE AT ON CHOICE '''
                    turn=int(turn)-1      
                    if board[turn] == "-":
                            valid = True
                    else:
                            print("-----------------------------------------------------------------------------")
                            print('Space already occupied, try again on empty space!||again ',name11,'turn:')
                            print("-----------------------------------------------------------------------------")

            board[turn]="O"  #PUT 'O' IN CHOSEN BOX BY PLAYER
            print("-----------------------------------------------------------------------------")
            print(name11,"put 'O' in ",turn+1)#DEFINNIG THAT PLAYER CHOSE WHICH BOX.
            print("-----------------------------------------------------------------------------")
            display_board() #CALLING DISPLAY BOARD FUNCTION
            count+=1        #INCREMENT OF COUNT IN GLOBAL VARIABLE
            if count>=5:
                win_check()
            
            print("-----------------------------------------------------------------------------")
            print("ITS COMPUTER TURN||HAVING SYMBOL ' -X- '")#COMPUTER TURN
            computer_turn()
            
            valid = False        #AGAIN SPACE CHECK NOW FOR COMPUTER
            while not valid:
                    turn=int(turn)-1
                    if board[turn] == "-":
                            valid = True
                    else:
                            print("-----------------------------------------------------------------------------")
                            print('Space already occupied, try again on empty space!||again computer turn:')
                            print("-----------------------------------------------------------------------------")
            
            board[turn]="X"   #PUT 'X' IN CHOSEN BOX BY COMPUTER
            display_board()
            count+=1
            if count>=5:#WIN CHECK AFTER AND IN 5TH MOVE
                win_check() #CALLING FOR WIN CHECK TO CHECK IF ANYONE WIN OR LOSE.
#Double Player Mode                              
def double_player_mode():#DOUBLE PLAYER FUNCTION
    print("-----------------------WELCOME TO TIK TAK TOE GAME---------------------------")
    print('''-------------------------------INSTRUCTION:----------------------------------
Select your desire number in range(1-9) in given grid to replace it with your
symbol.if sequense will get match such as rows and coloums and diagonals have
same symbol then player which was able to put symbol in sequence will winner .''')
    print("                                                                             ")
    print("------------------------------Lets Play It-----------------------------------")
    print("                                                                             ")
    print("-------------------------ENTER THE PLAYERS NAME------------------------------")
    print("---------------------------------Then----------------------------------------")
    print("-----------------------CHOSE YOUR BOX FROM GIVEN GRID------------------------")
    print("------------------------------TWO PLAYER GAME--------------------------------")
    start_4()#FUNCTION FOR DUAL PLAYER MODE

def start_4():
        print("1","|","2","|","3")
        print('--+---+---')
        print("4","|","5","|","6")
        print('--+---+---')
        print("7","|","8","|","9")
        print("-----------------------------------------------------------------------------")
        play_p_p_game()

def play_p_p_game():
        global name_a 
        global name_b
        global name_2
        global toss
        global name11
        global name12
        global name
        global n
        global board
        global count
        global current_player   #IT HAVE VALUE ACCORDING TO PLAYER CHOSEN SYMBOL
        #i am going to check whether name is complete and have relative things
        while   (name==True or name_a==True):
                o = input("Enter 1st Player name:")
                for i in range(58,128): #maximum two word name
                        while o in chr(i):
                                print("-----------------------------------------------------------------------------")
                                print("Please select Alphabatic Full name")
                                print("-----------------------------------------------------------------------------")
                                o = input("Enter 1st Player name:")
                
                name=o.isdigit()
                if      name==True:
                        print("-----------------------------------------------------------------------------")
                        print('Name should not consist of only digits!')
                        print("-----------------------------------------------------------------------------")
                else:
                        name=False
                name_a=o.isspace()
                if      name_a==True:
                        print("-----------------------------------------------------------------------------")
                        print('Name should not consist of only empty spaces!')
                        print("-----------------------------------------------------------------------------")
                else:
                        name_a=False
                

                name11=o
                print("-----------------------------------------------------------------------------")

        while   (name_2==True or name_b==True):
                x = input("Enter 2nd Player name:")
                for i in range(58,128):
                        while x in chr(i):
                                print("-----------------------------------------------------------------------------")
                                print("Please select Alphabatic Full name")
                                print("-----------------------------------------------------------------------------")
                                x = input("Enter 2nd Player name:")
                
                name_2=x.isdigit()      #digit check in name
                if      name_2==True:
                        print("-----------------------------------------------------------------------------")
                        print('Name should not consist of only digits!')
                        print("-----------------------------------------------------------------------------")
                        
                else:
                        name_2=False
                name_b=x.isspace()      #space check in name
                if      name_b==True:
                        print("-----------------------------------------------------------------------------")
                        print('Name should not consist of only empty spaces!')
                        print("-----------------------------------------------------------------------------")
                        
                else:
                        name_b=False
                while o == x:       #name should be different
                        print('-----------------------------------------------------------------------------')
                        print('Name should be different.You can use digits after name to differentiate name')
                        print('-----------------------------------------------------------------------------')
                        x = input("Please again enter the 2nd Player name:")
                        print('-----------------------------------------------------------------------------')

                name12=x
                print("-----------------------------------------------------------------------------")
        Toss()  #CALLING TOSS FUNCTION    
        if toss==0:
                print("-----------------------------------------------------------------------------")
                print(name11,"its your turn||play with your First move")
                print("-----------------------------------------------------------------------------")
                print(name11,"Please chose your symbol!| if you want to be 'X' or 'O':")
                print("-----------------------------------------------------------------------------")
                current_player = input()
                while current_player not in ['O','o','X','x']:#SELECTION OF SYMBOL AND VALID CHOICE
                        print("-----------------------------------------------------------------------------")
                        print("Invalid Choice")
                        print("-----------------------------------------------------------------------------")
                        current_player = input()
        elif toss==1:
                print("-----------------------------------------------------------------------------")
                print(name12,"its your turn||play with your First move")
                print("-----------------------------------------------------------------------------")
                print(name12,"Please chose your symbol!| if you want to be 'X' or 'O':")
                print("-----------------------------------------------------------------------------")
                current_player = input()
                while current_player not in ['O','o','X','x']:#SELECTION OF SYMBOL AND VALID CHOICE
                        print("-----------------------------------------------------------------------------")
                        print("Invalid Choice")
                        print("-----------------------------------------------------------------------------")
                        current_player = input()
                
        for i in range(1,10):#IT WILL RUN 9 TIMES AND WILL TAKE 9 TURN
            #playerS turn
            print("-----------------------------------------------------------------------------")
            turn=input("Select the number in range (1-9) to replace it with your symbol :")
            print("-----------------------------------------------------------------------------")
            valid = False
            while not valid:
                    while  turn not in ['1','2','3','4','5','6','7','8','9']:
                            print("-----------------------------------------------------------------------------")
                            turn=input("Please Select the number in range (1-9) to replace it with your symbol :")
                            print("-----------------------------------------------------------------------------")
                    turn=int(turn)-1
                    if board[turn] == "-":
                            valid = True
                    else:
                            print("-----------------------------------------------------------------------------")
                            print('Space already occupied, try again on empty space!||again your turn:')
                            print("-----------------------------------------------------------------------------")

            if current_player == "X" or current_player == "x":  #CHANGE OF SYMBOL FROM 'X' TO 'O' OR 'O' TO 'X'
                board[turn]="X"
                print("-----------------------------------------------------------------------------")
                print("You put 'X' in ",turn+1)
                print("-----------------------------------------------------------------------------")
                current_player="O"
            elif current_player == "O" or current_player == "o":
                board[turn]="O"
                print("-----------------------------------------------------------------------------")
                print("You put 'O' in ",turn+1)
                print("-----------------------------------------------------------------------------")
                current_player="X"
            
            display_board()  #CALLING DISPLAY BOARD FUNCTION
            count+=1         #INCREMENT OF COUNT IN GLOBAL VARIABLE
            if count>=5:
                win_check()
main_menu()                  #CALLING MAIN FUNCTION                 
