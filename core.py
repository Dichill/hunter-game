import json
from colorama import Fore, init
from pick import pick
import random
import settings
import time
import os

# Initalize Coloroma which is responsible for adding beautiful colors to our terminal
init()

"""
    Instead of repetitive coding of print(s) we can instead
    just make it into a function to make the code much more readable
"""


def info_msg(text):
    print(Fore.BLUE + f"[!] {text}")


def success_msg(text):
    print(Fore.GREEN + f"[✓] {text}")


def error_msg(text):
    print(Fore.RED + f"[X] {text}")


class Game:
    def __init__(self):
        self.is_new_user = True
        self.current_name = ""
        self.current_weapon = ""
        self.current_armor = "Basic Armor"
        self.current_level = 1
        self.current_exp = 0
        self.current_epilogue = 1
        self.current_health = 100
        self.current_potion = 1
        self.exp = 0

    """
        Same at the very top, but instead here we add a delay within the terminal
        to make it have like a story kind of effect.
    """

    def epilogue_msg(self, text, delay=2.5):
        if delay != 0:
            time.sleep(delay)
        print(Fore.WHITE + f"[+] {text}")

    def alert_msg(self, text):
        print(Fore.YELLOW + f"[!] {text}")

    """
        Check if the User is a new Player or Not.

        If New User -> First Epilogue Starts
        If Not New User -> Continue Gameplay (as there is already data)
    """

    def check_saved(self):
        info_msg("Checking saved.json")

        # Check if the file exists
        if os.path.isfile("saved.json"):
            # If it exists then we can simply disable the is_new_user boolean to disable
            # other functions that might be triggered if the user IS new.
            self.is_new_user = False
            success_msg("Initializing saved.json")
        else:
            # If its not in the records then we create a simple saved.json
            # With basic information in it. You can go ahead and check 'settings.py'
            # and find the variable CONFIG at line 71
            error_msg("Hunter is not in the records!")

            json_object = json.dumps(settings.CONFIG, indent=4)

            with open("saved.json", "w") as outfile:
                outfile.write(json_object)

    """
        Get the data if needed (this will be only initialized once and will be passed on onto different functions)
    """

    def get_data(self):
        with open("saved.json", "r") as json_file:
            data = json.load(json_file)
        return data

    """
        Update the data (This is used when the game is saving)
    """

    def update_data(self, new_data):
        json_file_path = "saved.json"
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)
        data.update(new_data)
        with open(json_file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

    def update_status(self):
        data = {
            "name": self.current_name,
            "weapon": self.current_weapon,
            "armor": self.current_armor,
            "level": self.current_level,
            "exp": self.current_exp,
            "epilogue": self.current_epilogue,
            "potion": self.current_potion,
        }
        self.update_data(data)

    def spawn_monster(self):
        difficulty_percentage = random.random()

        Slime = settings.MONSTER_PERCENTAGE[0]
        Ghoul = settings.MONSTER_PERCENTAGE[1]
        Zombie = settings.MONSTER_PERCENTAGE[2]

        if difficulty_percentage >= Slime:
            return "Slime"
        elif difficulty_percentage <= Slime and difficulty_percentage >= Ghoul:
            return "Ghoul"
        elif difficulty_percentage <= Ghoul and difficulty_percentage >= Zombie:
            return "Zombie"

    def monster_drop(self, current_monster):
        drops = []
        if current_monster == "Slime":
            drops = settings.SLIME_DROPS
        elif current_monster == "Ghoul":
            drops = settings.GHOUL_DROPS
        elif current_monster == "Zombie":
            drops = settings.ZOMBIE_DROPS

        is_lucky = random.random()

        if is_lucky >= settings.LUCK_PERCENTAGE:
            return random.choice(drops)
        else:
            return "Health Potion"

    def hunter_status(self):
        print(
            Fore.RED
            + "Hunter {0} ➤ \n  ‣LVL {1}\n  ‣EXP {2}/100\n  ‣WPN {3}".format(
                self.current_name,
                self.current_level,
                self.current_exp,
                self.current_weapon,
            )
        )

    def draw_hp_bar(self, current_hp=None, max_hp=100, bar_length=20):
        is_a_monster = False

        if current_hp == None:
            current_hp = self.current_health
        else:
            is_a_monster = True

        # Calculate the number of characters to represent the HP bar
        bar_fill = int((current_hp / max_hp) * bar_length)

        # Create the HP bar using asterisks (*) for filled HP and hyphens (-) for empty HP
        hp_bar = "[" + "*" * bar_fill + "-" * (bar_length - bar_fill) + "]"

        # Print the HP bar
        color = Fore.GREEN
        if not is_a_monster:
            if self.current_health <= 25:
                color = Fore.LIGHTRED_EX
                error_msg("HEALTH IS BELOW 25%!")

            print(color + "MY HP ⮞ " + hp_bar)
        else:
            print(Fore.RED + "MONSTER HP ⮞ " + hp_bar)

    def draw_hunter(self):
        print(
            Fore.WHITE
            + r"""
-------------
|           |
|     O     |
|    /|\    |
| {0}   | \   |
|    / \    |
|   /   \   |
|           |
-------------""".format(
                "🗡️",
            )
        )
        self.hunter_status()

    def hunter_menu(self):
        print(Fore.GREEN + "What do you want to do?")
        print(Fore.CYAN + "[1] Fight it")
        print(Fore.YELLOW + "[2] Flee")
        print(Fore.RED + "[3] Quit")

        try:
            return int(input(""))
        except:
            return None

    def fight_dashboard(self, current_monster, monster_hp):
        print(Fore.GREEN + settings.MONSTER_ART[current_monster])
        print(Fore.CYAN + "Fighting ➤  " + current_monster)

        self.hunter_status()
        # User HP
        self.draw_hp_bar()
        # Monster HP
        self.draw_hp_bar(monster_hp, max_hp=20)

        print(Fore.LIGHTRED_EX + f"What will you do?")
        print(Fore.WHITE + "[1] FIGHT")
        print("[2] USE POTION")
        print("[3] FLEE")

        try:
            return int(input(""))
        except:
            return None

    def fight_monster(self, current_monster):
        monster_hp = 20

        os.system("cls")

        while monster_hp > 0:
            player_action = self.fight_dashboard(current_monster, monster_hp)

            if player_action == None:
                continue
            elif player_action == 1:
                print("ATTACK")
            elif player_action == 2:
                if self.current_health == 100:
                    error_msg("Your Health is full!")
                    continue
                else:
                    total_hp = self.current_health + settings.HEALTH_POTION
                    if total_hp > 100:
                        self.current_health = 100
                    else:
                        self.current_health = total_hp

            elif player_action == 3:
                print("FLEE")
                time.sleep(1)
                break

    """
        This is where the Story Would Take Place
        EPILOGUE 1: AN OLD MAN'S TALE
        EPILOGUE 2: THe HUNTER'S TRIAL
    """

    def continue_gameplay(self):
        os.system("cls")
        self.alert_msg("Goal: You must reach Level 5 to Defeat the Boss!")
        time.sleep(2.5)

        while True:
            os.system("cls")

            self.draw_hunter()
            self.draw_hp_bar()

            print(Fore.LIGHTRED_EX + "Walking through the dark and cold cave....")

            monster_spawning = random.random()

            # Check if the random number falls within the specified probability
            if monster_spawning <= settings.PROBABILITY:
                time.sleep(1)

                current_monster = self.spawn_monster()
                self.alert_msg("Theres a {0}! Defeat it!".format(current_monster))
                action = self.hunter_menu()

                if action == None:
                    error_msg("Invalid Input! Trying again...")
                    continue
                elif action == 1:
                    self.fight_monster(current_monster)
                    continue
                elif action == 2:
                    success_msg("You Fled the scene...")
                    pass
                elif action == 3:
                    # Save first before it quits
                    os.system("cls")
                    self.update_status()
                    success_msg("Game has been saved.")

                    quit()

            else:
                # Continue the loop
                pass

            # Updates the Frame Every 1 Second
            time.sleep(1)

    # First Epilogue: AN OLD MAN'S TALE
    def first_epilogue(self):
        os.system("cls")
        print(Fore.CYAN + "⮞ FIRST EPILOGUE: AN OLD MAN'S TALE")

        epilogue_texts = settings.EPILOGUE_ONE

        for text in epilogue_texts[:3]:
            self.epilogue_msg(text)

        name = input(Fore.RED + "What is your name? ➤ ")
        self.current_name = name

        self.epilogue_msg(epilogue_texts[3].format(name), 1)
        self.epilogue_msg(epilogue_texts[4].format(name), 5)

        time.sleep(5)

        options = ["Sword", "Bow", "Axe"]
        _, index = pick(options, "PICK YOUR WEAPON")

        self.current_weapon = options[index]

        if index == 0:
            self.epilogue_msg(epilogue_texts[5], 0)
        elif index == 2:
            self.epilogue_msg(epilogue_texts[6], 0)
        elif index == 1:
            self.epilogue_msg(epilogue_texts[7], 0)

        print("")
        self.epilogue_msg(epilogue_texts[8].format(name, self.current_weapon), 5)

        time.sleep(5)

        os.system("cls")

        print(Fore.RED + settings.TITLE)
        print(
            Fore.WHITE
            + f"Congratulations {Fore.RED}Hunter {name} {Fore.WHITE}for Completing {Fore.GREEN}Epilogue 1!"
        )
        self.current_epilogue = 2

    # Second Epilogue: THE HUNTER'S TRIALS
    def second_epilogue(self):
        os.system("cls")
        print(Fore.CYAN + "⮞ SECOND EPILOGUE: THE HUNTER'S TRIALS")

        self.epilogue_msg(settings.EPILOGUE_TWO[0])

        time.sleep(5)

        self.continue_gameplay()


class Hunter(Game):
    def __init__(self):
        super().__init__()

    def user_status(self):
        print(self.current_name)
        print(Fore.BLUE + "Current Status ⮞")
        print(f"     Health ￫ {self.current_health}/100")
        print(f"     Weapon ￫ {self.current_weapon}")
        print(f"     Armor ￫ {self.current_armor}")


def initialize_game():
    game = Game()
    game.check_saved()
    data = game.get_data()
    hunter = Hunter()

    hunter.current_name = data["name"]
    hunter.current_weapon = data["weapon"]
    hunter.current_armor = data["armor"]
    hunter.current_level = data["level"]
    hunter.current_exp = data["exp"]
    hunter.current_epilogue = data["epilogue"]
    hunter.current_health = data["health"]

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
            print("~ End Game ~")


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
        success_msg("Saving Game")

    else:
        error_msg("Invalid Option....")


if __name__ == "__main__":
    print(Fore.RED + settings.TITLE)
    initialize_game()
