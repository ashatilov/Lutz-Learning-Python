# nested2.py
from nested1 import X, printer # Копировать имена
X = 88     # Изменит только локальную версию “X”!
printer()  # X в nested1 по-прежнему будет равно 99
