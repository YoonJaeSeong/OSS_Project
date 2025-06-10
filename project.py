#연락처 목록
def load_contacts():
    pass
def list_contacts():
    contacts = load_contacts()
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
