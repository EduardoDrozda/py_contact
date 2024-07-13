contacts = [];


def add_contact(contact):
    id = len(contacts) + 1
    contact["id"] = id
    contacts.append(contact)

def view_contacts():
    for contact in contacts:
        print(f"Id: {contact['id']}")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Favorite: {contact['favorite']}")
        print("\n")
    

def favorite_contacts(id):
    task = next((contact for contact in contacts if contact["id"] == id), None)
    
    if task:
        task["favorite"] = True
        print("Contact added to favorites")
        return
    
    print("Contact not found")

def view_favorites_contacts():
    for contact in contacts:
        if contact["favorite"]:
            print(f"Id: {contact['id']}")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Favorite: {contact['favorite']}")
            print("\n")

def delete_contact(id):
    task = next((contact for contact in contacts if contact["id"] == id), None)
    
    if task:
        contacts.remove(task)
        print("Contact deleted")
        return
    
    print("Contact not found")

while True:
    print("\n Menu: Contacts")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Favorite Contacts")
    print("4. View Favorite Contacts")
    print("5. Delete Contact")
    print("6. Exit")
    
    choosen_option = int(input("Choose an option: "))
    
    match choosen_option:
        case 1:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            favorite = input("Enter favorite (yes/no): ")
            isFavorite = favorite == "yes"
            contact = {
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": isFavorite
            }
            
            add_contact()
        case 2:
            view_contacts()
        case 3:
            favorite_contacts()
        case 4:
            view_favorites_contacts()
        case 5:
            delete_contact()
        case 6:
            break
        case _:
            print("Invalid option")
    
print("Goodbye!") 