'''
2.1. Специальные свойства и методы классов

__name__    - имя класса
__class__   - объект-метакласс
__module__  - имя модуля, в котором объявлен данный класс
__bases__   - кортеж базовых классов
__dict__    - словарь атрибутов класса (все статические свойства и все методы)
__doc__     - строка документации


2.2. Специальные свойства и методы объектов
__class__   - класс, на основе которого создан объект
__dict__    - словарь атрибутов объекта
                (если есть __slots__, то не создается)

__dir__()   - список атрибутов класса (используется функцией dir(obj))
__repr__()  - формальное строковое представление объекта, используется функцией repr(obj).
                Должен быть валидным Python-кодом

2.3. Явное приведение объекта к определенному типу.
Все нижеперчисленное - методы
__bool__    - преобразование в логический тип
__int__     - преобразование в целочисленный тип
__index__   - преобразование без потерь числового объекта в целочисленный тип
                используется в срезах ([start:end:step])
                => объект используется как индекс списка
                => bin() oct() hex()
                => Python2: __oct__, __hex__
__float__   - преобразование в дробный тип
__complex__ - преобразование в комплексное число
__str__     - преобразование в строку
__bytes__   - преобразование в байтовую строку
             не поддерживается в Python2
'''