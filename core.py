import json
from colorama import Fore, init
from pick import pick
import random
import settings
import time
import os
import utils

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
        """
        All the variables that we need for the Game & for the Hunter
        """
        self.is_new_user = True
        self.current_name = ""
        self.current_weapon = ""
        self.current_level = 1
        self.current_exp = 0
        self.current_epilogue = 1
        self.current_health = 100
        self.current_potion = 0
        self.previous_level = 1
        self.type = None
        self.exp = 0
        self.monster_killed = 0
        self.total_dmgs = 0

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
        Accepting JSON and then updating it onto our saved.json file
    """

    def update_data(self, new_data):
        json_file_path = "saved.json"
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)
        data.update(new_data)
        with open(json_file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

    """
        This is the function where we update all of our variables and push them into
        the json file. Noticed how we called update_data which is above this function?

    """

    def update_status(self):
        data = {
            "name": self.current_name,
            "weapon": self.current_weapon,
            "level": self.current_level,
            "health": self.current_health,
            "exp": self.current_exp,
            "epilogue": self.current_epilogue,
            "potion": self.current_potion,
            "type": self.type,
            "monster_killed": self.monster_killed,
            "total_dmgs": self.total_dmgs,
        }
        self.update_data(data)

    """
        START OF HUNTER
    """

    # Just a function that shows the status of the hunter
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

    # A HP Bar Skeleton that renders the HP for the player, monsters, and the Boss
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

            print(color + "MY HP ⮞ " + hp_bar + f" {current_hp}/{max_hp}")
        else:
            print(Fore.RED + "MONSTER HP ⮞ " + hp_bar + f" {current_hp}/{max_hp}")

    # Draw the funny looking sticky figure of the player with a weapon on his/her left hand.
    def draw_hunter(self):
        print(
            Fore.WHITE
            + r"""
