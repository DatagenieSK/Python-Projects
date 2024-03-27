import random
winning_num = random.randrange(0,11)
count = 0

while True:
    guess = int(input('Enter your guess between 1 to 10\n> '))
    if guess == winning_num:
        print('You Win')
        break
    elif guess != winning_num:
        count +=1
        if count == 3:
            print(f"The Number to Win is {winning_num}")
            print('You Lose')
            break
        print('Try Again')