import json
import os
import re

FILE_NAME = "contacts.json"
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# -------------------- File Handling --------------------#

def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []

def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

contacts = load_contacts()

# -------------------- Functions --------------------#

def add_contact():
    name = input("Enter Name: ").strip()

#name validation no numbers or special characters
    if not name.replace(" ", "").isalpha():
        print("Invalid name! Please enter a valid name without numbers or special characters.")
        return
    phone = input("Enter Phone Number: ").strip()

    if not phone.isdigit() or len(phone) != 10 or phone[0] not in "6789":
        print("Invalid phone number! Please enter a 10-digit number starting with 6, 7, 8, or 9.")
        return

    email = input("Enter Email: ").strip()
   
 #email validation
  
    if not re.match(email_pattern, email):
       print("Invalid email! Please enter a valid email address.")
       return

# Check duplicates
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact name already exists.")
            return
        elif  contact["phone"] == phone:
            print("phone number already exists.")
            return
        elif contact["email"].lower() == email.lower():
            print("email already exists.")
            return

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(new_contact)
    save_contacts()

    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    sorted_contacts = sorted(contacts, key=lambda x: x["name"].lower())

    print("\n----- Contact List -----")
    for i, contact in enumerate(sorted_contacts, start=1):
        print(f"\nContact {i}")
        print("Name :", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])

def search_contact():
    key = input("Enter Name or Phone Number: ").strip()

    found = False

    for contact in contacts:
        if key.lower() in contact["name"].lower() or contact["phone"] == key:
            print("\nContact Found")
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("Contact not found.")

def update_contact():
    key = input("Enter Name or Phone Number to update: ").strip()

    for contact in contacts:
        if contact["name"].lower() == key.lower() or contact["phone"] == key:

            print("\nLeave blank to keep old value.")

            new_name = input("New Name: ").strip()
            new_phone = input("New Phone: ").strip()
            new_email = input("New Email: ").strip()

            if new_name:
                if not new_name.replace(" ", "").isalpha():
                    print("Invalid name! Please enter a valid name without numbers or special characters.")
                    return
                
 # Check if name already exists
                for c in contacts:
                    if c != contact and c["name"].lower() == new_name.lower():
                        print("Contact name already exists.")
                        return
                contact["name"] = new_name

            if new_phone:
                if not new_phone.isdigit() or len(new_phone) != 10 or new_phone[0] not in "6789":
                    print("Invalid phone number! Please enter a 10-digit number starting with 6, 7, 8, or 9.")
                    return
                
# Check if phone already exists
                for c in contacts:
                    if c != contact and c["phone"] == new_phone:
                        print("Phone number already exists.")
                        return
                contact["phone"] = new_phone

            if new_email:
                if not re.match(email_pattern, new_email):
                    print("Invalid email! Please enter a valid email address.")
                    return
                
# Check if email already exists
                for c in contacts:
                    if c != contact and c["email"].lower() == new_email.lower():
                        print("Email already exists.")
                        return
                contact["email"] = new_email

            save_contacts()
            print("Contact updated successfully.")
            return

    print("Contact not found.")

def delete_contact():
    key = input("Enter Name or Phone Number to delete: ").strip()

    for contact in contacts:
        if contact["name"].lower() == key.lower() or contact["phone"] == key:
            contacts.remove(contact)
            save_contacts()
            print("Contact deleted successfully.")
            return

    print("Contact not found.")

def show_recent():
    if not contacts:
        print("No contacts found.")
        return

    print("\nRecently Added Contacts")
    for contact in contacts[-3:]:
        print(f"{contact['name']} - {contact['phone']}")

# -------------------- Main Program ---------------------#

while True:
    print("\n===== Contact Book Management System =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Recently Added Contacts")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        show_recent()

    elif choice == "7":
        print("Thank you for using Contact Book Management System.")
        break

    else:
        print("Invalid choice. Please try again.")