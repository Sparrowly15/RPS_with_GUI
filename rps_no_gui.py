import tkinter as tk
import random

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

def main():
    run_game()
    return 0

if __name__ == "__main__":
    main()