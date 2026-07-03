# Contact Book Management System

## Project Overview

The Contact Book Management System is a Python-based console application that allows users to manage personal contacts efficiently. The application stores contact information permanently using a JSON file, allowing data to remain available even after the program is closed.

The project demonstrates the use of Python functions, file handling, JSON manipulation, regular expressions, loops, conditional statements, list operations, and exception handling.

---

## Features

- Add New Contact
- View All Contacts (Sorted Alphabetically)
- Search Contact by Name or Phone Number
- Update Existing Contact
- Delete Contact
- View Recently Added Contacts
- Data Persistence using JSON
- Duplicate Contact Prevention
- Input Validation
- Exception Handling

---

## Technologies Used

- Python 3.x
- JSON
- Regular Expressions (re module)
- OS module

---

## Project Structure

```
Contact Book Management System/
│
├── contact_book.py
├── contacts.json
└── README.md
|___Screenshots
```

---

## Contact Information Stored

Each contact contains the following fields:

- Name
- Phone Number
- Email Address

Example:

```json
[
    {
        "name": "Rahul Sharma",
        "phone": "9876543210",
        "email": "rahul@gmail.com"
    }
]
```

---

## Functionalities

### 1. Add Contact

Allows the user to add a new contact.

Validation includes:

- Name should contain only alphabets.
- Phone number must contain exactly 10 digits.
- Phone number should begin with 6, 7, 8 or 9.
- Email must follow a valid email format.
- Duplicate names, phone numbers, and email addresses are not allowed.

---

### 2. View Contacts

Displays all contacts.

Features:

- Contacts are sorted alphabetically.
- Displays Name, Phone Number, and Email Address.

---

### 3. Search Contact

Allows searching using:

- Contact Name
- Phone Number

Partial name matching is supported.

---

### 4. Update Contact

Allows updating:

- Name
- Phone Number
- Email Address

Users may leave any field blank to keep the previous value.

All updated values are validated before saving.

---

### 5. Delete Contact

Deletes a contact using:

- Name
- Phone Number

---

### 6. Recently Added Contacts

Displays the last three contacts added to the contact book.

---

## Data Storage

All contact information is stored inside:

```
contacts.json
```

The data is automatically saved after:

- Adding a contact
- Updating a contact
- Deleting a contact

---

## Input Validations

### Name Validation

- Cannot contain numbers.
- Cannot contain special characters.
- Spaces between words are allowed.

Example:

```
Rahul Sharma ✔
Rahul123 ✖
Rahul@ ✖
```

---

### Phone Number Validation

Rules:

- Must contain exactly 10 digits.
- Only digits allowed.
- Must start with:

```
6
7
8
9
```

Example:

```
9876543210 ✔
1234567890 ✖
98765abcde ✖
```

---

### Email Validation

Uses Regular Expressions.

Valid examples:

```
abc@gmail.com
john123@yahoo.com
hello.world@outlook.com
```

Invalid examples:

```
abcgmail.com
abc@
@gmail.com
```

---

## Exception Handling

The application safely handles:

- Missing JSON file
- Corrupted JSON file
- File reading errors

Instead of crashing, the application starts with an empty contact list.

---

## Concepts Used

- Functions
- Loops
- Lists
- Dictionaries
- JSON File Handling
- Exception Handling
- Regular Expressions
- Input Validation
- Searching
- Sorting
- CRUD Operations

---

## Future Enhancements

- GUI using Tkinter
- Web Application using Flask
- Import and Export Contacts
- Contact Groups
- Favorite Contacts
- Password Protection
- Contact Images
- Birthday Reminder
- CSV Support

---

## How to Run

Step 1

Install Python 3.

Step 2

Download the project.

Step 3

Open terminal.

Step 4

Run:

```
python contact_book.py
```

---

## Author

Prateek Goswami
