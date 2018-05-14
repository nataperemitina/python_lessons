# Декораторы

import time
from urllib.request import urlopen

def page(url):
    def get():
        return urlopen(url).read()
    return get

python = page('http://python.org')
#print(python())

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    
    return f

def benchmark(func, *args, **kwargs):
    started = time.time()
    result = func(*args, **kwargs)
    worked = time.time() - started
    print('Функция "{}" выполнилась за {:f} микросекунд'.format(
        func.__name__, worked * 1e6
    ))
    return result

print(benchmark(factorial, 5))
print(benchmark(python))
