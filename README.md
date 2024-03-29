# ORG BOOK

Web-приоржение с возможностью ведения двух таблиц. Без данных.

### Стек:
* Python 3.9
* Django 4
* SQLite 3.4

## Запуск
Необходим python 3.

1) Необходимо скачать проект. Первый способ из консоли в среде разработке командой ```git clone https://github.com/Minigamy/org_book.git```. Второй способ, скачать проект архивом с github.
2) Установить зависимости командой ```pip install -r requirements.txt```
3) Сделать миграцию ```python manage.py migrate```
4) Запустить сервер ```python manage.py runserver```
5) Открыть в браузере ```http://127.0.0.1:8000/```



## Инструкция пользователя
<hr>
Данное web-приложение разработано для ведения двух справочников (Организационная структура и Сотрудники предприятия), с возможностью добавления/изменения/удаления записей в обеих таблицах.

Графический интерфейс содержит три основные страницы:
1) Главная страница. 
2) Страница со справочником по структуре
3) Страница со справочником по сотрудникам


На главной странице две кнопки "Организационная структура" и "Сотрудники предприятия" перенаправляют пользователя на страницу со справочником по структуре и на страницу со справочником по сотрудникам соответственно.

На страницах со справочниками реализована возможность Редактирования/Создания/Удаления записей в таблицах. Кнопка "Создать новую запись" открывает форму, которую необходимо заполнить данными. После нажатия кнопки "Save" данные будут сохранены в БД. Настроена валидация полей формы и всплывающие подсказки для корректного заполнения.

Кнопки Редактирования и Удаления записи соответствуют строке, которую они позволяют отредактировать или удалить.

<hr>

### SQL-запросы для создания таблиц


Создание таблицы: structure
```
create table structure
(
    structure_id INTEGER not null
        primary key,
    idup         INTEGER,
    name         TEXT    not null
);
```

Создание таблицы employee: 
```
create table employee
(
    id       INTEGER      not null
        primary key autoincrement,
    name     varchar(200) not null,
    orgid_id INTEGER      not null
        references structure(structure_id)            
);
```