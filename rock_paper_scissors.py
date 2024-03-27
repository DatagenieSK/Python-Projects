import random

user_point = 0
comp_point = 0

options = ['rock', 'paper', 'scissors']
user_input_shortcut = ['r', 'p', 's']

while True:
    user_input = input("Enter Rock, Paper and Scissors, or Q to Quit the game: ").lower()

    if user_input == 'q':
        print("Game Over")
        break

    if user_input not in options:
        print("Enter a Valid Choice")
        continue

    random_number = random.randint(0, 2)
    comp_choice = options[random_number]

    print(f"Your choice: {user_input.capitalize()}, Computer choice: {comp_choice.capitalize()}")


    if user_input == comp_choice:
        print("It's a tie!")
    else:
        if user_input == 'rock' and comp_choice == 'scissors':
            user_point += 1
        elif user_input == 'paper' and comp_choice == 'rock':
            user_point += 1
        elif user_input == 'scissors' and comp_choice == 'paper':
            user_point += 1
        else:
            comp_point += 1

    print(f"Your points: {user_point}, Computer points: {comp_point}")

    if user_point == 5:
        print('User Wins')
        break
    elif comp_point == 5:
        print('Computer Wins')
        break
    print(f"Total points of User is {user_point}")
    print(f"Total points of Computer is {comp_point}")
