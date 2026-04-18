import random


def play():
    secret = random.randint(1, 20)
    attempts = 0

    print("I'm thinking of a number between 1 and 20.")

    while True:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Correct! It took you {attempts} tries.")
            break


if __name__ == "__main__":
    play()
