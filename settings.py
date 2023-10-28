"""
    ALL TYPES OF WEAPONS
    SWORD | BOW | AXE
"""
SWORD_TYPE = {
    "Basic": "Wooden Sword",
    "Common": "Katana",
    "Epic": "Samurai Sword",
    "Legendary": "Excalibur",
}
SWORD_DMG = [[4, 6], [6, 8], [9, 11], [16, 22]]

BOW_TYPE = {
    "Basic": "Wooden Bow",
    "Common": "Long Bow",
    "Epic": "Crossbow",
    "Legendary": "Bow of Apollo",
}
BOW_DMG = [[3, 4], [4, 7], [8, 10], [15, 20]]

AXE_TYPE = {
    "Basic": "Wooden Axe",
    "Common": "Katana",
    "Epic": "Samurai Sword",
    "Legendary": "Leviathan Axe",
}

"""
    How Lucky must the user be?
    From:
    - Getting Weapons
    - Damage
    - Fighting Monsters
"""
LUCK_PERCENTAGE = 0.4  # PERCENTAGE
PROBABILITY = 0.6  # PERCENTAGE
HEALTH_POTION = 50

MONSTERS = ["Slime", "Ghoul", "Zombie"]
MONSTER_PERCENTAGE = [0.6, 0.3, 0.1]
MONSTER_EXP = [30, 50, 70]

SLIME_DROPS = ["Common", "Health Potion"]
GHOUL_DROPS = ["Epic", "Common", "Health Potion"]
ZOMBIE_DROPS = ["Legendary", "Epic", "Common", "Health Potion"]

BOSS = "WithYouWithMe"
BOSS_DROP = ["The Undefeatable"]


EPILOGUE_ONE = [
    """In a dense forest, where the shadows of towering trees concealed secrets of old, a skillful hunter ventured deep into the wilderness.\nHe had been tracking elusive prey for days, but as he ventured further, a soft, raspy voice cut through the silence.
    """,
    """You followed the voice to a small, secluded cottage, nearly swallowed by the encroaching forest. Inside, he discovered an old man, bedridden and frail.\nThe man's eyes, however, held a spark of wisdom and determination that belied his years.
    """,
    """"I've been waiting for someone like you," the old man wheezed, his voice strained. \n"I need your help to defeat the final boss of this land. I can't do it alone. May I know your name my fellow hunter?"
    """,
    """{0}, intrigued by the old man's story and the promise of adventure, agreed to lend his strength.\nThe old man reached beneath his bed and produced a wooden chest. Inside were three items: a gleaming sword, a finely crafted bow, and a sturdy axe.\n""",
    """"{0}... You must choose," the old man said, 'for one of these will become your weapon on this quest.'""",
    """The old man smiled, his eyes filled with gratitude. "The sword," he said, his voice carrying a sense of honor. "A blade of precision and grace. With this weapon, you'll become a master of finesse and technique.'""",
    """The old man smiled, his eyes filled with gratitude. "Ah, the axe," he murmured with a knowing nod. "It's a symbol of sheer strength and determination. With this mighty weapon, you'll cleave through obstacles and adversaries alike.""",
    """The old man smiled, his eyes filled with gratitude. "With the bow, you'll have the advantage of surprise and accuracy," he explained. 'It's a wise choice.'""",
    """And so, {0}, the hunter with his trusty {1} in hand, embarked on a new quest with the old man as his guide.\nTogether, they would face the final boss, their fates intertwined in the heart of the mystical forest, where adventure and challenges awaited them at every turn.""",
]

EPILOGUE_TWO = [
    """The hunter, armed with the weapon of their choice, ventured deeper into the forest, determined to prove their worth.\nTheir path led them to a dark and foreboding cave. Inside, they encountered a series of trials, battling fearsome monsters one after another."""
]

TITLE = """ __    __   __    __  .__   __. .___________. _______ .______      
|  |  |  | |  |  |  | |  \ |  | |           ||   ____||   _  \     
|  |__|  | |  |  |  | |   \|  | `---|  |----`|  |__   |  |_)  |    
|   __   | |  |  |  | |  . `  |     |  |     |   __|  |      /     
|  |  |  | |  `--'  | |  |\   |     |  |     |  |____ |  |\  \----.
|__|  |__|  \______/  |__| \__|     |__|     |_______|| _| `._____|
"""

CONFIG = {
    "name": "WithYouWithMe",
    "level": 1,
    "exp": 0,
    "weapon": "basic",
    "armor": "basic",
    "epilogue": 1,
    "health": 100,
    "potion": 1,
}


