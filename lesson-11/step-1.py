#Итераторы
#Генераторы
#Генераторы списковб словарей, множеств
#Генераторные выражения

s = 'Linus Torvalds'
lst = [1, 2, 3, 4, 5]
d = {
    'name': 'Linus Torvalds',
    'age' : 47,
    'is_developer': True,
}

"""
__iter__() => return Iterator
__next__() => Iterator
"""

it = iter(s) #calls __iter__()
print(type(it))


it = iter(lst) #calls __iter__()
print(type(it))


it = iter((1, 2)) #calls __iter__()
print(type(it))


it = iter(d) # calls __iter__()
print(type(it))

print(next(it)) # calls __next__()
print(next(it))
print(next(it))
#print(next(it)) # StopIteration exception


def for_emitator(seq):
    it = iter(seq)

    while 1:
        try:
            i = next(it)
            print(i)
        except StopIteration:
            break


for_emitator(s)
for_emitator(lst)
for_emitator(d)

with open(__file__) as f:
    print(type(iter(f)))
    for i in f:
        pass

# todo: Генераторы
# Функция, которая воспроизводит последовательность значений и может использоваться при выполнении итераций


def generator():
    print('Шаг №1')
    yield 1 # Возвращает результат и выполнение функции приостанавливается в этой точке пока снова не будет вызван next
    print('Шаг №2')
    yield 2
    print('Шаг №3')

# Для генераторов нельзя использовать возвращение None (поэтому без return) - нецелесообразно

gen = generator()
print(type(gen))

print(next(gen))
print(next(gen))
#print(next(gen))# StopIteration exception


def countdown(n):
    print('Генератор стартовал!')
    while n:
        yield n # на каждой итерации будет тратиться фиксированный объем памяти
        n -= 1


for i in countdown(3):
    print('Значение счетчика: {}'.format(i))


# todo: Генераторы списков/словарей/множеств

"""
[expression for item1 in iterable1 if condition1
            for item2 in iterable2 if condition2
            ......
            for itemN in iterableN if conditionN ]
"""

numbers = [1, 1, 2, 2, 3, 3]
#squares = []
#for i in numbers:
#    squares.append(i * I)

squares = [i * i for i in numbers]
odd = [i for i in numbers if i % 2]

"""
points = []
for x in range(3):
    for y in range(3):
        point.append((x, y))
"""

points = [(x, y) for x in range(3) for y in range(3)]

sett = {i for i in numbers}

print(squares)
print(odd)
print(points)
print(sett)

sett = set(numbers)
print(sett)


# todo: Генераторы словарей

keys = ['id', 'original_url', 'short_url']
values = [1, 'http://profi.itmo.ru', '/1']

data = {k: v for i, k in enumerate(keys)
             for j, v in enumerate(values) if i == j}
print(data)


for k, v in zip(keys, values): # так можно сделать только с двумя списками
    print(k, v)

print(dict(zip(keys, values)))

print(data.items())

print(dict([('k1', 1), ('k2', 2), ('k3', 3)]))


# todo: Генераторные выражения


squares = (i * i for i in numbers)
print(squares, type(squares), list(squares))


with open(__file__) as f:
    lines = (line.strip() for line in f)
    todos = (s.replace('# todo:', '') for s in lines if s.startswith('# todo:'))
    '''
    Только внутри контекстного менеджера, т.к. реально код будет выполняться при вызове генератора.
    Файл должен быть открыт на этот момент
    '''
    print('Todos:', todos, list(todos))


print(', '.join(str(i) for i in numbers))