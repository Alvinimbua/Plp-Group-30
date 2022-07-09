# Personality Test Program

books_purchased = int(input('Enter number of books purchased this month: '))

if books_purchased == 0:
    print('You have been awarded 0 points')

elif books_purchased == 1:
    print('You have been awarded 6 points')

elif books_purchased == 2:
    print('You have been awarded 16 points')

elif books_purchased == 3:
    print('You have been awarded 32 points')

elif books_purchased >= 4:
    print('You have been awarded 60 points')

else:
    print('Oops! You have entered a negative number')