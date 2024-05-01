import tkinter as tk
from tkinter import messagebox
import random

# Define the new list of words and their rhymes
word_rhyme_pairs = {
    "love": ["dove", "glove", "above", "shove", "cove", "clove", "hove", "prove"],
    "rain": ["train", "pain", "gain", "lane", "spain", "brain", "strain", "grain", "reign", "crane", "chain"],
    "song": ["long", "strong", "gong", "wrong", "along", "thong", "mahjong"],
    "dream": ["cream", "stream", "scream", "steam", "team", "beam", "ream", "seem", "supreme", "extreme", "redeem", "scheme"],
    "tree": ["free", "three", "flee", "knee", "bee", "sea", "tea", "pee", "tee", "plea", "see"]
}

# Choose a random word and its rhymes from the list
target_word, rhymes = random.choice(list(word_rhyme_pairs.items()))

# Initialize the list of guessed rhymes
guessed_rhymes = []

# Initialize the number of guesses
guesses_left = 6

# Create the main window
root = tk.Tk()
root.title("Hangman - Guess the Rhymes")

# Create the canvas for drawing the hangman
canvas = tk.Canvas(root, width=300, height=300)
canvas.grid(column=0, row=0)

# Draw the scaffold
canvas.create_line(20, 280, 120, 280)
canvas.create_line(70, 280, 70, 20)
canvas.create_line(70, 20, 170, 20)
canvas.create_line(170, 20, 170, 50)

# Create a label for displaying the word to rhyme
word_label = tk.Label(root, text="Rhymes with: {}".format(target_word))
word_label.grid(column=0, row=1)

# Create a label for displaying the number of guesses remaining
guesses_label = tk.Label(root, text="Guesses remaining: {}".format(guesses_left))
guesses_label.grid(column=0, row=2)

# Create a label for displaying the letters guessed so far
guessed_label = tk.Label(root, text="Guessed rhymes: ")
guessed_label.grid(column=0, row=3)

# Create an entry for the user to guess a rhyme
rhyme_entry = tk.Entry(root)
rhyme_entry.grid(column=0, row=4)

# Display a message indicating that the player needs to guess 2 rhyming words to win
messagebox.showinfo("Hangman - Guess the Rhymes", "You're about to play a guess the rhyme made by Aldrin & Peter")

messagebox.showinfo("Hangman - Guess the Rhymes", "Guess two rhyming words to win the game! Goodluck!")

messagebox.showinfo("Hangman - Guess the Rhymes", "Start")

# Define a function to check the user's rhyme guess
def check_rhyme():
    global guesses_left

    guess = rhyme_entry.get().lower()
    rhyme_entry.delete(0, tk.END)

    # Check if the guess is correct
    if guess in rhymes:
        if guess not in guessed_rhymes:
            guessed_rhymes.append(guess)
            guessed_label.config(text="Guessed rhymes: {}".format(", ".join(guessed_rhymes)))
            if len(set(guessed_rhymes)) == 2:  # Check if the player has guessed two unique rhymes
                messagebox.showinfo("Hangman - Guess the Rhymes", "Congratulations! You guessed two rhymes correctly! \n You WON!")
                exit_game()
        else:
            messagebox.showinfo("Hangman - Guess the Rhymes", "You already guessed this rhyme!")
    else:
        guesses_left -= 1
        update_hangman()
        guesses_label.config(text="Guesses remaining: {}".format(guesses_left))
        if guesses_left == 0:
            messagebox.showinfo("Hangman - Guess the Rhymes", "You ran out of guesses! The word was '{}'".format(target_word))
            exit_game()


def update_hangman():
    # Draw the hangman based on remaining guesses
    if guesses_left == 5:
        canvas.create_oval(140, 50, 200, 110)
    elif guesses_left == 4:
        canvas.create_line(170, 110, 170, 170)
    elif guesses_left == 3:
        canvas.create_line(170, 130, 140, 140)
    elif guesses_left == 2:
        canvas.create_line(170, 130, 200, 140)
    elif guesses_left == 1:
        canvas.create_line(170, 170, 140, 190)
    elif guesses_left == 0:
        canvas.create_line(170, 170, 200, 190)


def exit_game():
    root.destroy()


root.bind("<Return>", lambda event: check_rhyme())

root.mainloop()
