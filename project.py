
#파일 입출력
def load_contacts():
    if not os.path.exists(CONTACT_FILE):
        return []
    with open(CONTACT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(CONTACT_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)

#연락처 추가
def add_contact(name, phone):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)


#연락처 목록
def list_contacts():
    contacts = load_contacts()
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

#연락처 삭제
def delete_contact(name):
    contacts = load_contacts()
    contacts = [c for c in contacts if c['name'] != name]
    save_contacts(contacts)


#연락처 수정
def edit_contact(old_name, new_name, new_phone):
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'] == old_name:
            contact['name'] = new_name
            contact['phone'] = new_phone
            break
    save_contacts(contacts)