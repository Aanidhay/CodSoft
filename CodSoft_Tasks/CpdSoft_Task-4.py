import tkinter as tk
from random import choice

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock-Paper-Scissors")
        self.window.geometry("300x400")
        self.user_score = 0
        self.computer_score = 0
        self.game_history = []

        self.label = tk.Label(self.window, text="Choose your move:", font=("Arial", 16))
        self.label.pack()

        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack()

        self.rock_button = tk.Button(self.button_frame, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.window, text="Reset", command=self.reset)
        self.reset_button.pack(pady=10)

        self.result_label = tk.Label(self.window, text="", font=("Arial", 16))
        self.result_label.pack()

        self.score_label = tk.Label(self.window, text=f"Score - You: {self.user_score}, Computer: {self.computer_score}", font=("Arial", 16))
        self.score_label.pack()

        self.history_label = tk.Label(self.window, text="Game History:", font=("Arial", 16))
        self.history_label.pack()

        self.history_text = tk.Text(self.window, height=10, width=30)
        self.history_text.pack()

    def play(self, user_choice):
        computer_choice = choice(["rock", "paper", "scissors"])
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1

        self.result_label.config(text=f"You chose: {user_choice}, Computer chose: {computer_choice}, {result}")
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")
        self.game_history.append(f"You chose: {user_choice}, Computer chose: {computer_choice}, {result}")
        self.history_text.insert(tk.END, f"You chose: {user_choice}, Computer chose: {computer_choice}, {result}\n")

    def reset(self):
        self.user_score = 0
        self.computer_score = 0
        self.game_history = []
        self.result_label.config(text="")
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")
        self.history_text.delete(1.0, tk.END)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()