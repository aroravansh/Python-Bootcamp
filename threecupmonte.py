from random import shuffle
mylist =['','O','']
def shuffle_list(mylist):
     shuffle(mylist)    
     return mylist
def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess= input('Enter your guess in cup 0,1 or 2 ')
    return int(guess)  
def guess_check(mylist,guess):
    if mylist[guess]=='O':
        print('Correct Cup!!')
    else:
        print(f'Wrong!! the currect cup is {mylist}')

print('Welcome to Three Cup Monte game!')
print('Here you have to guess in which cup the O is ')
print('You only get one chance so guess wisely')
list2= shuffle_list(mylist)
ans= player_guess()
guess_check(list2, ans)