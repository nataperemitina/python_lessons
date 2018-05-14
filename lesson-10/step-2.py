# Декораторы
from datetime import datetime
from functools import reduce, wraps, lru_cache
import pickle
import time

#todo: Простой декоратор. Как применить и где использовать
#Декоратор - это функция, основное назначение которой служить оберткой для другой функции
#Всегда принимает 1 аргумент - ссылку на оборачиваемую функцию
#Цель - поменять или дополнить имеющуюся функцию

def benchmark(func):
    @wraps(func) #копирует все свойства обертываемой функции
    def wrapper(*args, **kwargs):
        started = time.time()
        result = func(*args, **kwargs) #вызывается только один раз
        worked = time.time() - started
        print('Функция "{}" выполнилась за {:f} микросекунд'.format(
        func.__name__, worked * 1e6
        ))
        return result
    return wrapper

def cache(func):
    memory = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = pickle.dumps((args, sorted(kwargs.items())))
        if key not in memory:
            memory[key] = func(*args, **kwargs)
        
        return memory[key]
    
    return wrapper

#Декораторы вызываются сверху вниз, а применение снизу вверх
@cache
@benchmark
def factorial(n):
    return reduce(lambda f,i: f * i, range(1, n + 1))

print(factorial(5))
print(factorial(5))

#todo: Декоратор с параметрами

"""
def decorator_parameters(param1,....,paramN):
    def decorator(func):
        @warps(func)
        def wrapper(*args, **kwargs):
            do something
            return func(*args, **kwargs)
        return wrapper
    return decorator
"""

def log(filename):
    template = '''
[{now:%Y-%m-%d %H-%M-%S}] Function: "{func}" called with
    -> positional arguments: {args}
    -> keyword arguments: {kwargs}
Returns: {result}
'''
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'a') as f:
                f.write(template.format(now=datetime.now(),
                                        func='.'.join((func.__module__, func.__name__)),
                                        args=args,
                                        kwargs=kwargs,
                                        result=result))
            return result
        return wrapper
    return decorator

@log('log.txt')
def tst_func(a, b):
    return a + b

tst_func(2, 2)
tst_func(3, 5)


