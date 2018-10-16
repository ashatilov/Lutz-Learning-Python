# Файл person.py (окончательная версия)

from classtools import AttrDisplay
# Импортирует обобщенный инструмент

class Person(AttrDisplay):
    """
    Создает и обрабатывает записи с информацией о людях
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        
    def lastName(self):
        # Предполагается, что фамилия указана последней
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        # Процент – величина в диапазоне 0..1
        self.pay = int(self.pay * (1 + percent))

        
class Manager(Person):
    """
    Версия класса Person, адаптированная в соответствии
    со специальными требованиями
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
        
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
    
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)