import os.path as Path
import sqlite3

SQL_INSERT_URL = 'INSERT INTO shortener (original_url) VALUES (?)' 
SQL_UPDATE_SHORT_URL = '''
    UPDATE shortener SET short_url=? WHERE id=?
'''

SQL_SELECT_ALL = '''
    SELECT 
        id, original_url, short_url, created
    FROM
        shortener
'''

SQL_SELECT_URL_BY_ORIGIN = SQL_SELECT_ALL + ' WHERE original_url=?'
SQL_SELECT_URL_BY_PK = SQL_SELECT_ALL + ' WHERE id=?'


# def connect(db_name=':mamory"'):
def connect(db_name=None):
    """Выполненяет подключение к БД"""
    if db_name is None:
         db_name = ':memory:' #БД, создаваемая в памяти

    conn = sqlite3.connect(db_name)
    #Магия!!!

    return conn

def initialize(conn):
    """Инициализирует структуру БД."""
    script_path = Path.join(Path.dirname(__file__), 'schema.sql') 
# __file__ абсолютный путь до текущего файла
# dirname - возвращает родительский каталог
# join - склеивает пути, используя разделитель текущей ОС

    with conn, open(script_path) as f:
        conn.executescript(f.read())


def add_url(conn, url, domain=''):
    """Добавляет URL-адрес в БД и возвращает короткий"""
    url = url.rstrip('/')

    if not url:
        raise RuntimeError("URL can't be empty.")

    with conn:
        found = find_url_by_origin(conn, url)

        if found:
            return found[2]

        cursor = conn.execute(SQL_INSERT_URL, (url,)) 
        pk = cursor.lastrowid #primary key последней вставленной записи
        #Магия по сокращению

        short_url = '{}/{}'.format(domain.rstrip('/'), pk)
        
        conn.execute(SQL_UPDATE_SHORT_URL, (short_url, pk))
        
        return short_url

def find_url_by_origin(conn, origin_url):
    """Возвращает URL-адрес по оригинальному URL"""
    origin_url = origin_url.rstrip('/')

    with conn:
        cursor = conn.execute(SQL_SELECT_URL_BY_ORIGIN, (origin_url,))
        return cursor.fetchone()