MONSTER_ART = {
    "Slime": r"""
                ░░░░░░░░░░
            ░░░░        ░░░░░░
        ░░                  ░░
        ░░                    ░░░░
    ░░                      ░░░░░░
    ░░                        ░░░░
    ░░                ░░    ░░  ░░░░░░
    ░░                ██░░  ██    ░░░░
    ░░                ██░░  ██    ░░░░
    ░░            ░░            ░░░░░░
    ░░░░░░                      ░░░░░░
    ░░░░░░                  ░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░
""",
    "Ghoul": "",
    "Zombie": r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣴⣾⣶⣶⠿⢷⣶⣶⣶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠻⢿⣷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⡿⣿⣿⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠉⠀⠿⠇⠉⢉⣳⣶⣶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠘⠟⠉⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣽⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣻⣤⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡾⢿⠏⢻⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⡿⣿⠁⠀⢰⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀⠹⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠶⢶⣿⣯⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣴⡿⠛⢿⣾⣿⠁⠀⠤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⠿⠁⠿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠄⠀⢻⣷⣾⠟⠿⣷⣄⠀⠀
⢀⣼⡿⠋⠀⠀⢈⣿⡟⠀⠀⠀⢸⡏⠛⠳⢦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠴⠟⠛⣿⠀⠀⠀⢸⣿⡇⠀⠀⠈⠻⣷⡄
⣾⡟⠀⢀⡀⠀⢸⣿⡇⠀⠀⠀⢸⣧⠀⠀⠀⠈⠙⠻⢶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠶⠋⠉⠀⠀⠀⢰⡿⠀⠀⠀⢸⣿⡇⠀⠀⢀⠀⠘⣷
⢿⣧⠀⠀⢿⢦⡘⣿⡇⠀⠀⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠈⠙⠳⣦⣄⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⣀⣤⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀⣾⣷⠀⠀⠀⢸⣿⡇⢠⠶⠁⠀⢠⣿
⠘⢿⣆⠀⠀⠀⠙⢻⣿⡀⠀⠀⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⣿⠷⣄⡀⠀⠀⢸⠀⠀⠀⣠⣤⠞⣿⡏⣧⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⠃⠀⠀⠀⣼⣿⠏⠀⠀⠀⢀⣾⠏
⠀⠘⢿⣦⡀⠀⠀⠘⣿⣧⠀⠀⠀⠐⢿⣿⣄⠀⠀⠀⠀⠀⢀⣾⣵⠯⠇⠀⠈⠙⠛⠛⡏⠹⡟⠛⠉⠀⠀⢿⣷⣻⣇⠀⠀⠀⠀⠀⣀⣼⣿⠕⠀⠀⠀⣠⣿⠏⠀⠀⠀⣠⣿⠋⠀
⠀⠀⠀⠙⢿⣦⣄⡀⠘⣿⣷⡀⠀⠀⠀⠙⠿⣿⣦⣤⣀⣴⡾⠋⠁⠀⠀⠀⠀⠀⠀⣼⣧⢠⣿⡄⠀⠀⠀⠀⠀⠙⠻⣷⣤⣀⣤⣶⠿⠟⠁⠀⠀⠀⣰⣿⠏⠀⢀⣴⣾⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠉⠛⠿⣶⣾⣿⣷⣄⠲⣤⡀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⢸⢹⣷⡄⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⣠⡴⢂⣼⣿⣿⣶⡾⠟⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣧⡌⠻⣷⡾⢦⡀⢀⣤⡄⠀⠀⠀⠀⠀⠀⠸⠿⠷⠛⠘⠛⠛⠛⠀⠀⠀⠀⠀⢠⣤⡄⠀⣠⠷⣴⡿⢋⣠⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣷⣌⡳⢦⣙⠞⣁⣙⢦⡴⢿⡄⣀⣤⣤⡀⠀⣤⡀⠀⣠⣤⣄⢀⣾⢷⣴⢟⣁⠘⣿⣡⣶⣯⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣶⣯⣛⣋⠉⠳⠶⠶⣿⡻⠶⣎⠻⣿⡷⣽⡟⢡⡶⢮⣛⣷⠶⡶⠚⢙⣿⣿⣷⣿⠿⣟⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⢿⣿⣶⣦⣤⣭⣅⣀⣈⡛⠉⠀⠈⠛⣏⣀⣀⣬⣤⣴⣾⣿⣿⣿⣿⣫⣅⠀⠉⣛⡳⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⣤⣴⣶⣦⣄⡈⠉⠛⠛⠛⢿⡿⠿⠿⠿⠿⢿⣿⡿⠛⠛⣛⣋⣉⣴⠟⠋⠿⢿⡏⣿⣇⢻⣿⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢫⣽⡟⠁⣤⣍⠳⣍⠻⢷⣿⠲⠶⠟⠁⠘⠛⠛⠛⠋⠉⠛⠛⠋⠉⣿⡋⠁⠀⠀⣠⡿⠛⠋⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢻⣟⣿⣧⢹⡝⢷⡟⠀⠀⢿⣆⠀⠀⠀⢀⠀⠀⠀⠀⢀⡀⠀⠀⠀⢸⡇⢀⣴⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠘⠶⠇⠀⠙⢷⣄⣠⡿⠀⣠⡴⢋⣵⣶⠶⣦⠀⠉⠳⣤⣄⠸⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡴⢾⡟⠀⣼⣁⣿⠀⢸⡇⠀⠀⠈⣿⡛⠻⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣵⠏⠀⠀⠻⠿⠿⠿⠋⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏⠀⣤⣤⡄⣠⣤⣤⣀⢠⣄⢠⣭⣷⣖⢾⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⢀⣿⣟⣻⡏⠀⠘⣿⢸⣼⡟⠀⠈⠛⠻⣬⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠏⠛⠁⠀⠉⢁⣀⣦⡻⣿⠟⠁⠀⠀⠀⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⣿⠀⠀⠀⠀⢰⣿⠉⠉⠉⠛⢶⡄⠀⠀⠀⠀⢸⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠀⠀⠀⠀⢸⣿⠁⠀⠀⠀⢸⡇⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⣠⣶⣦⣄⣿⡄⠀⠀⠀⣸⣇⡀⠀⠀⠀⠸⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠃⣻⣏⣾⡿⠻⣷⣅⠀⠀⠀⢻⣿⣟⣿⢦⡀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠶⠿⠿⣿⠀⠀⠈⣿⡄⠀⠀⢸⣿⠿⠾⢿⣽⠶⢶⣾⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⣀⣠⡤⠤⣿⡇⠀⠀⠀⢿⣦⡀⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣥⣬⣭⣭⠥⠶⠞⠛⠛⠋⠁⠀⠀⠀⠈⢳⣝⡲⢤⡀⠀⠀⢹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠶⣯⣙⣒⣒⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
}
