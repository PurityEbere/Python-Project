import random
roll_count = 0
playing  = True
while playing:
    choice = input('Roll the dice? (Y/N): ').upper()

    if choice == 'Y' or choice == 'YES':
        times = input('How many times do you want to roll the dice?\n')

        if times == "":
            print('You did not enter any number.')
        else:
            times = int(times)
            for i in range(times):
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                print(f'Roll {i + 1}: ({dice1}, {dice2})')
                roll_count += 1
                print(f"You have rolled the dice {roll_count} times.\n")

    elif choice == 'N' or choice == 'NO':
        print('Thank you for playing the game!')
        break

    else:
        print('Invalid choice. Please enter Y or N.')
