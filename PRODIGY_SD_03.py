import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!\n")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nContacts List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()

# Edit a contact
def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter the contact number to edit: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            print("Leave field empty to keep current value.")
            name = input(f"Enter new name ({contact['name']}): ").strip()
            phone = input(f"Enter new phone ({contact['phone']}): ").strip()
            email = input(f"Enter new email ({contact['email']}): ").strip()
            
            if name:
                contact['name'] = name
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            
            save_contacts(contacts)
            print("Contact updated successfully!\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            save_contacts(contacts)
            print(f"Contact '{removed['name']}' deleted successfully!\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Main program loop
def main():
    contacts = load_contacts()
    
    while True:
        print("Contact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        print()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()