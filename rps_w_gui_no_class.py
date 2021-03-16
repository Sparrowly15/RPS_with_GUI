import tkinter as tk
from PIL import Image, ImageTk
#from rps_gui import RPS
import random

window = tk.Tk()

#set up all frames
frame1 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=3)
game_display = tk.Label(
    text="Welcome to Rock, Paper, Scissors.\nPress one of the buttons below to make your choice.",
    master=frame1
)
game_display.pack(expand=1, fill=tk.BOTH)
frame2 = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=3)

def get_user_choice(valid_picks):
    # add the meme picks to this list
    meme_picks = ["shoot"]
    full_valid = valid_picks + meme_picks

    # get user input
    print("Rock...\nPaper...\nScissors...\nShoot!\n")
    user_choice = input("Please enter \"Rock\", \"Paper\", or \"Scissors\": ")
    lower_choice = user_choice.lower()
    cleaned_choice = lower_choice.replace(" ", "")

    # verify user input
    if (cleaned_choice not in full_valid):
        cleaned_choice = "failed"

    return cleaned_choice

def counter(user_play, valid_picks):
    counters = {
        "shoot": "Nice try, disqualified."
    }
    if (user_play in counters):
        return counters[user_play]
    else:
        return random.choice(valid_picks)

def generate_outcome_string(response, result):
    results = {
        1: "It\'s a tie!",
        2: "You lose!",
        3: "You win!"
    }
    outcome = f"Computer chose {response.upper()}, {results[result]}"
    return outcome

def calc_outcome(user_play, response):
    outcome = ""
    if (user_play == "rock"):
        if (response == "rock"):
            outcome = generate_outcome_string(response, 1)
        elif (response == "paper"):
            outcome = generate_outcome_string(response, 2)
        elif (response == "scissors"):
            outcome = generate_outcome_string(response, 3)
        else:
            outcome = "Error in result processing"
    elif (user_play == "paper"):
        if (response == "rock"):
            outcome = generate_outcome_string(response, 3)
        elif (response == "paper"):
            outcome = generate_outcome_string(response, 1)
        elif (response == "scissors"):
            outcome = generate_outcome_string(response, 2)
        else:
            outcome = "Error in result processing"
    elif (user_play == "scissors"):
        if (response == "rock"):
            outcome = generate_outcome_string(response, 2)
        elif (response == "paper"):
            outcome = generate_outcome_string(response, 3)
        elif (response == "scissors"):
            outcome = generate_outcome_string(response, 1)
        else:
            outcome = "Error in result processing"
    else:
            outcome = "Error in result processing"

    return outcome

def run_game():
    valid_picks = ["rock", "paper", "scissors"]
    user_play = get_user_choice(valid_picks)

    if (user_play == "failed"):
        print("Error: please enter a valid choice.\n")
    else:
        print("Generating random pick...")
        response = counter(user_play, valid_picks)
        game_outcome = calc_outcome(user_play, response)
        print(game_outcome)

def update_game():
    global game_display
    game_display.config(text = "Yeet")

def main():
    #rock button
    rock_image = Image.open("Rock.png")
    rock_photo = ImageTk.PhotoImage(rock_image)
    rock_button = tk.Button(
        image=rock_photo,
        master=frame2,
        command=update_game
    )
    rock_button.pack(side=tk.LEFT)

    #paper button
    paper_image = Image.open("Paper.png")
    paper_photo = ImageTk.PhotoImage(paper_image)
    paper_button = tk.Button(
        image=paper_photo,
        master=frame2,
        command=update_game
    )
    paper_button.pack(side=tk.LEFT)

    #scissor button
    scissor_image = Image.open("Scissor.png")
    scissor_photo = ImageTk.PhotoImage(scissor_image)
    scissor_button = tk.Button(
        image=scissor_photo,
        master=frame2,
        command=update_game
    )
    scissor_button.pack(side=tk.LEFT)

    #pack frames
    frame1.pack(fill=tk.BOTH)
    frame2.pack(side=tk.BOTTOM)

    #ship it
    window.mainloop()

if __name__ == "__main__":
    main()