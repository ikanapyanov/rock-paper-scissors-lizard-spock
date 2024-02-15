import tkinter as tk
from tkinter import messagebox
import random

# Game rules
def play_game(user_choice, sheldon_choice):
    if user_choice == sheldon_choice:
        return "It's a tie!", None
    elif (user_choice == 'rock' and sheldon_choice in ['scissors', 'lizard']) or \
         (user_choice == 'paper' and sheldon_choice in ['rock', 'spock']) or \
         (user_choice == 'scissors' and sheldon_choice in ['paper', 'lizard']) or \
         (user_choice == 'lizard' and sheldon_choice in ['spock', 'paper']) or \
         (user_choice == 'spock' and sheldon_choice in ['rock', 'scissors']):
        return "You win!", 'player'
    else:
        return "Sheldon wins. Bazinga!", 'sheldon'

def choose(option):
    user_choice = option
    global player_wins, sheldon_wins
    sheldon_choice = random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])
    winner_msg, winner = play_game(user_choice, sheldon_choice)
    if winner == 'player':
        player_wins += 1
    elif winner == 'sheldon':
        sheldon_wins += 1
    messagebox.showinfo("Result", f"Sheldon chose {sheldon_choice}\n{winner_msg}\n\nPlayer wins: {player_wins}\nSheldon wins: {sheldon_wins}")

# Creates the app window
root = tk.Tk()
root.title("Rock-Paper-Scissors-Lizard-Spock")
label = tk.Label(root, text="Select your choice:", font=("Helvetica", 14))
label.pack(pady=10)

# Creates interactable buttons for the user
player_wins = 0
sheldon_wins = 0
choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
for choice in choices:
    button = tk.Button(root, text=choice.capitalize(), font=("Helvetica", 12), width=10, height=2,
                       command=lambda c=choice: choose(c))
    button.pack(pady=5)

root.mainloop()