import random

print("I am guessing a number between 1 to 100")

choice = input("Choose the difficulty. 'easy' or 'hard': ").lower()

a = random.randint(1, 100)

if choice == 'easy':
    no_of_times = 10
else:
    no_of_times = 5


def asking():
    global no_of_times
    global a

    for i in range(no_of_times):
        try:
            user_choice = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        print(f"No of guesses left: {no_of_times - i - 1}")

        if user_choice == a:
            print("🎉 Your guess was correct!")
            return
        elif user_choice > a:
            print("Too high")
        else:
            print("Too low")

    print(f"❌ You ran out of guesses. The number was {a}")


asking()