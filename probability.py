import random

def roll_dice(num_rolls, sides):
    outcomes = []
    for _ in range(num_rolls):
        outcome = random.randint(1, sides)
        outcomes.append(outcome)
    return outcomes

def flip_coin(num_flips):
    outcomes = []
    for _ in range(num_flips):
        outcome = random.choice(['Heads', 'Tails'])
        outcomes.append(outcome)
    return outcomes

def draw_cards(num_draws, deck_size):
    deck = list(range(1, deck_size + 1))
    outcomes = random.sample(deck, num_draws)
    return outcomes

def main():
    print("Welcome to the Probability Calculator!")

    while True:
        print("\nSelect an option:")
        print("1. Roll Dice" )
        print("2. Flip Coin")
        print("3. Draw Cards")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            num_rolls = int(input("Enter the number of dice rolls: "))
            sides = int(input("Enter the number of sides on the dice: "))
            outcomes = roll_dice(num_rolls, sides)
            print("Outcomes:", outcomes)

        elif choice == '2':
            num_flips = int(input("Enter the number of coin flips: "))
            outcomes = flip_coin(num_flips)
            print("Outcomes:", outcomes)

        elif choice == '3':
            num_draws = int(input("Enter the number of card draws: "))
            deck_size = int(input("Enter the size of the deck: "))
            outcomes = draw_cards(num_draws, deck_size)
            print("Outcomes:", outcomes)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()