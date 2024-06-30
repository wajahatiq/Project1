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


def change_price(item_name, item_price):
    if item_name in inventory:
        inventory[item_name]['price'] = item_price
        save_inventory()
        print()
        print(f'The new price of {item_name} is PKR{item_price}')
    else:
        print(f'{item_name} is not present in inventory.')


def update_inventory (item_name, Item_count):
    if item_name in inventory:
        inventory[item_name]['count'] = Item_count
        save_inventory()
        print()
        print(f'{item_name} quantity has been updated to {Item_count} units.')


def display_inventory ():
    print()
    print("\n===== Current Inventory =====")
    print('{:<20}{:<10}{:<10}'.format('item Name','Units','Price'))
    print('='*40)
    for x, y in inventory.items():
        item_name = x
        units = y['count']
        price = y['price']
        print("{:<20} {:<8} PKR{:<8}".format(item_name, units, price))
    print("=" * 40)


def save_inventory():
    with open ('a.json', 'w') as f:
        json.dump(inventory, f, indent=4)


def main ():
    while True:
        print("\n===== Inventory Management System =====")
        print()
        print('1. Add New Items')
        print('2. Buy Items')
        print('3. Change Item Price')
        print('4. Change Item Quantity')
        print('5. Display Inventory')
        print('6. View Total Sales Amount')
        print('7. Exit')


        choice = int(input('Please enter your choice:'))
        if choice == 1:
            item_name = input('Please enter item name:')
            Item_count = int(input('Please enter number of item:'))
            Item_price= float(input('Please enter price of item:'))
            add_item(item_name, Item_count, Item_price)
        elif choice == 2:
            item_name = input('Please enter item name:')
            Item_count = int(input('Please enter number of item:'))
            buy_item (item_name, Item_count)
        elif choice == 3:
            item_name = input('Please enter item name:')
            Item_price= float(input('Please enter new price of item:'))
            change_price (item_name, Item_price)    
        elif choice == 4:
            item_name = input('Please enter item name:')
            Item_count = int(input('Please enter the new quantity of the item:'))
            update_inventory (item_name, Item_count)
        elif choice == 5:
            display_inventory()
        elif choice == 6:
            print(f"Total Sales Amount is: PKR{total_sales}.")  
        elif choice == 7:
            print("Exiting programme.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 to 7.")     

main()
