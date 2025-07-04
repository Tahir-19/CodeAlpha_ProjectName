import random

words = ["apple", "banana", "grape", "orange", "peach"]

word = random.choice(words)
guessed = ["_"] * len(word)
guessed_letters = []
tries = 6

print("Welcome to Hangman!")
print("Guess the word: " + " ".join(guessed))

while tries > 0 and "_" in guessed:
    guess = input("Guess a letter: ").lower()
    
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("Good guess!")
    else:
        tries -= 1
        print(f"Wrong! You have {tries} tries left.")

    print(" ".join(guessed))

if "_" not in guessed:
    print("Congratulations! You guessed the word:", word)
else:
    print("Sorry, you lost. The word was:", word)