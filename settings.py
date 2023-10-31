"""
    Script by Dichill

    Note:
            Everything in here can be customized, you can add your own Monsters, Items, and even your own Boss. 
        I made it like that, so anyone who is reading this that is new can play around with the settings and try to 
        understand how the code itself works. I have written comments to explain how the code works and how it correlates 
        with one another. I hope you have fun coding! Keep grinding y'all!

    - Dichill
"""

"""
    DEFAULT CONFIGURATION FOR SAVED.JSON
"""
CONFIG = {
    "name": "WithYouWithMe",
    "level": 1,
    "exp": 0,
    "weapon": "basic",
    "epilogue": 1,
    "health": 100,
    "potion": 1,
    "type": None,
    "monster_killed": 0,
    "total_dmgs": 0,
}

"""
    ALL TYPES OF WEAPONS
    SWORD | BOW | AXE
"""
SWORD_TYPE = {
    "Basic": "Wooden Sword",
    "Common": "Deshell's Sword",
    "Epic": "Samurai Sword",
    "Legendary": "Excalibur Sword",
}
SWORD_DMG = {
    "Basic": [4, 6],
    "Common": [6, 8],
    "Epic": [9, 11],
    "Legendary": [11, 22],
}

BOW_TYPE = {
    "Basic": "Wooden Bow",
    "Common": "Long Bow",
    "Epic": "Churchill's Bow",
    "Legendary": "Bow of Apollo",
}

BOW_DMG = {
    "Basic": [3, 4],
    "Common": [4, 7],
    "Epic": [8, 10],
    "Legendary": [15, 20],
}

AXE_TYPE = {
    "Basic": "Wooden Axe",
    "Common": "Stone Axe",
    "Epic": "Emerald Axe",
    "Legendary": "Leviathan Axe",
}

AXE_DMG = {
    "Basic": [4, 7],
    "Common": [7, 10],
    "Epic": [11, 14],
    "Legendary": [15, 22],
}

"""
    Weapons added to a dict to easily
    access them
"""
WEAPONS = {"Sword": SWORD_TYPE, "Bow": BOW_TYPE, "Axe": AXE_TYPE}
WPN_DMGS = {"Sword": SWORD_DMG, "Bow": BOW_DMG, "Axe": AXE_DMG}


"""
    How Lucky must the user be?
    From:
    - Getting Weapons
    - Damage
    - Fighting Monsters
"""
LUCK_PERCENTAGE = 0.4  # How lucky is the user for them to get an item?
PROBABILITY = 0.6  # Probability of a monster spawning
MONSTER_HIT_BACK = 0.4
HEALTH_POTION = 50  # How much Health the potion restores

"""
    To add your own monster, don't forget to edit
    MONSTERS
    MONSTERS_PERCENTAGE
    MONSTER_EXP
    MONSTER_DROPS
    MONSTER_ART (Optional, you still gotta create a key for it but you can leave it as "")
"""

# MONSTER CONFIGURATION
MONSTERS = ["Slime", "Ghoul", "Zombie"]  # Monsters within the Game
MONSTER_PERCENTAGE = [0.5, 0.3, 0.2]  #
MONSTER_EXP = [30, 50, 70]
MONSTER_DMG = [5, 10, 20]

# MONSTER DROPS
SLIME_DROPS = ["Common", "Health Potion", "Health Potion"]
GHOUL_DROPS = ["Epic", "Common", "Health Potion", "Health Potion"]
ZOMBIE_DROPS = [
    "Legendary",
    "Epic",
    "Common",
    "Health Potion",
    "Health Potion",
    "Health Potion",
]

# ALL OF THE MONSTERS DROPS
MONSTER_DROPS = {
    "Slime": SLIME_DROPS,
    "Ghoul": GHOUL_DROPS,
    "Zombie": ZOMBIE_DROPS,
}

"""
    THE FINAL BOSS :-O
"""
BOSS = ["WithYouWithMe"]
BOSS_DROP = [
    "The Undefeatable"
]  # What drop should the boss give? In this case its a title.
BOSS_HP = 200
BOSS_FIGHT_BACK = [0.65]
BOSS_DMG = [69]

