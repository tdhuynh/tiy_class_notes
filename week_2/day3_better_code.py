# NEW FILE EDIT THIS FILE
# Inventory Tracker RPG

# Player
# Inventory
# Items

# functions should only mutate variables that they are give or that they create themselves
# functions should only mutate variables that they are give or that they create themselves
# functions should only mutate variables that they are give or that they create themselves

# mutating player dict by side effect
# if you're just calling a function but not assigning it, you don't need to return it

def add_item_to_inventory(player):
    item_name = input("What is the item name? ")
    item_quantity  = int(input("How many? "))
    # ??? is item already in inventory?
    # if it is, just add quantity - don't replace
    if item_name in player["inventory"].keys():
        #updating quantity of existing items
        player["inventory"][item_name]["quantity"] += item_quantity
    else:
        #adding new item with quantity
        player["inventory"][item_name] = {"quantity": item_quantity}

def inspect_inventory(player):
    for item in player["inventory"].keys():
        quantity = player["inventory"][item]["quantity"]
        print("{} - {}".format(item, quantity))

def player_input(player, choice):
    if choice == 'a':
        add_item_to_inventory(player)
    elif choice == 'i':
        inspect_inventory(player)

def make_character():
    player = {"inventory": {"red potion": {"quantity": 20}}}
    player_name = input("Welcome Traveler! What is your name? ")
    player["name"] = player_name
    return player

player = make_character()  # since the make_character() is returning player, we set player = make_character()

while True:
    choice = input("Would you like to (i)nspect your inventory? or (a)dd to inventory?\n>>> ")
    player_input(player, choice)



# refactoring works best from inside out, not top to bottom
# functions should only mutate variables that they are give or that they create themselves
#
