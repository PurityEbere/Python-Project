import random

Rock = 'r'
Paper = 'p'
Scissors = 's'
Player = 'p'
Computer = 'c'

emojis = {Rock: '🪨', Paper: '📃', Scissors: '✂'}
choices = tuple(emojis.keys())
mode = (Computer, Player)


def determine_mode():
    while True:
        players_choice = input("Play against computer or player? (c/p): ")
        if players_choice in mode:
            return players_choice
        else:
            print('Select a mode')


def get_user_choice(player_name):
    while True:
        user_choice = input(
            f'{player_name} - Rock, Paper or Scissors? (r/p/s): '
        ).lower()
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
        return 'user'
    else:
        print('You lose!')
        return 'computer'


def play_game():
    total_wins = 0
    total_losses = 0
    total_ties = 0

    mode = determine_mode()

    while True:
        user_wins = 0
        computer_wins = 0

        for _ in range(3):
            if mode == 'c':
                user_choice = get_user_choice('You')
                computer_choice = random.choice(choices)
            else:
                user_choice = get_user_choice('Player 1')
                computer_choice = get_user_choice('Player 2')

            display_choice(user_choice, computer_choice)
            result = determine_winner(user_choice, computer_choice)

            if result == 'player':
                user_wins += 1
                total_wins += 1
            elif result == 'computer':
                computer_wins += 1
                total_losses += 1
            else:
                total_ties += 1

            print(
                f'Score -> You: {user_wins} | '
                f'Computer: {computer_wins}'
            )

        if user_wins > computer_wins:
            print('You are the overall winner!')
        elif computer_wins > user_wins:
            print('Computer is the overall winner!')
        else:
            print("It's an overall tie!")

        play_again = input(
            'Do you want to play again? (yes/no): '
        ).strip().lower()
        if play_again != 'yes':
            print('Thanks for playing! Goodbye!')
            print(
                f'Total wins: {total_wins} | '
                f'Total losses: {total_losses} | '
                f'Total ties: {total_ties}'
            )
            break


play_game()
