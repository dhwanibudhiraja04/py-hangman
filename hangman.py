from time import sleep
import pwinput

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
         "S", "T", "U", "V", "W", "X", "Y", "Z", " "]

stages = [
    """
       --------
       |      |
       |      
       |    
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |     \|
       |      |
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |     \|/
       |      |
       |     
       -
    """,
    """
       --------
       |      |
       |      O
       |     \|/
       |      |
       |     / 
       -
    """,
    """
       --------
       |      |
       |      O
       |     \|/
       |      |
       |     / \\
       -
    """
]


print("------------------------HANGMAN GAME--------------------------")
sleep(1)
player1 = input("Enter the name of Player 1: ")
player2 = input("Enter the name of Player 2: ")


def play1():
    global word1, revealed
    w1 = pwinput.pwinput(f"Enter a word {player1}: ")
    word1 = []
    revealed = []
    for i in w1:
        if i in alpha:
            word1.append(i)
            revealed.append('_')
        else:
            print("Input Invalid. Try again!")
            play1()

    for i in word1:
        if i == ' ':
            print('  ', end="")
        else:
            print("'_'", end="")
    sleep(2)
    print("")
    print(f"{player2} has 6 tries to guess the word correctly.")
    print("Setting up your hangman...")
    sleep(4)
    print("""
        --------
        |      
        |      
        |    
        |      
        |     
        -
       """)


play1()

incorrect_guesses = 0

while '_' in revealed and incorrect_guesses < len(stages):
    guess = input("Enter your guess here: ")
    sleep(1)
    correct_guess = False
    for index, letter in enumerate(word1):
        if guess == letter:
            revealed[index] = letter
            correct_guess = True

    for i in range(len(revealed)):
        if revealed[i] == ' ':
            print(' ', end='')
        else:
            print(revealed[i], end=' ')
    print()

    if not correct_guess:
        incorrect_guesses += 1
        print("Oops! Try Again.")
        print(stages[incorrect_guesses - 1])
        sleep(1)
        print(f"You have {len(stages) - incorrect_guesses} more guesses left.")

if '_' not in revealed:
    print("Congratulations! You guessed the word correctly.")
    print("GAME OVER.")
else:
    print("You loose. GAME OVER.")
    

    

