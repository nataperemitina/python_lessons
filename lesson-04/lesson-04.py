"""
Как объявить функцию?
Функция - это блок кода, который можно вызывать многократно
Название функции как и название переменной - не начинается с цифры, без кириллицы, слова разделяются _, не начинаются с _ и __
"""

def hello():
    print('Hello!') 

print(type(hello))
hello() #вызов функции
hello()

say_hello = hello #копирование ссылки на функцию
say_hello()

#Зачем функции аргументы?

def hello_username(name):
    print('Hello,', name)

hello_username('Python')
hello_username('JavaScript')
hello_username('Вася')

def summa(a, b):
    print(a+b)

summa(1,3)

#Передача значений аргументов по ссылке

def parse(src, output):
    src = src.strip('.')
    for i in src.split(): #разбиение строки на слова с разделителем "пробел"
        output.append(i)

src = 'Python is programming language.'
output = []

print(src, output)
parse(src, output)
print(src, output)
#все скалярные типы передаются только копированием - по значению
#все изменяемые типы передаются только по ссылке

#Задание аргументов по-умолчанию
def poww(x, p=2): #аргументы по-умолчанию всегда идут последними
    print(x ** p)

poww(5)
poww(2,3)

'''
нормальное количество аргументов >=3 
по-умолчанию передаются только неизменяемые типы, потому что если передать изменяемый тип, то он создастся в памяти только один раз, и все обращения без аргумента будут осуществляться к ранее созданному
'''

def f(i, l=None):
    l = l or []
#    l = l if l is not None else []


#Как вернуть значение из функции?

def minus(a, b):
    return a - b
    a = a * b # никогда не выполнится!!!

r = minus(1,2)
print(r)


#Нужно проверять всегда на ложь, а не на истину!!!
#Нужно избавляться от else

def f2():
    return 1, 2, 3 #просто возвращается кортеж

a, b, c = f2()

#Если нужно вернуть кортеж, то нужно return (1, 2, 3) И присваивать кортежу.


#Переменное количество аргументов в описании функции
def demo_func(i, *args, **kwargs):
    """
    args - кортеж
    kwargs - словарь
    """
    print(args, type(args))
    print(kwargs, type(kwargs))

demo_func(1,2,3,4, j=4)
demo_func(10,'20', k=True, e=456)

def f3(i, j=1, *args):
    print(i,j,args)

f3(2,2,5,5)

#Переменное количество аргументов при вызове функции

def f4(i,j,k,a=None, b=None, c=None):
    print(i, j, k)
    print(a, b, c)

args = [1, 2, 3]
kwargs = {
    'a':10,
    'b':20,
    'c':30,
}

f4(*args, **kwargs)

#Анонимная функция

sqrt = lambda x: x ** 0.5
print(sqrt(9))

#lambda: pass
#lambda x,y: pass
#функция всегда возвращает результат

#Замыкания

"""
Глобальные переменные - те, что объявлены вне функций в теле скрипта
Локальные переменные - те, что объявлены внутри функций
"""
#Функция каррирования
def trim(chars=None):
    #Локальная область видимости функции trim
    #Замкнутая область
    def f(s):
        #Локальная область видимости функции f
        return s.strip(chars)
    return f

spaces_trim = trim()
slashes_trim = ('/\\')
print(spaces_trim('    Hello   '))
#print(slashes_trim('////url//\\\\//'))    

#Рекурсивная функция
def factorial(x):
    # Прямая рекурсия
    return 1 if x == 0 else x * factorial(x - 1)

print(factorial(5))

#Косвенная рекурсия
#def a():
#    b()
#
#def b():
#    a()

"""
Запись глобальной переменной внутри локальной области видимости - global
Запись переменной из замыкания из вложенной функции - nonlocal
"""
