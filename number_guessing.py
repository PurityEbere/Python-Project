
import random

min_value = int(input('Enter a minimum value: '))
max_value = int(input('Enter a maximum value: '))
max_attempts = int(input('Enter the maximum number of attempts allowed: '))
guess_count = 0
number_to_guess = random.randint(min_value, max_value)

while guess_count < max_attempts:
    try:
        guess = int(input(f'Guess the number between {min_value} and {max_value}: '))
        guess_count += 1 
        if guess < number_to_guess:
            print('Too low! Try again.')
        elif guess > number_to_guess:
            print('Too high! Try again.')
        else:
            print(f'You guessed it! Smart guess! It took you {guess_count} attempts.\n')
            break  
    except ValueError:
        print("Invalid input. Please enter a valid number.")
else:
    if guess_count > 1:
        print(f'Game over my gee, you have used all {max_attempts} attempts. The correct number was {number_to_guess}.')
    else:
       print(f"Game over! You've used all attempts")