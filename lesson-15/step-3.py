# 2.4. Перегрузка операторов


class Vector(object):
    __slots__=('x','y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        """Перегрузка оператора +"""
        assert isinstance(other, Vector)
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Перегрузка оператора -"""
        assert isinstance(other, self.__class__)
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """Перегрузка оператора *"""
        assert isinstance(other, self.__class__)
        return Vector(self.x * other.x, self.y * other.y)

    def __gt__(self, other):
        """Перегрузка оператора >"""
        assert isinstance(other, self.__class__)
        return self.length > other.length

    def __eq__(self, other):
        """Перегрузка оператора =="""
        assert isinstance(other, self.__class__)
        return self.length == other.length

    def __eq__(self, other):
        """Перегрузка оператора >="""
        assert isinstance(other, self.__class__)
        return self.length >= other.length

    @property
    def length(self): #преобразование метода в свойство
        return (self.x ** 2 + self.y ** 2) ** 0.5

v1 = Vector(-3, 4)
print(v1)

v2 = Vector(-3, 6)
v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * v2

print('Сумма векторов:', v3)
print('Разность векторов:', v4)
print('Произведение векторов:', v5)
