import json
a = 0
stars = {"id": 0, "name":"", "constellation": "", "is_visible": "", "radius": ""}
with open('.json', 'r') as file:
    data = json.load(file)
    while a!= 5: 
        k = 0
        print("Вывести все записи\n2 - Вывести запись по полю\n3")