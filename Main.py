import json

total_sales = 0
inventory = {}


def load_inventory():
    global inventory
    with open('a.json', 'r') as f:
            inventory = json.load(f)
load_inventory()



def add_item (item_name, Item_count, Item_price):
    if item_name not in inventory:
        inventory[item_name] = {'count':Item_count, 'price':Item_price}
        save_inventory()
        print(f'{item_name} added to inventory.')
        print(inventory)
    else:
        print(f'The {item_name} is already listed in inventory, please update item to make changes.')



def buy_item (item_name, Item_count):
    global total_sales
    if item_name in inventory and inventory[item_name]['count']>=Item_count:
         inventory[item_name]['count'] -= Item_count
         sale = Item_count * inventory[item_name]['price']
         total_sales += sale
         save_inventory()
         print(f'You have bought {Item_count}{item_name}. Total price is: PKR{sale}.')
         print('Remaining items in inventory are:')
         print(inventory)
    elif item_name in inventory:
        print(f'Entered quantity is not present. Available: {inventory[item_name]['count']}.')
    else:
        print(f'{item_name} is not present in inventory.')





def save_inventory():
    with open ('a.json', 'w') as f:
        json.dump(inventory, f, indent=4)



def main ():
    while True:
        print('1. Add new items')
        print('2. Buy items')

        choice = int(input('Please enter your choice:'))
        if choice == 1:
            item_name = input('Please enter item name:')
            Item_count = int(input('Please enter number of item:'))
            Item_price= float(input('Please enter price of item:'))
            add_item(item_name, Item_count, Item_price)
        if choice == 2:
            item_name = input('Please enter item name:')
            Item_count = int(input('Please enter number of item:'))
            buy_item (item_name, Item_count)


main()
