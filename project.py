
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

#연락처 검색
def search_contact(keyword):
    contacts = load_contacts()
    results = [c for c in contacts if keyword.lower() in c['name'].lower()]
    for contact in results:
        print(f"{contact['name']} - {contact['phone']}")

#
def menu():
    while True:
        print("\n1. 추가 | 2. 수정 | 3. 삭제 | 4. 목록 | 5. 검색 | 0. 종료")
        choice = input("선택: ")

        if choice == "1":
            name = input("이름: ")
            phone = input("전화번호: ")
            add_contact(name, phone)
        elif choice == "2":
            old = input("수정할 이름: ")
            new = input("새 이름: ")
            phone = input("새 전화번호: ")
            edit_contact(old, new, phone)
        elif choice == "3":
            name = input("삭제할 이름: ")
            delete_contact(name)
        elif choice == "4":
            list_contacts()
        elif choice == "5":
            keyword = input("검색어: ")
            search_contact(keyword)
        elif choice == "0":
            break
        else:
            print("잘못된 입력입니다.")