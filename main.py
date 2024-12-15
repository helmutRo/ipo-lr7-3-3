import json #подключение модуля
a = 0 # пользователь вводит пункт
stars = {"id": 0, "name":"", "constellation": "", "is_visible": "", "radius":0 } #для добавлния
with open('stars.json', 'r', encoding='utf-8') as file: # открывает файл и запись в data
    data = json.load(file)
    while a!= 5: #цикл повторяется пока не будет введен 5 
        k = 0 #нахождение порядка записи 
        flage = True
        print("1 - Вывести все записи\n2 - Вывести запись по полю\n3 - Добавить запись\n4 - Удалить запись по полю\n5 - Выйти из программы\n")
        a = int(input("выберите действие: ")) #запрашивает действие
        if a == 1: #выводит все 
            print(" ")
            for star in data:
                print(f'{star["id"]}: {star["name"]}, название созвездия: {star["constellation"]}, радиус равен: {star["radius"]}, видимость: {'да' if star["is_visible"] else 'нет'}\n')
        elif a == 2: #поле записи для пользователя
            inid = int(input("введите поле выводимой записи: "))
            for star in data:
                k += 1
                if inid == star["id"]:
                    print(f'{star["id"]}: {star["name"]}, название созвездия: {star["constellation"]}, радиус равен: {star["radius"]}, видимость: {'да' if star["is_visible"] else 'нет'}\n')
                    flage = False
            print("нужная запись не найдена\n" if flage else "")        
        elif a == 3: #ввод данных
            stars["id"] = int(input("введите id: "))
            stars["name"] = input("введите название звезды: ")
            stars["constellation"] = input("введите название созвездия: ")
            stars["is_visible"] = (True if stars["constellation"] == 'да' else 'нет')
            stars["radius"] = int(input("введите радиус: "))
            data.append(stars)
        elif a == 4: #нахождение id в файле и последующее удаление       
            inid = int(input("введите поле для удаления: "))
            for star in data:
                if inid == star["id"]:
                    data.pop(k)
                    flage = False  
                k += 1
            print("нужная запись не найдена\n" if flage else "") 
        elif a == 5: #завершение цикла
            print('завершение работы программы')
            break
        else: #при вводе неправильного
            print('введите правильное значение') 
with open('stars.json', 'w', encoding='utf-8') as file: #инф заноситься обратно в файл
    json.dump(data, file, indent=4, ensure_ascii=True)