import requests

def add_part():
    name = input("Enter part name: ")
    description = input("descripton: ")
    quantity = input("Enter the number: ")
    part_data = {'name': name, 'description': description, 'quantity': quantity}
    response = requests.post('http://localhost:3000/parts', json=part_data)
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

def main():
    while True:
        print("1. Add new part")
        print("2. query part")
        print("3. exit\n")
        choice = input(": ")

        if choice == '1':
            add_part()
        elif choice == '2':
            get_part()
        elif choice == '3':
            break
        else:
            print("Invalid input")

if __name__ == '__main__':
    main()
