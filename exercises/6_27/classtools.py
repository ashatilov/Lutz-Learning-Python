# Файл classtools.py (новый)
# "Различные утилиты и инструменты для работы с классами"

class AttrDisplay:
    """
    Реализует наследуемый метод перегрузки операции вывода, отображающий
    имена классов экземпляров и все атрибуты в виде пар имя=значение,
    имеющиеся в экземплярах (исключая атрибуты, унаследованные от классов).
    Может добавляться в любые классы и способен работать с любыми
    экземплярами.
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)
    
    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())
    
if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2
        
    class SubTest(TopTest):
        pass
    
    X, Y = TopTest(), SubTest()
    print(X)    # Выведет все атрибуты экземпляра
    print(Y)    # Выведет имя класса,
                # самого близкого в дереве наследования
