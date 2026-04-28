contacts = {
    "paula": { 
        "phone": "5005005000",
        "email": "paula@python.py",
    },
    "ana": {
        "phone": "4004004000",
        "email": "ana@python.py"
    }
}

def add_contact(contacts: dict, contact_info: tuple) -> str:
    name, phone, email = contact_info
    name = name.lower()
    if name in contacts:
        return f"Contact '{name}' already exists!"
    else:
        contacts[name] = {"phone": phone, "email": email}
        return f"Contact '{name}' added successfully!"
    
def update_contact(contacts: dict, name: str, new_info: tuple) -> str:
    phone, email = new_info
    name = name.lower()
    if name in contacts:
        contacts[name] = {"phone": phone, "email": email}
        return f"Contact '{name}' updated successfully!"
    else:
        return f"Contact '{name}' does not exist!"
    
def delete_contact(contacts: dict, name: str) -> str:
    name = name.lower()
    if name in contacts:
        contacts.pop(name)
        return f"Contact '{name}' deleted successfully!"
    else:
        return f"Contact '{name}' not found!"

def search_contact(contacts: dict, name: str) -> str:
    name = name.lower()
    if name in contacts:
        phone = contacts[name]["phone"] 
        email = contacts[name]["email"]
        return f"Name: {name} | Phone: {phone} | Email: {email}"
    else:
        return f"Contact '{name}' not found!"
    
def view_contacts(contacts: dict) -> str:
    if contacts == {}:
        return "No contacts available."
    else: 
        contact = ""
        for name, info in contacts.items():
            phone = info["phone"]           
            email = info["email"]
            contact += f"Name: {name} | Phone: {phone} | Email: {email}\n"
    return f"Contact Book:\n{contact}"

if __name__ == "__main__":
    # --- Testing ---

    # add_contact
    print(add_contact(contacts, ("Paula", "1231231234", "paula@test.com")))   # Contact 'paula' already exists!
    print(add_contact(contacts, ("karla", "1231231234", "karla@test.com")))   # Contact 'karla' added successfully!

    # update_contact
    print(update_contact(contacts, "ana", ("9999999999", "ana@new.com")))     # Contact 'ana' updated successfully!
    print(update_contact(contacts, "mario", ("8888888888", "mario@new.com"))) # Contact 'mario' does not exist!

    # delete_contact
    print(delete_contact(contacts, "Ana"))                                     # Contact 'ana' deleted successfully!
    print(delete_contact(contacts, "mario"))                                   # Contact 'mario' not found!

    # search_contact
    print(search_contact(contacts, "Paula"))                                   # Name: paula | Phone: 5005005000 | Email: paula@python.py
    print(search_contact(contacts, "mario"))                                   # Contact 'mario' not found!

    # view_contacts
    print(view_contacts(contacts))                                             # Contact Book: + remaining contacts
    print(view_contacts({}))                                                   # No contacts available.
