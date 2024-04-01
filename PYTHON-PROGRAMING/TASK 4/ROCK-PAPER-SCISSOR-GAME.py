import tkinter as tk
import random

def play():
    global games_played, wins, losses
    games_played += 1
    
    # Get the player's choice
    player_choice = player_choice_var.get()

    # Generate computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Update computer's choice label
    computer_choice_var.set(f"Computer chose: {computer_choice.capitalize()}")

    # Determine the winner
    if player_choice == computer_choice:
        result_var.set("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result_var.set("You win!")
        wins += 1
    else:
        result_var.set("Computer wins!")
        losses += 1

    # Update statistics label
    update_stats()

def update_stats():
    stats_label.config(text=f"Games Played: {games_played}\nWins: {wins}\nLosses: {losses}")

def reset_stats():
    global games_played, wins, losses
    games_played = 0
    wins = 0
    losses = 0
    update_stats()

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Create a frame to contain widgets
frame = tk.Frame(window, bg="lightblue", padx=20, pady=20)
frame.pack()

# Label for player's choice
player_label = tk.Label(frame, text="Your choice:", font=("Arial", 16), bg="lightblue")
player_label.grid(row=0, column=0, padx=10, pady=10)

# Radio buttons for player's choice
player_choice_var = tk.StringVar()
player_choice_var.set("rock")

rock_button = tk.Radiobutton(frame, text="Rock", variable=player_choice_var, value="rock", font=("Arial", 14), bg="lightblue")
rock_button.grid(row=0, column=1, padx=10, pady=10)

paper_button = tk.Radiobutton(frame, text="Paper", variable=player_choice_var, value="paper", font=("Arial", 14), bg="lightblue")
paper_button.grid(row=0, column=2, padx=10, pady=10)

scissors_button = tk.Radiobutton(frame, text="Scissors", variable=player_choice_var, value="scissors", font=("Arial", 14), bg="lightblue")
scissors_button.grid(row=0, column=3, padx=10, pady=10)

# Button to play
play_button = tk.Button(frame, text="Play", font=("Arial", 14), command=play)
play_button.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Label to display computer's choice
computer_choice_var = tk.StringVar()
computer_choice_label = tk.Label(frame, textvariable=computer_choice_var, font=("Arial", 14), bg="lightblue")
computer_choice_label.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Label to display result
result_var = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_var, font=("Arial", 14), bg="lightblue")
result_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

# Button to reset
reset_button = tk.Button(frame, text="Reset", font=("Arial", 14), command=reset_stats)
reset_button.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

# Label to display statistics
games_played = 0
wins = 0
losses = 0
stats_label = tk.Label(frame, text=f"Games Played: {games_played}\nWins: {wins}\nLosses: {losses}", font=("Arial", 14), bg="lightblue")
stats_label.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# Exit button
exit_button = tk.Button(frame, text="Exit", font=("Arial", 14), command=window.quit)
exit_button.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

# Run the application
window.mainloop()
