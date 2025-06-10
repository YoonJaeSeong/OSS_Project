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
