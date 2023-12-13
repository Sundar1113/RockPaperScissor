import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice.lower(), computer_choice.lower())

    result_label.config(text=f"You chose {user_choice}.\nThe computer chose {computer_choice}.\nYou {result}!")

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x300")

result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.pack(pady=20)

choices = ['Rock', 'Paper', 'Scissors']

for choice in choices:
    tk.Button(root, text=choice, width=10, height=2, font=('Arial', 14), command=lambda c=choice: play_game(c)).pack(side=tk.LEFT, padx=10)

root.mainloop()