-------------
|           |
|     O     |
|    /|\    |
| {0}  | \   |
|    / \    |
|   /   \   |
|           |
-------------""".format(
                "🗡️",
            )
        )
        self.hunter_status()

    # Shows all the Menu when you found a monster
    def hunter_menu(self):
        print(Fore.GREEN + "What do you want to do?")
        print(Fore.CYAN + "[1] FIGHT")
        print(Fore.YELLOW + "[2] FLEE")
        print(Fore.RED + "[3] QUIT")
        if self.current_level >= 5:
            print(Fore.LIGHTWHITE_EX + "[4] FIGHT THE BOSS")

        # This is used to avoid errors stopping our game, so we catch it and return None instead
        # and let the loop continue
        try:
            return int(input(""))
        except:
            return None

    """
        FIGHTING DASHBOARD
    """

    def fight_dashboard(self, current_monster, monster_hp):
        print(Fore.GREEN + settings.MONSTER_ART[current_monster])
        print(Fore.CYAN + "Fighting ➤  " + current_monster)

        # Hunter Status
        self.hunter_status()
        # User HP
        self.draw_hp_bar()
        # Monster HP
        self.draw_hp_bar(monster_hp, max_hp=20)

        # Simple Menu
        print(Fore.LIGHTRED_EX + f"What will you do?")
        print(Fore.WHITE + "[1] ATTACK")
        print(f"[2] USE POTION ({self.current_potion}x)")
        print("[3] FLEE")

        try:
            return int(input(""))
        except:
            return None

    """
        START OF MONSTER
    """

    # Get the KEY based from the VALUE
    def get_weapon_type(self, type):
        # We can get the KEY based on the value that we give it.
        for type, name in type.items():
            if name == self.current_weapon:
                return type

    def spawn_monster(self):
        # Generate a random number between 0 and 1 to determine the monster spawn
        difficulty_percentage = random.random()

        cumulative_probability = 0  # Initialize a cumulative probability variable to keep track of probabilities

        # Iterate over MONSTERS and MONSTER_PERCENTAGE using zip to check each monster's spawn probability
        for monster, probability in zip(settings.MONSTERS, settings.MONSTER_PERCENTAGE):
            cumulative_probability += probability  # Add the current monster's probability to the cumulative probability

            # If the random number is less than the cumulative probability, this monster spawns
            if difficulty_percentage < cumulative_probability:
                return monster  # Return the name of the spawned monster

        # If no monster spawns (which should be very rare), return None
        return None

    def monster_drop(self, current_monster):
        # Get the list of possible drops for the current monster from settings
        drops = settings.MONSTER_DROPS[current_monster]

        # Generate a random number between 0 and 1 to determine if the player is lucky
        is_lucky = random.random()

        # Check if the player is lucky (random number is greater than or equal to LUCK_PERCENTAGE)
        if is_lucky >= settings.LUCK_PERCENTAGE:
            # Return a random item from the list of drops
            return random.choice(drops)
        else:
            # If the player is not lucky, return a "Health Potion"
            return "Health Potion"

    def damage_modifier(self):
        weapon_type = None
        current_wpn = self.type
        damage = None

        # Get the weapon type based on the current weapon
        weapon_type = self.get_weapon_type(settings.WEAPONS[self.type])

        if weapon_type is not None:
            # Get the damage range for the current weapon type from settings
            damage = settings.WPN_DMGS[current_wpn][weapon_type]

            # Generate a random damage value within the specified range
            final_damage = random.randint(damage[0], damage[1])

            # Add the final damage to the total damage the player has dealt
            self.total_dmgs += final_damage

            # Display a message indicating the amount of damage dealt to the monster
            self.alert_msg(f"You dealt {final_damage} DMG to the monster!")

            # Return the final damage value
            return final_damage

        # If the weapon type is not found, return None
        return None

    """
        Calculate how the user would receive the reward when the user kills a monster
    """

    def monster_reward(self, current_monster):
        index_of_monster = settings.MONSTERS.index(current_monster)
        exp_reward = settings.MONSTER_EXP[index_of_monster]
        drop_reward = settings.MONSTER_DROPS[current_monster][
            random.randint(0, len(settings.MONSTER_DROPS[current_monster]) - 1)
        ]
        self.monster_killed += 1

        if drop_reward != "Health Potion":
            success_msg(f"You have received a {drop_reward} item!")
            user_equip = input(Fore.WHITE + "Do you want to equip it? (Y/n) ")

            if user_equip.lower() == "y":
                new_weapon = settings.WEAPONS[self.type][drop_reward]

                self.current_weapon = new_weapon
                success_msg(f"Successfully Equipped {new_weapon}!")
                time.sleep(1)

        else:
            self.current_potion += 1

        total_exp = exp_reward + self.current_exp
        if total_exp >= 100:
            self.current_exp = 0
            self.current_level += 1
        else:
            self.current_exp = total_exp

        return [exp_reward, drop_reward]

    """
        The functionality of the Potion is here
    """

    def use_potion(self):
        if self.current_potion == 0:
            error_msg("You do not have any potions left!")
            time.sleep(2)
            return

        total_hp = self.current_health + settings.HEALTH_POTION
        if total_hp > 100:
            self.current_health = 100
        else:
            self.current_health = total_hp
        self.current_potion -= 1

    """
        This is the logic where the user fights with the monster
        Most of the functions above will be called from this function below
    """

    def fight_monster(self, current_monster):
        monster_hp = 20
        did_user_flee = False

        while monster_hp > 0 and self.current_health > 0:
            utils.clearScreen()

            player_action = self.fight_dashboard(current_monster, monster_hp)

            if player_action == None:
                continue
            elif player_action == 1:
                dmg_to_deal = self.damage_modifier()
                final_hp = monster_hp - dmg_to_deal

                if final_hp > 0:
                    monster_hp = final_hp

                    does_monster_hit = random.random()

                    if settings.MONSTER_HIT_BACK <= does_monster_hit:
                        monster_dmg = settings.MONSTER_DMG[
                            settings.MONSTERS.index(current_monster)
                        ]

                        monster_dmg_to_user = random.randint(1, monster_dmg)
                        hunter_final_hp = self.current_health - monster_dmg_to_user

                        if hunter_final_hp >= 1:
                            self.current_health = hunter_final_hp
                        else:
                            self.current_health = 0

                        print(
                            Fore.RED
                            + f"[⚠️] The monster hitted back and dealt a damage of {monster_dmg_to_user} to you!"
                        )
                else:
                    time.sleep(2)
                    break
                time.sleep(1.5)

            elif player_action == 2:
                if self.current_health == 100:
                    error_msg("Your Health is already full!")
                    time.sleep(2)
                    continue
                else:
                    self.use_potion()

            elif player_action == 3:
                success_msg("You fled from the scene.")
                time.sleep(1)
                did_user_flee = True
                break

        if self.current_health > 0 and did_user_flee == False:
            utils.clearScreen()
            item_reward = self.monster_reward(current_monster)

            success_msg("You have successfully eradicated the monster!")
            print(
                f" ⮞ Gained {item_reward[0]} EXP and received a {item_reward[1]} item!"
            )
            print("")
            time.sleep(3)
        elif self.current_health == 0:
            utils.clearScreen()
            print(Fore.Red + settings.DEAD_TXT)
            error_msg("You died!")
            input(Fore.GREEN + "Enter any keys to resurrect ")
            self.current_health = 50

    """
        START OF BOSS
    """

    # Menu for the Boss, same as the other Menu's like the Hunter Menu and etc.
    def boss_menu(self):
        print(Fore.YELLOW + "What will you do?")
        print(Fore.WHITE + "[1] ATTACK")
        print(f"[2] USE POTION ({self.current_potion}x)")

        try:
            return int(input(""))
        except:
            return None

    # Dashboard when fighting the boss. This displays the common values such as HP, POTIONS and etc.
    def boss_dashboard(self):
        boss_hp = settings.BOSS_HP

        while boss_hp > 0 or self.current_health > 0:
            utils.clearScreen()
            print(Fore.GREEN + settings.BOSS_ART["WYWM"][0])
            self.draw_hp_bar()
            self.draw_hp_bar(current_hp=boss_hp, max_hp=settings.BOSS_HP)
            print(Fore.WHITE + "[!] You are now fighting the final boss!")
            self.hunter_status()

            user = self.boss_menu()

            if user == 1:
                dmg = self.damage_modifier()
                final_boss_hp = boss_hp - dmg

                if final_boss_hp > 0:
                    boss_hp = final_boss_hp
                else:
                    boss_hp = 0
                    break

                boss_attack = random.random()

                if boss_attack <= settings.BOSS_FIGHT_BACK[0]:
                    boss_dmg = random.randint(1, settings.BOSS_DMG[0])
                    final_hunter_hp = self.current_health - boss_dmg
                    if final_hunter_hp > 0:
                        self.current_health = final_hunter_hp
                    else:
                        self.current_health = 0
                        break
                    print(
                        Fore.RED + f"[⚠️] The boss dealt a damage of {boss_dmg} to you!"
                    )
                    time.sleep(1)
            elif user == 2:
                self.use_potion()
            else:
                quit()

            time.sleep(1)

        if self.current_health == 0:
            utils.clearScreen()
            print(Fore.Red + settings.DEAD_TXT)
            error_msg("You died!")
            input(Fore.GREEN + "Enter any keys to resurrect ")
            self.current_health = 50
        if boss_hp == 0:
            utils.clearScreen()
            print(Fore.GREEN + settings.BOSS_ART["WYWM"][0])
            print(
                f"{Fore.WHITE}[!] Wha.... What is this? I won't forget this.... {self.current_name}... Til we meet again."
            )
            time.sleep(5)
            self.epilogue_msg(settings.EPILOGUE_THREE[2].format(self.current_name))

            time.sleep(3)
            success_msg(
                f'Congratulations! You have achieved the title, "{settings.BOSS_DROP[0]}"!'
            )

            time.sleep(2)
            info_msg(
                "Thank you for playing this short and simple game! Til we meet again :) - Dichill"
            )

            time.sleep(2)
            info_msg(
                "You can continue playing if you like, theres no restriction for how far you should level up"
            )

            time.sleep(2)
            info_msg(
                "You can also add your own weapons and monsters in this game! I coded this game such that anyone can have fun and add their own characters here too!"
            )

            time.sleep(2)
            success_msg("Til we meet again!")

            # A Quick Summary of the Journey of the User
            print(Fore.GREEN + "Summary ⮞" + Fore.WHITE)
            print(f"  • You have killed at least {self.monster_killed} monster(s)!")
            print(f"  • Your Total Damage is at least {self.total_dmgs} DMG(s)!")
            print(f"  • You beated the Boss at Level {self.current_level}")
            print(f"  • Your remaining Potions is {self.current_potion}!")
            input(Fore.RED + "Enter any key to go back to the menu ")

    """
        The logic when the user fights the Boss
    """

    def fight_boss(self):
        utils.clearScreen()
        error_msg("You are now fighting the FINAL BOSS.....".upper())
        time.sleep(2.5)
        error_msg(
            "There is no going back... You will lose all progress IF you DIE....".upper()
        )
        time.sleep(2.5)
        error_msg("Are you prepared?".upper())
        time.sleep(1.5)
        tnc = input(Fore.WHITE + "[Hunter] Dichill (Y/n) ⮞ ")

        if tnc.lower() == "y":
            utils.clearScreen()
            time.sleep(1)
            for x in settings.WYWM_ALL_ARTS:
                print(Fore.GREEN + x)
                time.sleep(0.5)

            utils.clearScreen()
            print(Fore.GREEN + settings.BOSS_ART["WYWM"][0])
            self.epilogue_msg(settings.EPILOGUE_THREE[0], 1)
            self.epilogue_msg(settings.EPILOGUE_THREE[1])
            time.sleep(2.5)
            self.boss_dashboard()

        else:
            self.continue_gameplay()

    """
        This is where the Story Would Take Place
        EPILOGUE 1: AN OLD MAN'S TALE
        EPILOGUE 2: THe HUNTER'S TRIAL
    """

    def continue_gameplay(self):
        utils.clearScreen()
        self.alert_msg(
            "Goal: You must reach Level 5 and get Good Items to Defeat the Boss!"
        )
        time.sleep(2.5)

        while True:
            utils.clearScreen()

            self.draw_hunter()
            self.draw_hp_bar()

            print(Fore.LIGHTRED_EX + "Walking through the dark and cold cave....")

            current_monster = self.spawn_monster()

            if current_monster != None:
                self.alert_msg("Theres a {0}! Defeat it!".format(current_monster))
                action = self.hunter_menu()

                if action == None:
                    error_msg("Invalid Input! Trying again...")
                    continue
                elif action == 1:
                    self.fight_monster(current_monster)

                    if self.current_level > self.previous_level:
                        utils.clearScreen()
                        print(Fore.GREEN + settings.CONGRATS_TXT)
                        print(
                            Fore.CYAN
                            + f"Congratulations Hunter {self.current_name} for Leveling up!"
                        )
                        print(Fore.GREEN + "Summary ⮞" + Fore.WHITE)
                        if self.current_level < 5:
                            print(
                                f"  • {5 - self.current_level} more levels to go to fight the boss!"
                            )
                        else:
                            print(f"  ✓ You are now ready to fight the boss!")
                        print(
                            f"  • You have {self.current_potion}x Potions (recommended to have 10+ more for the final boss!)"
                        )

                        print(f"  • Get a legendary weapon!")

                        self.previous_level = self.current_level
                        time.sleep(3.5)

                    continue
                elif action == 2:
                    success_msg("You Fled the scene...")
                    pass
                elif action == 3:
                    # Save first before it quits
                    utils.clearScreen()
                    self.update_status()
                    success_msg("Game has been saved.")

                    quit()
                elif action == 4 and self.current_level >= 5:
                    self.fight_boss()
                self.update_status()
            else:
                pass

            # Updates the Frame Every 1 Second
            time.sleep(1)

    # First Epilogue: AN OLD MAN'S TALE
    def first_epilogue(self):
        utils.clearScreen()
        print(Fore.CYAN + "⮞ FIRST EPILOGUE: AN OLD MAN'S TALE")

        epilogue_texts = settings.EPILOGUE_ONE

        for text in epilogue_texts[:3]:
            self.epilogue_msg(text)

        name = input(Fore.RED + "What is your name? ➤ ")
        self.current_name = name

        self.epilogue_msg(epilogue_texts[3].format(name), 1)
        self.epilogue_msg(epilogue_texts[4].format(name), 5)

        time.sleep(5)

        options = ["Wooden Sword", "Wooden Bow", "Wooden Axe"]
        _, index = pick(options, "PICK YOUR WEAPON")

        self.current_weapon = options[index]
        self.type = options[index].split(" ")[1]

        if index == 0:
            self.epilogue_msg(epilogue_texts[5], 0)
        elif index == 2:
            self.epilogue_msg(epilogue_texts[6], 0)
        elif index == 1:
            self.epilogue_msg(epilogue_texts[7], 0)

        print("")
        self.epilogue_msg(epilogue_texts[8].format(name, self.current_weapon), 5)

        time.sleep(5)

        utils.clearScreen()

        print(Fore.RED + settings.TITLE)
        print(
            Fore.WHITE
            + f"Congratulations {Fore.RED}Hunter {name} {Fore.WHITE}for Completing {Fore.GREEN}Epilogue 1!"
        )
        self.current_epilogue = 2

    # Second Epilogue: THE HUNTER'S TRIALS
    def second_epilogue(self):
        utils.clearScreen()
        print(Fore.CYAN + "⮞ SECOND EPILOGUE: THE HUNTER'S TRIALS")

        self.epilogue_msg(settings.EPILOGUE_TWO[0], 0)

        time.sleep(5)

        self.continue_gameplay()


class Hunter(Game):
    def __init__(self):
        super().__init__()

    def user_status(self):
        print(Fore.BLUE + "Current Status ⮞")
        print(f"     Weapon ￫ {self.current_weapon}")
        print(f"     Class ￫ {self.type} User")
        print(f"     Level ￫ {self.current_level}")
        print(f"     EXP ￫ {self.exp}")
