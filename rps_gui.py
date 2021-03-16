import tkinter as tk
from PIL import Image, ImageTk
import random

class RPS:
    def __init__(self):
        #set up gamestate variables
        self.needs_cleaning = False
        self.current_gamestate = ""

        #set up window
        self.window = tk.Tk()

        #set up all frames
        self.frame1 = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=3)
        self.game_display = tk.Label(
            text="Welcome to Rock, Paper, Scissors.\nPress one of the buttons below to make your choice.",
            master=self.frame1
        )
        self.game_display.pack(expand=1, fill=tk.BOTH)

        self.frame2 = tk.Frame(master=self.window, relief=tk.GROOVE, borderwidth=3)

        #rock button
        self.rock_image = Image.open("Rock.png")
        self.rock_photo = ImageTk.PhotoImage(self.rock_image)
        self.rock_button = tk.Button(
            image=self.rock_photo,
            master=self.frame2,
            command=self.choose_rock
        )
        self.rock_button.pack(side=tk.LEFT)

        #paper button
        self.paper_image = Image.open("Paper.png")
        self.paper_photo = ImageTk.PhotoImage(self.paper_image)
        self.paper_button = tk.Button(
            image=self.paper_photo,
            master=self.frame2,
            command=self.choose_paper
        )
        self.paper_button.pack(side=tk.LEFT)

        #Scissors button
        self.scissors_image = Image.open("Scissors.png")
        self.scissors_photo = ImageTk.PhotoImage(self.scissors_image)
        self.scissors_button = tk.Button(
            image=self.scissors_photo,
            master=self.frame2,
            command=self.choose_scissors
        )
        self.scissors_button.pack(side=tk.LEFT)

        #pack frames
        self.frame1.pack(fill=tk.BOTH)
        self.frame2.pack(side=tk.BOTTOM)

    def clean_game(self):
        clean_state = "Welcome to Rock, Paper, Scissors.\nPress one of the buttons below to make your choice."
        self.game_display.config(text=clean_state)
        return

    def update_game(self, new_message, append):
        if append:
            self.current_gamestate = self.current_gamestate + new_message
        else:
            self.current_gamestate = new_message
        self.game_display.config(text=self.current_gamestate)
        return

    def generate_outcome_string(self, response, result):
        results = {
            1: "It\'s a tie!",
            2: "You lose!",
            3: "You win!"
        }
        outcome = f"Computer chose {response.upper()}, {results[result]}"
        return outcome
    
    def calc_outcome(self, user_play, response):
        outcome = ""
        if (user_play == "rock"):
            if (response == "rock"):
                outcome = self.generate_outcome_string(response, 1)
            elif (response == "paper"):
                outcome = self.generate_outcome_string(response, 2)
            elif (response == "scissors"):
                outcome = self.generate_outcome_string(response, 3)
            else:
                outcome = "Error in result processing"
        elif (user_play == "paper"):
            if (response == "rock"):
                outcome = self.generate_outcome_string(response, 3)
            elif (response == "paper"):
                outcome = self.generate_outcome_string(response, 1)
            elif (response == "scissors"):
                outcome = self.generate_outcome_string(response, 2)
            else:
                outcome = "Error in result processing"
        elif (user_play == "scissors"):
            if (response == "rock"):
                outcome = self.generate_outcome_string(response, 2)
            elif (response == "paper"):
                outcome = self.generate_outcome_string(response, 3)
            elif (response == "scissors"):
                outcome = self.generate_outcome_string(response, 1)
            else:
                outcome = "Error in result processing"
        else:
                outcome = "Error in result processing"
        return outcome

    def counter(self, user_play, valid_picks):
        return random.choice(valid_picks)
    
    def run_game(self, user_play):
        valid_picks = ["rock", "paper", "scissors"]

        self.update_game(f"You chose {user_play.upper()}", False)
        self.update_game("\n\nGenerating random pick...", True)
        response = self.counter(user_play, valid_picks)
        game_outcome = self.calc_outcome(user_play, response)
        self.update_game(f"\n{game_outcome}", True)

        self.needs_cleaning = True
        self.update_game("\n\nPress one of the buttons below to start over...", True)
        return
    
    def choose_rock(self):
        if (self.needs_cleaning == True):
            self.clean_game()
            self.needs_cleaning = False
        else:
            self.run_game("rock")
        return
    
    def choose_paper(self):
        if (self.needs_cleaning == True):
            self.clean_game()
            self.needs_cleaning = False
        else:
            self.run_game("paper")
        return

    def choose_scissors(self):
        if (self.needs_cleaning == True):
            self.clean_game()
            self.needs_cleaning = False
        else:
            self.run_game("scissors")
        return

    def run_window(self):
        self.window.mainloop()
    