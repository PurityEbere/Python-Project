import random

min_value = int(input('Enter a minimum value: '))
max_value = int(input('Enter a maximum value: '))
guess_count = 0
number_to_guess = random.randint(min_value, max_value)

while True:
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
