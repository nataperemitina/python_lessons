#Классы и объекты

# todo: Как объявить/создать класс?
#Свойства/атрибуты/данные-члены/данные
#В свойствах хранятся данные объекта
#Методы - поведение объекта

# todo: Зачем нужен конструктор?
# Основная задача - инициализация экземпляра


class Person(object):
    __slots__ = ('__firstname', '__lastname') # Ограничение на набор свойств, иначе свойства добавляются на лету!!!
    def __init__(self, firstname, lastname): #__xx__ - неявно вызываемые магические методы
        #self - ссылка на текущий экземпляр/объект
        self.__lastname = lastname
        self.__firstname = firstname

    def get_full_name(self):
        return '{} {}'.format(self.get_firstname(), self.get_lastname())

    def get_firstname(self):
        """Метод-получатель, getter"""
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

 #   def set_firstname(self, firstname):
 #       """Метод установщик, setter"""
 #       self.firstname = firstname

# todo: Как создать объект/экземпляр?


linus = Person('Linus', 'Torvalds')
#linus.firstname = 'Linus' # запись данных в свойство
#linus.lastname = 'Torvalds'

#print(linus.firstname, linus.lastname) # чтение свойства
print(linus.get_full_name())

stallman = Person('Richard', 'Stallman')
#print(stallman.firstname, stallman.lastname)
print(stallman.get_full_name())

pseudo_clone = linus # ссылка на тот же участок памяти
print(linus)
print(pseudo_clone)
print(stallman)


#print(Person, linus)
#print(type(Person), type(linus))

# todo: Что такое наследование?
# При наследовании __slots__ теряются

class Developer(Person):
    """
    Person  -базовый класс или родительский класс
    Developer - дочерний класс или потомок
    """
    __slots__ = ('__skills',)
    def __init__(self, firstname, lastname, skills):
        super().__init__(firstname, lastname) #super позволяет обращаться к базовому классу
        self.__skills = skills

    def add_skill(self, skill):
        if skill not in self.get_skills():
            self.get_skills().append(skill)

    def get_skills(self):
        return self.__skills

    def remove_skill(self, skill):
        if skill in self.get_skills():
            self.get_skills().remove(skill)

dev_2 = Developer('Developer', '2', ['Brainfuck'])
print(dev_2.get_skills())
print(dev_2.get_full_name())


# todo: Статические свойства и методы
# свойства и методы класса общие для всех объектов


class Singleton(object):
    __instance = None # статическое свойство

    def __init__(self):
        self.__params = {}

    @classmethod
    def get_instance(cls): # статический метод не требует созданного объекта
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def add_param(self, key, value):
        self.__params[key] = value

    def get_param(self, key):
        return self.__params.get(key)

    def remove_param(self, key):
        if key in self.__params:
            del self.__params[key]


config = Singleton.get_instance()
config.add_param('db_host', 'localhost')
config.add_param('db_port', 1234)

config_2 = Singleton.get_instance()
print(config_2.get_param('db_host'))
print(config_2.get_param('db_port'))