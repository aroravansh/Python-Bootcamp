#from IPython.display import clear_output
import random
game_list=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def display(r1):
    #clear_output()
    print('\n'*100)
    print( '          |              |             ')
    print(f'    {r1[7]}     |      {r1[8]}       |     {r1[9]}  ')
    print( '          |              |             ')
    print( '---------------------------------------')
    print( '          |              |             ')
    print(f'    {r1[4]}     |      {r1[5]}       |     {r1[6]}  ')
    print( '          |              |             ')
    print( '---------------------------------------')
    print( '          |              |             ')
    print(f'    {r1[1]}     |      {r1[2]}       |     {r1[3]}  ')
    print( '          |              |             ')
      
def player_input():
    p1= ' '    
    while p1 not in ['X','O']:
            p1 = input('Player 1, do you want to be X or O? ')
            if p1 not in ['X','O']:
                print('Sorry! Enter a valid input')
    if p1=='X':
        p2='O'
    else:
        p2='X'
    return (p1,p2)

def place_mark(r1,mark,pos):
    r1[pos]=mark

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))     

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

     

    
    
    
    
    

print('                                     Tic Tac Toe')
print('                                     ***********')
print('\n \nHi! Welcome to tic tac toe board game')
print('Here you are going to entera valid input including row and position  ')
print('You win when you get your X or O three times consecutively straight or diagnally')
print('Good luck!!\n\n\n')
print('Available moves and positions are gives as:\n\n')
print('          |              |             ')
print('    7     |      8       |     9       ')
print('          |              |             ')
print('---------------------------------------')
print('          |              |             ')
print('    4     |      5       |     6       ')
print('          |              |             ')
print('---------------------------------------')
print('          |              |             ')
print('    1     |     2        |     3       ')
print('          |              |             ')
print('|n\n')
while True:
    # Reset the board
    game_list = [' '] * 10
    p1, p2 = player_input()
    turn = choose_first()
    print(turn + ' will go first.\n')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display(game_list)
            position = player_choice(game_list)
            place_mark(game_list, p1, position)

            if win_check(game_list, p1):
                display(game_list)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(game_list):
                    display(game_list)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display(game_list)
            position = player_choice(game_list)
            place_mark(game_list, p2, position)

            if win_check(game_list, p2):
                display(game_list)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(game_list):
                    display(game_list)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break