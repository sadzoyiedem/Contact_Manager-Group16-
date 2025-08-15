# Group 16 - Contact Management System
# This program allows users to manage contacts with options to add, update, delete, search,view.
contacts = {

}


def search_contact():
    search_name = input('Name to search: ').strip().lower()
    found = False
    for name, details in contacts.items():
        if search_name in name.lower():
            print(
                f'Name: {name}, Phone: {details["number"]}, Email: {details["email"]}')
            found = True
    if not found:
        print('No matching contact found.')


def update_contact():
    update_name = input('Name to update: ').strip().lower()
    found_contact = False
    for name, details in contacts.items():
        if update_name in name.lower():
            found_contact = True
            print(
                f"Update '{name}' contact details.\nCurrent details: Phone: {details['number']}\n Email: {details['email']}")
            number = input('Enter new phone number (10 digits): ').strip()
        while len(number) != 10:
            print('Invalid phone number. It should be 10 digits.')
            number = input('Enter new phone number (10 digits): ').strip()
        contacts[name]['number'] = number
        email = input('Enter new email: ').strip()
        while not email or '@' not in email or '.' not in email:
            print('Invalid email format. It should contain "@" and "."')
            email = input('Enter new email: ').strip()
        contacts[name]['email'] = email
        print(f'Contact {name} updated successfully.')
    if not found_contact:
        print('Contact not found.')


def delete_contact():
    name = input('Name to delete: ').strip()
    if name in contacts:
        del contacts[name]
        print(f'Contact "{name}" deleted successfully.')
    else:
        print('Contact not found.')


def add_contact():
    name = input('New contact name: ').strip()
    if name in contacts:
        print('Contact already exists.')
    else:
        number = input('Enter phone number: ').strip()
        while not number.isdigit() or len(number) != 10:
            print('Invalid phone number. It should be 10 digits.')
            number = input('Enter phone number: ').strip()
        email = input('Enter email: ').strip()
        while not email or '@' not in email or '.' not in email:
            print('Invalid email format. It should contain "@" and "."')
            email = input('Enter email: ').strip()
        contacts[name] = {'number': number, 'email': email}
        print(f'Contact {name} added succesfully.')


def view_contacts():
    if contacts:
        for name, details in contacts.items():
            print(
                f'Name: {name}, Phone:{details["number"]}, Email: {details["email"]}')
    else:
        print('No contacts available.')


def main():
    while True:
        print('Choose an action: Search, Update, Delete, Add, View')
        action = input(': ').lower()

        if action in ['search', 's']:
            search_contact()
        elif action in ['update', 'u']:
            update_contact()
        elif action in ['delete', 'd']:
            delete_contact()
        elif action in ['add', 'a']:
            add_contact()
        elif action in ['view', 'v']:
            view_contacts()
        elif action in ['q', 'quit']:
            break
        else:
            print(
                'Invalid action.\n Enter a valid action: Search, Update, Delete, Add, View or Quit.')


print('Welcome to the Contact Management System!')
print('You can add, search, update, delete, or view contacts.\n')

main()
