#파일 입출력력
def load_contacts():
    if not os.path.exists(CONTACT_FILE):
        return []
    with open(CONTACT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(CONTACT_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)