"""
    STORY MODE CONFIGS
"""
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

EPILOGUE_THREE = [
    """Well, well, well...... Seems like a hero who wishes death dare comes to me? You won't be able to escape from me...""",
    """Let us see what you can do! Hunter!""",
    """Congratulations Hunter {0}... You haved saved everyone! Keep pushing forward and be you, hunter. I'll see you again in the next journey my friend.""",
]

TITLE = """ __    __   __    __  .__   __. .___________. _______ .______      
|  |  |  | |  |  |  | |  \ |  | |           ||   ____||   _  \     
|  |__|  | |  |  |  | |   \|  | `---|  |----`|  |__   |  |_)  |    
|   __   | |  |  |  | |  . `  |     |  |     |   __|  |      /     
|  |  |  | |  `--'  | |  |\   |     |  |     |  |____ |  |\  \----.
|__|  |__|  \______/  |__| \__|     |__|     |_______|| _| `._____|
"""

"""
    MONSTER ART
"""
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


WYWM_ALL_ARTS = [
    r"""
 __          ____     ____          ____  __ 
 \ \        / /\ \   / /\ \        / /  \/  |
  \ \  /\  / /  \ \_/ /  \ \  /\  / /| \  / |
   \ \/  \/ /    \   /    \ \/  \/ / | |\/| |
    \  /\  /      | |      \  /\  /  | |  | |
     \/  \/       |_|       \/  \/   |_|  |_|
""",
    r"""
               __   __               __  __   
 __        __  \ \ / /__        __ U|' \/ '|u 
 \"\      /"/   \ V / \"\      /"/ \| |\/| |/ 
 /\ \ /\ / /\  U_|"|_u/\ \ /\ / /\  | |  | |  
U  \ V  V /  U   |_| U  \ V  V /  U |_|  |_|  
.-,_\ /\ /_,-.-,//|(_.-,_\ /\ /_,-.<<,-,,-.   
 \_)-'  '-(_/ \_) (__)\_)-'  '-(_/  (./  \.)  
""",
    r"""
        _           _        _         _             _   _       
       / /\      _ /\ \     /\_\      / /\      _   /\_\/\_\ _   
      / / /    / /\\ \ \   / / /     / / /    / /\ / / / / //\_\ 
     / / /    / / / \ \ \_/ / /     / / /    / / //\ \/ \ \/ / / 
    / / /_   / / /   \ \___/ /     / / /_   / / //  \____\__/ /  
   / /_//_/\/ / /     \ \ \_/     / /_//_/\/ / // /\/________/   
  / _______/\/ /       \ \ \     / _______/\/ // / /\/_// / /    
 / /  \____\  /         \ \ \   / /  \____\  // / /    / / /     
/_/ /\ \ /\ \/           \ \ \ /_/ /\ \ /\ \// / /    / / /      
\_\//_/ /_/ /             \ \_\\_\//_/ /_/ / \/_/    / / /       
    \_\/\_\/               \/_/    \_\/\_\/          \/_/        
""",
]

BOSS_ART = {"WYWM": WYWM_ALL_ARTS}

CONGRATS_TXT = r"""
   _____ ____  _   _  _____ _____         _______ _____ 
  / ____/ __ \| \ | |/ ____|  __ \     /\|__   __/ ____|
 | |   | |  | |  \| | |  __| |__) |   /  \  | | | (___  
 | |   | |  | | . ` | | |_ |  _  /   / /\ \ | |  \___ \ 
 | |___| |__| | |\  | |__| | | \ \  / ____ \| |  ____) |
  \_____\____/|_| \_|\_____|_|  \_\/_/    \_\_| |_____/ 
"""

DEAD_TXT = r"""
 ____  ____    __    ____  
(  _ \( ___)  /__\  (  _ \ 
 )(_) ))__)  /(__)\  )(_) )
(____/(____)(__)(__)(____/ 
"""
