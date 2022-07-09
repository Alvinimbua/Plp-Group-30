# Door lock system

import datetime 

current_time = datetime.datetime.now() 


set_password = input('Please set your password: ')
print('You have set your password successfully...')
print()

open = 'open'
close = 'close'
quit = 'quit'

while True:
    password = input('Enter your password: ')
    if password == set_password:
        print('Password entered successfully...')
        break
    else:
        print('Oops! Incorrect password. Try again.')
        continue


while True:
    open = False
    close = False
    quit = False

    cmd_1 = input('Enter your command: ')
    print()

    if cmd_1 == 'open':       
        print('The door is now open') 
        print('Door last open at ',current_time)
        time_now = datetime.datetime.now()
        open = True
        break

    elif cmd_1 == 'close':
        close = True
        print('The door is now closed')
        print('Door last closed at ',current_time)
        time_now = datetime.datetime.now()
        break

    elif cmd_1 == 'quit':
        quit = True
        break

    else:
        print('Invalid input')
        break


while True:
    if quit == True:
        print('You have logged out')
        break

    cmd_2  = input('Enter your command: ')
    print()

    if close == True and cmd_2 == 'close':
        print('The door is already locked')
        print('Door last closed at ',time_now)
        continue
        
    if cmd_2 == 'open' and open == True:       
        print('The door is already open')  
        print('Door last open  at ',time_now)
        continue

    if cmd_2 == 'close':
        print('The door is now closed')
        print('Door last closed at ',time_now)
        close = True
        continue

    elif cmd_2 == 'open':
        print('The door is now open')
        print('Door last open at ',time_now)
        continue
        open = True

    if cmd_2 == 'quit':
        print('You have logged out')
        break

    else:
        print('Invalid input')
        continue