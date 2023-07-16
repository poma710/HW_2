def input_num():
    ask = int(input("Выбери действие:\n1 - Записать нового пользователя: \n2- Изменить: " ))
    return ask

def input_name():
    pass

#id, ФИО, дата рождения
#1) Ввод нового пользователя
#2) Поиск по характеристике - ввод характеристики

def input_found():
    found = input("Введите параметр для поиска /n")
    search_line = input("Введите ФИО или номер для поиска: ")
    with open("telefonNum.txt", "r", encoding='utf-8') as file:
        tel_book = file.read()
        find_list = search(tel_book, search_line)
        return find_list
def search(book: str, search_str: str):
    book = book.split("\n")
    result = []
    for line in book:
        if search_str in line:
            result.append(line)
    return result


def edit_data():
    with open("telefonNum.txt", "r", encoding='utf-8') as f:
        tel_book = f.read()
    tel_book_lines = tel_book.split("\n")
    target_line = find_one_line("telefonNum.txt")
    while len(target_line) == 0:
        target_line = find_one_line("telefonNum.txt")
    edited_line = edit_line(target_line)
    tel_book_lines[tel_book_lines.index(target_line)] = edited_line
    print(f"Запись - {target_line}, изменена на - {edited_line}")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))


def edit_line():
    elements = line.split(" | ")
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    if len(fio) == 0:
        fio = elements[0]
    if len(phone) == 0:
        phone = elements[1]
    return f"{fio} | {phone}"


def remove_data():
    with open("telefonNum.txt", "r", encoding='utf-8') as f:
        tel_book = f.read()
    tel_book_lines = tel_book.split("\n")
    find_list = find_data("telefonNum.txt")
    while len(find_list) == 0:
        find_list = find_data("telefonNum.txt")
    if len(find_list) > 0:
        print("Найдены записи:")
        for index in range(len(find_list)):
            print(f"{index + 1} - {find_list[index]}")
        index_for_remove = int(
            input("Введите номер строки для удаления, или 0 для удаления всех найденных строк: ")) - 1
        if 0 <= index_for_remove < len(find_list):
            print(f"Удалена запись: {find_list[index_for_remove]}")
            tel_book_lines.pop(tel_book_lines.index(find_list[index_for_remove]))
        elif index_for_remove == -1:
            for index in find_list:
                tel_book_lines.pop(tel_book_lines.index(index))
            print(f"Удалено записей: {len(find_list)}")
        else:
            print("Удалено записей: 0")
    with open("telefonNum.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))


close = False
print("Программа для редактирование и отображения данных справочника.")
file_phone_book = "phone_book.txt"
with open(file_phone_book, "a", encoding="utf-8") as file:
    file.write("")

while not close:
    print("Введите: 1 - просмотр, 2 - добавление, 3 - поиск, 4 - изменение, 5 - удаление, 6 - выход")
    action = int(input("Действие: "))
    if action == 1:
        show_data(file_phone_book)
    elif action == 2:
        add_data(file_phone_book)
    elif action == 3:
        for i in find_data(file_phone_book):
            print(i)
    elif action == 4:
        edit_data(file_phone_book)
    elif action == 5:
        remove_data(file_phone_book)
    else:
        close = True   