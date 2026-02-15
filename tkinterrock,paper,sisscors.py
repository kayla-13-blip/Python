import tkinter as tk
import random
def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win! 🎉"
    else:
        result = "Computer Wins! 💻"
    user_label.config(text=f"Your Choice: {user_choice}")
    comp_label.config(text=f"Computer Choice: {computer_choice}")
    result_label.config(text=result)
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
tk.Label(root, text="Choose Your Move:", font=("Arial", 14, "bold")).pack(pady=10)
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
for choice in ["Rock", "Paper", "Scissors"]:
    tk.Button(btn_frame, text=choice, width=10, 
              command=lambda c=choice: play(c)).pack(side="left", padx=5)
user_label = tk.Label(root, text="Your Choice: ", font=("Arial", 11))
user_label.pack()
comp_label = tk.Label(root, text="Computer Choice: ", font=("Arial", 11))
comp_label.pack()
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=20)
root.mainloop()
