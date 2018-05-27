# todo: Метаклассы


def person_init(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname


"""
type принимает три аргумента:
- имя нового типа
- кортеж базовых типов
- словарь атрибутов
"""

Person = type('Person', (object,), {
    '__init__': person_init,
    '__str__': lambda self: '{} {}'.format(self.firstname, self.lastname)
})

print(type(Person), Person)

def car_init(self, vendor, driver):
    self.vendor = vendor
    self.driver = driver

Car = type('Car', (object,), {
    'COLOR_RED': 1,
    '__init__': car_init,
    'get_vendor': lambda self: self.vendor,
    'get_driver': lambda self: self.driver
})

print(type(Car), Car)

driver = Person('Михаэль', 'Шумахер')
ferrari = Car('Ferrari', driver)
print('Автомобиль "{}", водитель "{}"'.format(
    ferrari.get_vendor(), ferrari.get_driver()
))

# todo: Demo метакласс

class DemoMeta(type):
    def __new__(mcs, name, bases, d): #всегда статический метод, декоратор не нужен
        print('Выделение памяти под класс:\n', name, bases, d)
        return super().__new__(mcs, name, bases, d)

    def __init__(cls, name, bases, d):
        print('Инициализация класса:\n', name, bases, d)
        super().__init__(name, bases, d)

    def __call__(cls, *args, **kwargs):
        print('Создание экземпляра (объекта):\n', args, kwargs)
        return super().__call__(*args, **kwargs)


class Demo(metaclass=DemoMeta):
    def __new__(cls, *args, **kwargs):
        print('Выделение памяти под экземпляр(объект):\n', args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print('Инициализация экземпляра (объекта):\n', args, kwargs)


demo = Demo(1, True, msg='ok')
demo2 = Demo(666, True, msg='ok')


# todo: Пример №2

from abc import ABCMeta, abstractmethod

class MathFunctionMeta(ABCMeta): #метаклассы наследуются друг от друга
    def __init__(cls, name, bases, d):
        super().__init__(name, bases, d)

        if bases:
            cls.check_property('func_name')

    def check_property(cls, prop):
        if getattr(cls, prop, None) is None:
            raise RuntimeError(
                'You need to set the "{}" property'.format(prop)
            )

class MathFunction(metaclass=MathFunctionMeta):
    func_name = None

    def get_func_name(self):
        return self.func_name

    @abstractmethod
    def execute(self):
        pass

class RoundFunction(MathFunction):
    func_name = 'round'
    
    def __init__(self, number, ndigits=None):
        self.number = number
        self.ndigits = ndigits

    def execute(self):
        return round(self.number, self.ndigits)

print(RoundFunction(50).get_func_name())