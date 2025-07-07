import random

best_score = None

while True:
    min_value = int(input('Enter a minimum value: '))
    max_value = int(input('Enter a maximum value: '))
    max_attempts = int(input('Enter the maximum number of attempts allowed: '))
    guess_count = 0
    number_to_guess = random.randint(min_value, max_value)

    while guess_count < max_attempts:
        try:
            guess = int(input(
                (
                    f'Guess the number between {min_value} and {max_value}: '
                )
            ))
            guess_count += 1
            if guess < min_value:
                print('You are below the minimum value.')
            elif guess > max_value:
                print('You are above the maximum value.')
            elif guess > number_to_guess:
                print('Too high! Try again.')
            elif guess < number_to_guess:
                print('Too low! Try again.')
            else:
                print(f'You guessed it! Smart guess! It took you {guess_count} attempts.\n')

                if best_score is None or guess_count < best_score:
                    best_score = guess_count
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print(f"Game over! You've used all {max_attempts} attempts. The correct number was {number_to_guess}.")

    if best_score is not None:
        print(f"The best score so far is {best_score} attempts.")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        print("Let's play again, hun.")
    else:
        print("Thanks for playing! Goodbye!")
        break