import random
from ascii_art import STAGES

# Liste geheimer Wörter
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Wählt ein zufälliges Wort aus der Liste aus."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def is_word_guessed(secret_word, guessed_letters):
    """Überprüfen Sie, ob alle Buchstaben des geheimen Wortes erraten wurden."""
    return all(letter in guessed_letters for letter in secret_word)


def display_game_state(mistakes, secret_word, guessed_letters):
    """ Zeigt den aktuellen Schneeman und den bisherigen Fortschritt im Wort"""
    print(STAGES[mistakes])
    display_word = " ".join(
        [letter if letter in guessed_letters else "_" for letter in secret_word]
    )
    print(f"Word: {display_word}")
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    if guessed_letters:
        print("Guessed:", " ".join(sorted(guessed_letters)))
    else:
        print("Guessed: -")
    print()


def play_game():
    """Hauptspielschleife mit Ratelogik und Gewinn - / Verlustbedingungen."""
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")
    print(f"(debug) Secret word: {secret_word}")

    # Erster Spielzustand anzeigen
    display_game_state(mistakes, secret_word, guessed_letters)

    # Schleife bis zum Sieg oder zur Niederlage
    while mistakes < max_mistakes and not is_word_guessed(secret_word, guessed_letters):
        guess = input("Guess a letter: ").lower().strip()

        # Basisvalidierung: einzelner Buchstabe von A bis Z
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.\n")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Nice! That letter is in the word.\n")
        else:
            mistakes += 1
            print("Nope! That letter is not in the word.\n")

        display_game_state(mistakes, secret_word, guessed_letters)

    # Ende des Spiels
    if is_word_guessed(secret_word, guessed_letters):
        print("You saved the snowman!")
    else:
        print("Oh no! The snowman melted.")
        print(f"The word was: {secret_word}")

def main():
    """Startet das Spiel und fragt nach Replay."""
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower().strip()
        if again != "y":
            print("Goodbye! Thanks for playing Snowman Meltdown!")
            break
