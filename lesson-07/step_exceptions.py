# Exception - исключение

try:
    i = int(input())
    print(i[0])
except ValueError:
    print('Некорректное число!')
except: # может отсутствовать
    print('Любое исключение было отловлено')
finally: # может отсутствовать
    print('Выполняется всегда!')


raise KeyError('Мое сообщение об ошибке') # генерация исключения
