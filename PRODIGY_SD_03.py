import json
import os

# Define the file to store contacts
CONTACTS_FILE = 'contacts.json'

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if contacts:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts found.")

# Edit a contact
def edit_contact():
    contacts = load_contacts()
    view_contacts()
    index = int(input("Enter the number of the contact you want to edit: ")) - 1
    if 0 <= index < len(contacts):
        contact = contacts[index]
        contact['name'] = input(f"Enter new name (current: {contact['name']}): ") or contact['name']
        contact['phone'] = input(f"Enter new phone number (current: {contact['phone']}): ") or contact['phone']
        contact['email'] = input(f"Enter new email address (current: {contact['email']}): ") or contact['email']
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

# Delete a contact
def delete_contact():
    contacts = load_contacts()
    view_contacts()
    index = int(input("Enter the number of the contact you want to delete: ")) - 1
    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Invalid contact number.")

# Main program loop
def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            contacts = load_contacts()
            add_contact(contacts)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
