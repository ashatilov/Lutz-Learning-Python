"""
reloadall.py: транзитивная перезагрузка вложенных модулей
"""
import types
from imp import reload

def status(module):
    print('reloading ' + module.__name__)

def transitive_reload(module, visited):
    if not module in visited:  # Пропустить повторные посещения
        status(module)         # Перезагрузить модуль
        reload(module)         # И посетить дочерние модули
        visited[module] = None
        # Для всех атрибутов
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:
                # Рекурсия, если модуль
                transitive_reload(attrobj, visited)

def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

if __name__ == '__main__':      # Тест: перезагрузить себя
    import reloadall            # перезагрузить этот модуль
    reload_all(reloadall)       # и модуль types
