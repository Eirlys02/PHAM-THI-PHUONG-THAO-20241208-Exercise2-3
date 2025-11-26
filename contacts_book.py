# load contacts from file
def load_contacts():
    contacts_dict = {}
    try:
        with open("contacts.txt", "r", encoding= "utf-8") as f: #if you want to input Korean name
            for line in f:
                name, phone = line.strip().split(":")
                contacts_dict[name] = phone
    except FileNotFoundError:
        print("File not found. Starting with an empty contact list.")
    return contacts_dict

# validate phone number
def is_valid_phone(phone):
    if phone.startswith("+"):
        phone = phone[1:]
    return phone.isdigit()

# add a contact
def add_contact(contacts_dict):
    name = input("Enter the name: ").strip()
    while True:
        phone_number = input("Enter the phone number: ").strip()

        if is_valid_phone(phone_number):
            contacts_dict[name] = phone_number
            print("Contact added successfully.")
            break
        else:
            print("Invalid phone number!")
            print("Only digits (0-9) and optional '+' at the start are allowed. Please try again.")

# view all contacts
def view_contacts(contacts_dict):
    if not contacts_dict:
        print("The contact list is empty.")
    else:
        print("\n==== All Contacts ====")
        for name, phone_number in contacts_dict.items():
            print(f"- {name}: {phone_number}")

# search for a contact by name
def search_contact_by_name(contacts_dict):
    name = input("Enter the name: ").strip()
    if name in contacts_dict:
        print(f"Found: {name} - {contacts_dict[name]}")
    else:
        print("Contact not found.")

# save contacts to file
def save_contacts(contacts_dict):
    with open("contacts.txt", "w", encoding= "utf-8") as f:
        for name, phone_number in contacts_dict.items():
            f.write(f"{name}:{phone_number}\n")
    print("Contacts saved to file.")

contacts= load_contacts()

# menu loop
while True:
    print("\n1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact by name")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        search_contact_by_name(contacts)
    elif choice == "4":
        save_contacts(contacts)
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")    
