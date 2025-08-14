import random

# Liste geheimer Wörter
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII-Art-Stufen
STAGES = [
    # Stufe 0: Vollständiger Schneemann
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
    """,
    # Stufe 1: Unterer Teil schmilzt
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
    """,
    # Stufe 2: Nur der Kopf bleibt
    """
      ___  
     /___\\ 
     (o o) 
    """,
    # Stufe 3: Schneemann komplett geschmolzen
    """
      ___  
     /___\\ 
    """
]

def display_game_state(mistakes, secret_word, guessed_letters):
    """ Zeigt den aktuellen Schneeman und den bisherigen Fortschritt im Wort"""
    print(STAGES[mistakes])
    display_word = " ".join(
        [letter if letter in guessed_letters else "_" for letter in secret_word]
    )
    print(display_word)




def get_random_word():
    """Wählt ein zufälliges Wort aus der Liste aus."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # Zum Testen, später entfernen

    # Erster Spielzustand anzeigen
    display_game_state(mistakes, secret_word, guessed_letters)

    # Für jetzt einfach einmal den Benutzer fragen:
    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)


if __name__ == "__main__":
    play_game()