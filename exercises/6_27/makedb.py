from person import Person, Manager  # Импортирует наши классы

bob = Person('Bob Smith')  # Создание объектов для сохранения
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')    # Имя файла хранилища
for obj in (bob, sue, tom):     # В качестве ключа исп-ть атрибут name
    db[obj.name] = obj          # Сохранить объект в хранилище
db.close()                      # Закрыть после внесения изменений
