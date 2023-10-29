from colorama import Fore, init
import settings
from core import *
import os
import time

# Initialize Coloroma
init()

"""
    Initialize The Game
"""


def initialize_game():
    # Create a Game instance
    game = Game()
    # Check for saved data
    game.check_saved()
    # Get player data
    data = game.get_data()
    # Create a Hunter character
    hunter = Hunter()

    # Load player data into the Hunter character
    hunter.current_name = data["name"]
    hunter.current_weapon = data["weapon"]
    hunter.current_level = data["level"]
    hunter.current_exp = data["exp"]
    hunter.current_epilogue = data["epilogue"]
    hunter.current_health = data["health"]
    hunter.current_potion = data["potion"]
    hunter.type = data["type"]
    hunter.monster_killed = data["monster_killed"]
    hunter.total_dmgs = data["total_dmgs"]

    # Store the previous level to check for level-up
    hunter.previous_level = hunter.current_level

    # Display a success message and wait for 1 second
    success_msg("Starting Story")
    time.sleep(1)

    # Check if it's a new user or an existing player
    if not game.is_new_user:
        show_menu(hunter)
    else:
        hunter.first_epilogue()
        hunter.update_status()
        hunter.user_status()

        # Ask the user if they want to continue the journey
        user = input(Fore.RED + "Continue Journey (Y/n) ⮞ ")
        if user.lower() == "y":
            hunter.second_epilogue()

        if user.lower() == "n":
            print("")
            success_msg("Game has been saved.")


"""
New Game when user wants to start over again
"""


def new_game():
    # Remove any existing saved data
    os.remove("saved.json")
    # Call the initialize_game function to start a new game
    initialize_game()


# Define a function to continue the game for a given Hunter character
def continue_game(hunter):
    hunter.second_epilogue()


# Define a function to display information about the game
def about_game():
    utils.clearScreen()  # Placeholder function, clears the screen
    print(Fore.BLUE + "About ⮞")
    print(
        Fore.WHITE
        + """
Everything in here can be customized, you can add your own Monsters, Items, and even your own Boss. 
I made it like that, so anyone who is reading this that is new can play around with the settings and try to 
understand how the code itself works. I have written comments to explain how the code works and how it correlates 
with one another. I hope you have fun coding! Keep grinding y'all!
"""
    )
    print("\n- Dichill\n")

    input(Fore.RED + "Enter any key to go back to the menu ")


# Define a function to show the game menu
def show_menu(hunter):
    utils.clearScreen()  # Clear the screen
    while True:
        utils.clearScreen()
        # Display the game title and player's name
        print(Fore.RED + settings.TITLE)
        print(f"{Fore.WHITE}Welcome back {Fore.RED}Hunter {hunter.current_name}!")
        print(Fore.BLUE + "Select Option ⮞")
        print(Fore.GREEN + "     [1] Continue Game")
        print(Fore.LIGHTYELLOW_EX + "     [2] New Game")
        print(Fore.LIGHTBLUE_EX + "     [3] About")
        print(Fore.RED + "     [4] Quit")
        print("")
        try:
            user = int(
                input(Fore.LIGHTRED_EX + "[Hunter] " + hunter.current_name + " ⮞ ")
            )
        except ValueError:
            utils.clearScreen()
            print("Wrong Selection! Try again!")
            time.sleep(2)
            utils.clearScreen()

        # Process the user's choice
        if user == 1:
            continue_game(hunter)
        elif user == 2:
            new_game()
        elif user == 3:
            about_game()  # Placeholder for displaying game information
            continue
        elif user == 4:
            utils.clearScreen()
            success_msg("Game has been saved.")
            quit()

        else:
            error_msg("Invalid Option....")


# Entry point of the script
if __name__ == "__main__":
    # Display the game title and initialize the game
    print(Fore.RED + settings.TITLE)
    initialize_game()
