import json

total_sales = 0
inventory = {}


def add_item (item_name, Item_count, Item_price):
    if item_name not in inventory:
        inventory[item_name] = {'Count':Item_count, 'Price':Item_price}
        print(f'{item_name} added to inventory')
        print(inventory)
        save_inventory()
    else:
        print(f'The {item_name} is already listed in inventory, please update item to make changes.')


def save_inventory():
    with open ('a.json', 'w') as f:
        json.dump(inventory, f, indent=4)



def main ():
    while True:
        print('1. Add new items')

        choice = int(input('Please enter your choice:'))
        if choice == 1:
            item_name = input('Please enter item name:')
            Item_count = int(input('Please enter number of item:'))
            Item_price= float(input('Please enter price of item:'))
            add_item(item_name, Item_count, Item_price)

main()
