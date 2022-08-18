import random

print("Let's play rock, paper, scissors.")


while True:
    def play():
        user = input("[r] for rock, [p] for paper, [s] for scissors: ")
        user = user.lower()
        if user != 'r' and user != 'p' and user != 's':
            print("Wrong choice!")

        else:
            computer = random.choice(['r', 'p', 's'])
            print("I chose, ", computer, " !")

            if user == computer:
                return 'Draw!'

            elif is_win(user, computer):
                return 'You win!'

            elif is_win(computer, user):
                return 'You lost!'


    def is_win(pl, op):
        if (pl == 'r' and op == 's') or (pl == 's' and op == 'p') or (pl == 'p' and op == 'r'):
            return True


    print(play())
    next_calculation = input("\nLet's play another game? (yes/no): ")
    if next_calculation == "no":
        break
    elif next_calculation != "yes" and next_calculation != "no":
        print("Invalid input!")
        break
