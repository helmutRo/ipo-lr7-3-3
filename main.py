import json #подключение модуля
a = 0
stars = {"id": 0, "name":"", "constellation": "", "is_visible": "", "radius":0 }
with open('stars.json', 'r') as file:
    data = json.load(file)
    while a!= 5: 
        k = 0
        print("1 - Вывести все записи\n2 - Вывести запись по полю\n3 - Добавить запись\n4 - Удалить запись по полю\n5 - Выйти из программы\n6 - Вывести запись по полю\n")
        a = int(input("выберите действие: "))
        if a == 1:
            print(" ")
            for star in data:
                print(f"{star["id"]}: {star["name"]}, название созвездия: {star["constellation"]}, радиус равен: {star["radius"]}, видимость: {'да' if star["is_visible"] else 'нет'}\n")
        elif a == 2:
            inid = int(input("введите поле выводимой записи: "))
            for star in data:
                k += 1
                if inid == star["id"]:
                    print(f"{star["id"]}: {star["name"]}, название созвездия: {star["constellation"]}, радиус равен: {star["radius"]}, видимость: {'да' if star["is_visible"] else 'нет'}\n")
        elif a == 3:
            stars["id"] = int(input("введите id: "))
            stars["name"] = int(input("введите название звезды: "))
            stars["constellation"] = int(input("введите название созвездия: "))
            stars["is_visible"] = (True if stars["constellation"] == 'да' else 'нет')
            stars["radius"] = int(input("введите радиус: "))
            data.append(stars)
        elif a == 4:
            inid = int(input("введите поле для удаления: "))
            for star in data:
                if inid == star["id"]:
                    data.pop(k)
                k += 1
        elif a == 5:
            print('завершение работы программы')
            break
with open('stars.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=True)
