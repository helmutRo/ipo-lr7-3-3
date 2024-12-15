7. Задание 3

Написать программу которая:

- При запуске выводит меню из которого человек выбирает следующие пункты (*по средствам ввода номера пункта*):
    - Вывести все записи
    - Вывести запись по полю
    - Добавить запись
    - Удалить запись по полю
    - Выйти из программы
- После выполнения пунктов меню (*кроме “выйти из программы”*) меню отображается снова
- Все записи хранятся в виде `.json` файла (*любое название*)
- Пункт “**Вывести все записи**” — выводит в форматированном виде все записи из файла
- Пункт “**Вывести запись по полю**” — выводит одну запись по определённому полю (*поле `id`*), а так же ее позицию в словаре.
- Пункт “**Добавить запись**” — запрашивает у пользователя нужные данные и добавляет запись в файл
- Пункт “**Удалить запись по полю**” — удаляет запись из файла по определенному полю  (*поле `id`*)
- Пункт “**Выйти из программы**” — завершает выполнение программы, но перед этим вводит на экран количество выполненных операций с записями
- Пункты “**Вывести запись по полю**” и “**Удалить запись по полю**” должны выводить предупреждение если нужная запись не найдена
- Использовать функции запрещено
- Перед сдачей задание файл должен хранить 5 подготовленных записей
  Вариант 3

Программа должна хранить записи о звездах

Структура записи:

- `id` — номер записи
- `name` — общее название звезды
- `constellation` — название созвездия
- `is_visible` — хранить булевый тип данных, указывает на то можно ли увидеть звезду без телескопа
- `radius` — солнечный радиус звезды (подробнее https://ru.wikipedia.org/wiki/Солнечный_радиус)
  8. Создать новую ветку `feature/func` в репозитории с заданием :

Соединить ветку `feature/func` в ветку `main`
