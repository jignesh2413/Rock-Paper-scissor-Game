import random
import tkinter as tk


window = tk.Tk()
window.geometry("500x500")
window.title("Rock Paper Scissors Game")


options = {"Rock": 0, "Paper": 1, "Scissors": 2}


def play(player_choice):

    computer_choice = random.randint(0, 2)

    if computer_choice == player_choice:
        outcome_text.set("Tie!")
    elif (player_choice == options["Rock"] and computer_choice == options["Scissors"] or
          player_choice == options["Paper"] and computer_choice == options["Rock"] or
          player_choice == options["Scissors"] and computer_choice == options["Paper"]):
        outcome_text.set("You win!")
    else:
        outcome_text.set("Computer wins!")


    player_choice_text.set("You chose " + list(options.keys())[list(options.values()).index(player_choice)])
    computer_choice_text.set("Computer chose " + list(options.keys())[list(options.values()).index(computer_choice)])


player_choice_text = tk.StringVar()
computer_choice_text = tk.StringVar()
outcome_text = tk.StringVar()

player_choice_label = tk.Label(window, textvariable=player_choice_text,font=('arial',20,'bold') )
player_choice_label.pack()

computer_choice_label = tk.Label(window, textvariable=computer_choice_text, font=('arial',20,'bold'))
computer_choice_label.pack()

outcome_label = tk.Label(window, textvariable=outcome_text, font=('arial',20,'bold'))
outcome_label.pack()

rock_button = tk.Button(window, text="Rock", command=lambda: play(options["Rock"]), font=('arial',20,'bold'), background='orange')
rock_button.pack()

paper_button = tk.Button(window, text="Paper", command=lambda: play(options["Paper"]), font=('arial',20,'bold'), background='green')
paper_button.pack()

scissors_button = tk.Button(window, text="Scissors", command=lambda: play(options["Scissors"]), font=('arial',20,'bold'), background='cyan')
scissors_button.pack()

window.mainloop()
