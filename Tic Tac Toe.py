#Tic Tac Toe Game(Python), Created by Jiajing Qi, revised 05/30/2021

import os 

#Dict holds Tic Tac Toe data 
Tic_Tac = {'1':'   ' , '2':'   ', '3':'   ',
'4':'   ', '5':'   ', '6':'  ',
'7':'   ','8':'   ','9':'   '}

# Display Tic Tac Toe
def display():
    print ('{}|{}|{}'.format(Tic_Tac['1'],Tic_Tac['2'],Tic_Tac['3']))
    print('-----------')
    print ('{}|{}|{}'.format(Tic_Tac['4'],Tic_Tac['5'],Tic_Tac['6']))
    print('-----------')
    print ('{}|{}|{}'.format(Tic_Tac['7'],Tic_Tac['8'],Tic_Tac['9']))

# Clear the output
def clearscreen ():
    os.system('cls')

#  Illustrate the game rule
def rule():
      print("""Welcome to Tic Tac Toe Game, 2 Players are required.
Following is the position index that players will choose when game starts.
1 | 2 | 3|
----------
4 | 5 | 6| 
----------
7 | 8 | 9|\n """)

# Start the game
def start_game(Rest):
    userint = input('Would you like to {} the game, Y or N?'.format(Rest)).upper().replace(' ','')
    if userint.isalpha()== True and userint in ['Y']:
        return userint
    elif userint.isalpha()== True and userint in ['N']:
        print('--Sorry to see you go, we could have fun!')
    else:
        print("--Sorry, I do not understand. Let's try again\n")
        start_game()

# Assign unique symbol to each player
def assign_player():
    Player1_Sym = '0'
    Player_name= ['X','O']
    while Player1_Sym.isalpha() == False:
        Player1_Sym = input("Choose symbol 'X' or 'O' as player1: ").upper()
        if Player1_Sym.isalpha() == True and Player1_Sym in Player_name:
            print('Player1 is {} '.format(Player1_Sym))
            Player_name.remove(Player1_Sym)
            Player2_Sym = Player_name[0]
            print('Player2 is {} '.format(Player2_Sym))         
            return Player1_Sym,Player2_Sym
        else:
            Player1_Sym = '0'
            clearscreen()
            print("Oops, :(, Please choose either 'X' or 'O' as the player's name.\nLet us try again. \n ")

# Accept user input and check if anyone wins the game
def user_choice(P1,P2,players_pos,player_counter):  
    #player1 input
    while len(player_counter) ==0:
        player1_pos = int(input('Player1, please enter a postion index : '))
        if player1_pos in range(1,10) and player1_pos not in players_pos:
            clearscreen()
            Tic_Tac[str(player1_pos)] = P1
            players_pos.append(player1_pos)
            player_counter.append(1)
            display()         
        else:
            print('Oops, that is not a valid position index. Please try again')
            pass
        #Check if player1 wins
        Result = check_if_win(players_pos)
        if Result == True:
            print ('Player1 WIN!!')
            #Exit game
            player_counter = ['Game','Over']
        elif Result == 'Tie':
            print('The game ended in a standoff!')
            player_counter = ['Game','Tie']
            Rest = 'restart'
            start_game(Rest)
            

    #player2 input    
    while len(player_counter) == 1:
        player2_pos = int(input('Player2, please enter a postion index : '))
        if player2_pos in range(1,10) and player2_pos not in players_pos:
            clearscreen()
            Tic_Tac[str(player2_pos)] = P2
            players_pos.append(player2_pos)
            display()
            player_counter.clear()
        else:
            print('Oops, that is not a valid position index. Please try again')
            pass
        #Check if player2 wins
        Result = check_if_win(players_pos)
        if Result == True:
            print ('Player2 WIN!!')
            #Exit game
            player_counter = ['Game','Over']
        elif Result == 'Tie':
            print('The game ended in a standoff!')
            player_counter = ['Game','Tie']
            Rest = 'restart'
            start_game(Rest)
            
# Check if win logic
def check_if_win(players_pos):
    Player_name= ['X','O'] # Restate
    current_val = []
    for x in Tic_Tac.values():       
        current_val.append(x.replace(' ',''))
    if len(set(current_val [:3])) == 1 and current_val[0]in Player_name:
        return True
    elif len(set(current_val [3:7])) == 1 and current_val [3]in Player_name:
        return True
    elif len(set(current_val [6:])) == 1 and current_val [6]in Player_name:
        return True
    elif len(set(current_val [::3])) == 1 and current_val [0]in Player_name:
        return True
    elif len(set(current_val [1::3])) == 1 and current_val [1]in Player_name:
        return True
    elif len(set(current_val [2::3])) == 1 and current_val [2]in Player_name:
        return True
    elif len(set(current_val [::4])) == 1 and current_val [0]in Player_name:
        return True
    elif len(set(current_val [2:8:2])) == 1 and current_val [2]in Player_name:
        return True
    elif len(players_pos) == 10:
        return 'Tie'
    else:
        return False       

#Main loop
Win = False
players_pos = [0]
Rest = 'start'
clearscreen()
rule()
if start_game(Rest) == 'Y' :
    players = assign_player()
    P1 = ' '+ players[0] + ' '  # P1 is player1's sym
    P2 = ' '+ players[1] + ' ' # P2 is player2's sym
    #after display players' symbol, give it a line before showing Tic Tac Toe
    print('\n') 
    display()
    player_counter = []
    while Win == False and len(player_counter) ==0:
        user_choice(P1,P2,players_pos,player_counter)
