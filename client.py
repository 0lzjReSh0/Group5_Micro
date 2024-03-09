import requests

def add_part():
    name = input("Enter part name: ")
    description = input("descripton: ")
    quantity = input("Enter the number: ")
    part = {'name': name, 'description': description, 'quantity': quantity}
    response = requests.post('http://localhost:3000/parts', json=part)
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("failed")

def get_part(): 
    name = input("Enter the name you want to search: ")
    response = requests.get(f'http://localhost:3000/parts', params={'name': name})
    if response.status_code == 200:
        print("Information:", response.json())
    else:
        print("failed to get")

def add_part():
    name = input("Enter part name: ")
    description = input("Enter description: ")
    quantity = input("Enter the quantity: ")
    location = input("Enter the location: ")  
    status = input("Enter the status: ") 
    part = {'name': name, 'description': description, 'quantity': quantity, 'location': location, 'status': status}
    response = requests.post('http://localhost:3000/parts', json=part)
    print("Success:", response.json()) if response.status_code == 200 else print("Failed")

def get_part(): 
    name = input("Enter the name you want to search: ")
    response = requests.get(f'http://localhost:3000/parts', params={'name': name})
    print("Information:", response.json()) if response.status_code == 200 else print("Failed to get")

def add_or_update_inventory():
    category = input("Enter the category: ")
    part_id = input("Enter part ID: ")
    quantity = input("Enter the quantity: ")
    location = input("Enter the location: ")
    status = input("Enter the status: ")
    
    inventory_info = {
        'category': category,
        'part_id': part_id,
        'quantity': quantity,
        'location': location,
        'status': status
    }
    
    response = requests.post('http://localhost:3001/inventory', json=inventory_info)
    print("Success:", response.json()) if response.status_code == 200 else print("Failed")

def get_all_inventory():
    response = requests.get('http://localhost:3001/inventory/all')
    print("All inventory:") if response.status_code == 200 else print("Failed to retrieve inventory")
    print(response.json())

def get_inventory_by_category():
    category = input("Enter the category you want to view: ")
    response = requests.get(f'http://localhost:3001/inventory/{category}')
    print(f"Inventory for category '{category}':") if response.status_code == 200 else print("Failed to retrieve inventory for category")
    print(response.json())



def main():
    while True:
        print("1. Add new part")
        print("2. Query part")
        print("3. Add or update inventory")
        print("4. View all inventory")
        print("5. View inventory by category")
        print("6. Exit\n")
        choice = input(": ")

        if choice == '1':
            add_part()
        elif choice == '2':
            get_part()
        elif choice == '3':
            add_or_update_inventory()
        elif choice == '4':
            get_all_inventory()
        elif choice == '5':
            get_inventory_by_category()
        elif choice == '6':
            break
        else:
            print("Invalid input!")
            
if __name__ == '__main__':
    main()
    