import random

print("Welcome to Dragon Quest 2024!")
print("Write a better game description here.")
print()

player_name = input("What's your name, adventurer? ")
print()

print(f"Hello, {player_name}! You are on a quest to find treasure.")
print("Along the way, you'll likely face some challenges, but the rewards outweigh the risks!")
print()

print("You are walking through a dark forest. You come across a fork in the road.")
print()

choice = input("Do you want to go left or right? Type 'left' or 'right': ")
print()

if choice == 'left':
    print("You walk down the left path and encounter a hungry wolf!")
    print()

    action = input("Do you want to fight the wolf or run? Type 'fight' or 'run': ")
    
    if action == "fight":
        # Simulate a 6-sided dice roll
        enemyRoll = random.randint(1, 6) 

        print("The wolf rears up at you ready to attack!")
        print()
        
        # Get player's number
        playerRoll = random.randint(1,6)

        print(f"Your skill check was {playerRoll} but the wolf's was {enemyRoll}")
        print()

        if playerRoll > enemyRoll:                
            print("You bravely fight the wolf and win!")
            print()
            print("You continue down the path and eventually find the treasure chest.")
        else:
            print("The wolf overpowers you. You lose the fight. Game over.")
        print()
            
    elif action == 'run':
        print("You run away safely, but lose some time.")
        print("You eventually you give up on the treasure hunting life and get some mead at the nearest inn.")
    else:
        print()
        print("You hesitated and the wolf attacked. Game over.")
    print()
        
elif choice == 'right':
    print("You walk down the right path and find a chest of gold!")
    print("When you get back to town, drinks are on you!")
else:
    print("You stand still, unsure of what to do. Game over.")
print()

