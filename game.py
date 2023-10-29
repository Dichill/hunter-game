from colorama import Fore, init
import settings
from core import *
import os
import time

init()


def initialize_game():
    game = Game()
    game.check_saved()
    data = game.get_data()
    hunter = Hunter()

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

    # Just to know if the user newly leveled up
    hunter.previous_level = hunter.current_level

    success_msg("Starting Story")
    time.sleep(1)

    if not game.is_new_user:
        show_menu(hunter)
    else:
        hunter.first_epilogue()

        hunter.update_status()
        hunter.user_status()

        user = input(Fore.RED + "Continue Journey (Y/n) ⮞ ")
        if user.lower() == "y":
            hunter.second_epilogue()

        if user.lower() == "n":
            print("")
            success_msg("Game has been saved.")


def new_game():
    os.remove("saved.json")
    initialize_game()


def continue_game(hunter):
    hunter.second_epilogue()


def about_game():
    os.system("cls")


def show_menu(hunter):
    os.system("cls")
    has_selected = False
    while not has_selected:
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
            has_selected = True
        except ValueError:
            os.system("cls")
            print("Wrong Selection! Try again!")
            time.sleep(2)
            os.system("cls")
    if user == 1:
        continue_game(hunter)
    elif user == 2:
        new_game()
        # Handle "About" option
        pass
    elif user == 3:
        print("About")
    elif user == 4:
        success_msg("Game has been saved.")

    else:
        error_msg("Invalid Option....")


if __name__ == "__main__":
    print(Fore.RED + settings.TITLE)
    initialize_game()
