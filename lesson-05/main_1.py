# Модули и пакеты

#Название как всегда - не с цифры, без специальных символов и т.д.

#1. Импорт модуля "целиком"
import os.path
import square_shapes

print(square_shapes.calculate_square_area(5))
print(square_shapes.calculate_rectangle_area(4, 3))

os.path.basename('/home/itmo/1.txt')

#2. Частичный импорт

from square_shapes import ( #скобки необязательны
    calculate_triangle_area, calculate_circle_area
)

from os import path as Path

print(calculate_triangle_area(7, 8, 9))
Path.basename('gs')

#3. Импорт * (все имена из модуля)
from square_shapes import * # так лучше не делать

# main - это главный (исполняемый, запускаемый) модуль
# модули ищутся python-ом только в директории(и поддиректориях), где находится главный модуль
# если там нету, то ищется в $PYTHONPATH
# потом в заранее известных платформозависимых путях
# потом в файлах .pth в стандартных путях

# Модули компилируются в файлы .pyc после первого запуска программы, и затем уже могут не компилироваться 
# Если изменений в модуле не видно - значит нужно почистить .pyc
# скомпилированные файлы лежат в __pycache__

# python3 -O main.py => .opt-1.pyc
# оптимизированная компиляция (удаляется дебаг-информация)
# python3 -OO main.py => .opt-2.pyc (удаляются даже комментарии)


__name__ #имя модуля (если непосредственно он отдается интерпретатору, то он называется __main__)

if __name__ == '__main__':
    print('Будет работать, только если модуль используется как исполняемый') 


