import json
def allrecords(data): #вывод всех записей
    for stars in data: #переборка всех записей и их вывод
        print(f'{stars["id"]}: {stars["name"]}, название созвездия: {stars["constellation"]}, радиус равен: {stars["radius"]}, видимость: {"да" if stars["is_visible"] else "нет"}\n')
def record1(data): # вывод определенной записи
    a = 0 #переменная для номера 
    flag = True #флаг для нахождения записи
    inpid = input("Введите поле выводимой записи: ")
    if inpid.isdigit():
        inpid = int(inpid)
    else:
        print("неправильный ввод\n")
        return 0
    for stars in data: #цикл с поиском записи
        a += 1
        if inpid == stars["id"]:
            print(f'{stars["id"]}: {stars["name"]}, название созвездия: {stars["constellation"]}, радиус равен: {stars["radius"]}, видимость: {"да" if stars["is_visible"] else "нет"}\n')
            flag = False
    print("Запись не найдена\n" if flag else "")
def newRecord(data): #создание записи
    newStar= {"id":0, "name":"", "constellation":"", "is_visible":False,"radius":0} #множество для добавляемой записи
    newStar["id"] = int(input("введите id: "))
    newStar["name"] = input("введите название звезды: ")
    newStar["constellation"] = input("введите название созвездия: ")
    try:
        newStar["is_visible"] = (True if newStar["constellation"] == "да" else "нет")
    except:
        print("неправильное значение\n")
    newStar["radius"] = int(input("введите радиус: "))
    data.append(newStar) # записывается в data
def deleteRecord(data):#удаления записи
    a = 0#переменная для номера записи
    flag = True#флаг для нахождения записи
    inpid = input("Введите поле записи для удвления: ")
    if inpid.isdigit():
        inpid = int(inpid)
    else:
        print("Некорректный ввод\n")
        return 0
    for stars in data: #цикл с поиском записи и удалением её из data
        if inpid == stars["id"]:
            data.pop(a) #удаляет и возвращает запись
            flag = False
        a += 1
    print("Запись не найдена\n" if flag else "")
def closingProg(data, num): #закрытие программы и перенос data в файл json
    print(f'Завершение работы программы. Было выполнено {num} действий')
    with open('stars.json', 'w', encoding='utf-8') as file: #инф записывается обратно в файл
        json.dump(data, file, indent=4, ensure_ascii=True)
    exit()
def menu(data, num): #меню
    print("1 - Вывести все записи\n2 - Вывести запись по полю\n3 - Добавить запись\n4 - Удалить запись по полю\n5 - Выйти из программы\n")
    b = int(input("Выберите действие(введите число): ")) #запрашивает действие пользователя в переменную
    if b == 1: #выводит все записи
        allrecords(data)
    elif b == 2:#выводит определенную запись введенную пользователем
        record1(data)
    elif b == 3: #ввод всех данных их запись и добав в data
        newRecord(data)
    elif b == 4: #находится id в файле и удаляет ее
        deleteRecord(data)
    elif b == 5: #завершается цикл
        closingProg(data, num) 
    else: #при вводе некорректного значения
        print('Введите корректное значение')
def main(): #главная функция
    num = 0
    with open('stars.json', 'r', encoding='utf-8') as file: #из json и записывается в data
        data = json.load(file)
        while True: #цикл повторяется постоянно
            menu(data, num) #запускается меню
            num += 1
main() #запуск