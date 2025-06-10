#연락처 검색색
def search_contact(keyword):
    contacts = load_contacts()
    results = [c for c in contacts if keyword.lower() in c['name'].lower()]
    for contact in results:
        print(f"{contact['name']} - {contact['phone']}")
