import random
import settings

difficulty_percentage = random.random()

Slime = 0.60
Ghoul = 0.20
Zombie = 0.10

if difficulty_percentage >= Slime:
    print("Slime Spawned!")
elif difficulty_percentage <= Slime and difficulty_percentage >= Ghoul:
    print("Ghoul Spawned!")
elif difficulty_percentage <= Ghoul and difficulty_percentage >= Zombie:
    print("Zombie!")
