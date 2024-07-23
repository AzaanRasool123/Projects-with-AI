import random

# Initialize player stats
health = 100
gold = 0

# Define the temple rooms
rooms = [
    {"name": "Entrance", "description": "You stand at the entrance of the temple."},
    {"name": "Dark Chamber", "description": "The room is dark and musty."},
    {"name": "Treasure Room", "description": "You see a chest filled with gold."},
    {"name": "Trap Room", "description": "You hear the sound of traps being set."},
    {"name": "Puzzle Room", "description": "You see a complex puzzle on the wall."},
]

# Define the player's current room
current_room = 0

while True:
    # Display the current room
    print(f"You are in the {rooms[current_room]['name']}.")
    print(rooms[current_room]["description"])

    # Get the player's action
    action = input("What do you do? (move, take, solve, rest) ")

    # Handle the player's action
    if action == "move":
        # Move to a random adjacent room
        next_room = random.choice([-1, 1])
        current_room = (current_room + next_room) % len(rooms)
    elif action == "take":
        # Take gold from the treasure room
        if current_room == 2:
            gold += 100
            print("You took 100 gold!")
        else:
            print("There's nothing to take here.")
    elif action == "solve":
        # Solve the puzzle in the puzzle room
        if current_room == 4:
            puzzle_solution = input("What's the answer to the puzzle? ")
            if puzzle_solution == "42":
                print("You solved the puzzle! You gain 50 health.")
                health += 50
            else:
                print("You failed to solve the puzzle. You lose 20 health.")
                health -= 20
        else:
            print("There's no puzzle to solve here.")
    elif action == "rest":
        # Rest and regain health
        health += 10
        print("You rested and regained 10 health.")
    else:
        print("Invalid action. Try again!")

    # Check if the player is dead
    if health <= 0:
        print("You died! Game over.")
        break

    # Display the player's stats
    print(f"Health: {health}, Gold: {gold}")