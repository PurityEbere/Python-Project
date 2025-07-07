import random

Rock = 'r'
Paper = 'p'
Scissors = 's'

emojis = {Rock: '🪨', Paper: '📃', Scissors: '✂'}
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        user_choice = input('Rock, Paper or Scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice')


def display_choice(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif (
        (user_choice == Rock and computer_choice == Scissors) or
        (user_choice == Scissors and computer_choice == Paper) or
        (user_choice == Paper and computer_choice == Rock)
    ):
        print('You win!')
    else:
        print('You lose!')


def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choice(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        play_again = input(
            'Do you want to play again? (yes/no): '
        ).strip().lower()
        if play_again != 'yes':
            print('Thanks for playing! Goodbye!')
            break
play_game()
