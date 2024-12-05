from random import choice
from hangman_data import words, hangman_art


def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hint):
    print(f"\n| {" ".join(hint)} |\n")


def display_answer(answer):
    print(f"\nCorrect answer was: <  {" ".join(answer)}  >")


def main():
    answer = choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Type in your guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(
                "\nInvalid input! Your guess should be one string character at a time!\n")

            continue

        if guess in guessed_letters:
            print("\nYou already typed in that letter!\n")

            continue
        else:
            guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("\nYOU LOSE!\n")
            is_running = False
        elif "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("\n!!! YOU WIN !!!\n")
            is_running = False


if __name__ == "__main__":
    main()
