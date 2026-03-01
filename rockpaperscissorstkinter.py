import tkinter as tk
import random
def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        result = f"It's a Tie! Both chose {user_choice}."
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = f"You Win! {user_choice} beats {computer_choice}."
    else:
        result = f"You Lose! {computer_choice} beats {user_choice}"
    result_label.config(text=result)
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
tk.Label(root, text="Choose your move:", font=("Arial", 14)).pack(pady=20)
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
for choice in ["Rock", "Paper", "Scissors"]:
    tk.Button(button_frame, text=choice, width=10, 
              command=lambda c=choice: play(c)).pack(side=tk.LEFT, padx=5)
result_label = tk.Label(root, text="Make a move to start!", font=("Arial", 12, "italic"), fg="blue")
result_label.pack(pady=30)
root.mainloop()
