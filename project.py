#연락처 수정
def load_contacts():
    pass

def save_contacts():
    pass


def edit_contact(old_name, new_name, new_phone):
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'] == old_name:
            contact['name'] = new_name
            contact['phone'] = new_phone
            break
    save_contacts(contacts)
