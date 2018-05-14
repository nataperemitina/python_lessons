from collections import namedtuple, OrderedDict
import sys

from url_shortener import storage

get_connection = lambda: storage.connect('shortener.sqlite')

Action = namedtuple('Action', ('func', 'name'))
actions = OrderedDict()

def menu_action(cmd, name=None):
    #Это все выполнится на этапе синтаксического анализа до выполнения программы
    def decorator(func):
         actions[str(cmd)] = Action(func, name or func.__doc__)
         return func
    return decorator

@menu_action('1', 'Добавить URL-адрес')
def action_add():
    """Добавить URL-адрес"""
    url = input('\nВведите URL-адрес: ')

    with get_connection() as conn:
        short_url = storage.add_url(conn, url)

@menu_action('2', 'Найти оригинальный URL-адрес')
def action_find():
    """Найти оригинальный URL-адрес"""

@menu_action('3', 'Вывести все URL-адреса')
def action_find_all():
    """Вывести все URL-адреса"""
    with get_connection() as conn:
        urls = storage.find_all(conn)
    
    template = '{url[short_url]} - {url[original_url]} - {url[created]}'
    
    for url in urls:
        print(template.format(url=url))

@menu_action('t')
def action_tst():
    """Тестовая команда"""
    print('Тестовая команда')

@menu_action('m', 'Показать меню')
def action_show_menu():
    """Показать меню"""
    menu = []
    for cmd, action in actions.items():
        menu.append('{}.{}'.format(cmd, action.name))

    print('\n'.join(menu))

@menu_action('q', 'Выйти')
def action_exit():
    """Выйти"""
    sys.exit(0)

def main():
    with get_connection() as conn:
        storage.initialize(conn)

    action_show_menu()

    while 1:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd) 
#без исключения вернет None, если ключа нет (если в качестве ключа None, то значение по-умолчанию не вернется)
        if action:
            action.func()
        else:
            print('Неизвестная команда')












             
