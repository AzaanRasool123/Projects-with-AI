# adventure_game.py

# Game data
game_data = {
    "rooms": {
        "entrance_hall": {
            "description": "You are standing in the entrance hall of the lost temple.",
            "items": ["torch", "map"],
            "exits": {"north": "anteroom", "east": "library"}
        },
        "anteroom": {
            "description": "You are in a small anteroom.",
            "items": [],
            "exits": {"south": "entrance_hall"}
        },
        "library": {
            "description": "You are in a vast library.",
            "items": ["book"],
            "exits": {"west": "entrance_hall"}
        },
        "treasury": {
            "description": "You are in the treasury of the lost temple.",
            "items": ["treasure"],
            "exits": {"south": "library"}
        },
        "garden": {
            "description": "You are in a beautiful garden.",
            "items": [],
            "exits": {"north": "library"}
        }
    },
    "player": {
        "location": "entrance_hall",
        "inventory": []
    }
}

# Game functions
def describe_room(room_name):
    room = game_data["rooms"][room_name]
    print(room["description"])
    print("You see the following items:")
    for item in room["items"]:
        print(f"  * {item}")
    print("You can go:")
    for direction, exit_room in room["exits"].items():
        print(f"  * {direction} to {exit_room}")

def move_player(direction):
    current_room = game_data["player"]["location"]
    room_exits = game_data["rooms"][current_room]["exits"]
    if direction in room_exits:
        game_data["player"]["location"] = room_exits[direction]
        describe_room(game_data["player"]["location"])
    else:
        print("You can't go that way!")

def take_item(item_name):
    current_room = game_data["player"]["location"]
    room_items = game_data["rooms"][current_room]["items"]
    if item_name in room_items:
        game_data["player"]["inventory"].append(item_name)
        room_items.remove(item_name)
        print(f"You took the {item_name}!")
    else:
        print("You don't see that item here!")

def inventory():
    print("You have the following items:")
    for item in game_data["player"]["inventory"]:
        print(f"  * {item}")

def play_game():
    while True:
        describe_room(game_data["player"]["location"])
        command = input("> ").lower()
        if command.startswith("go "):
            direction = command[3:]
            move_player(direction)
        elif command.startswith("take "):
            item_name = command[5:]
            take_item(item_name)
        elif command == "inventory":
            inventory()
        elif command == "quit":
            print("Goodbye!")
            break
        else:
            print("I didn't understand that command!")

# Start the game
play_game()