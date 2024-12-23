'''
Write a program that starts with "Welcome to the Pirate Ship Adventure".
Ask the user to choose between "search for treasure" or "battle enemy ships".
If "search for treasure", ask whether to "dig on the island" or "explore the cave".
    If "dig on the island", print "You found a hidden treasure chest. You Win!"
    If "explore the cave", print "You were trapped inside. Game Over."
If "battle enemy ships", ask if they want to "attack" or "defend".
    If "attack", print "You won the battle. You Win!"
    If "defend", print "You were outnumbered. Game Over."
'''

print("Welcome to the Pirate Ship Adventure!")
choice = input("Do you want to 'search for treasure' or 'battle enemy ships'? ").lower()

if choice == "search for treasure":
    action = input("Do you want to 'dig on the island' or 'explore the cave'? ").lower()
    if action == "dig on the island":
        print("You found a hidden treasure chest. You Win!")
    elif action == "explore the cave":
        print("You were trapped inside. Game Over.")
    else:
        print("Invalid choice.")
elif choice == "battle enemy ships":
    action = input("Do you want to 'attack' or 'defend'? ").lower()
    if action == "attack":
        print("You won the battle. You Win!")
    elif action == "defend":
        print("You were outnumbered. Game Over.")
    else:
        print("Invalid choice.")
else:
    print("Invalid choice.")