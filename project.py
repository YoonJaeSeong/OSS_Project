def delete_contact(name):
    contacts = load_contacts()
    contacts = [c for c in contacts if c['name'] != name]
    save_contacts(contacts)
