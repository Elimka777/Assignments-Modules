# contacts_manager.py

contacts = []

def add_contact(name, phone):
    contacts.append({'name': name, 'phone': phone})
    return f"Contact {name} added successfully."

def remove_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'] != name]
    return f"Contact {name} removed successfully."

def display_contacts():
    if not contacts:
        return "No contacts available."
    contact_list = "\n".join([f"Name: {contact['name']}, Phone: {contact['phone']}" for contact in contacts])
    return contact_list
