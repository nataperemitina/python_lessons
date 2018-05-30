from datetime import datetime

from pony.orm import DataBase, Required, Optional, Set, PrimaryKey

db = DataBase()

class Product(db.Entity):
    """Товар"""
    category = Required('Category')
    title = Required(str)
    description = Optional(str) #будет значение по-умолчанию "пустая строка"
    unit = int
    price = Required(float)
    history = Set('ProductHistory')
    # alt_categories = Set('Category')
    # amount = int #сколько товаров в магазине сейчас

class ProductHistory(db.Entity):
    product = Required('Product')
    created = Optional(datetime, default=datetime.now)
    price = Required(float)


class Category:
    """Категория товара"""
    parent = 'Category'
    title = str
    products = Set(Product)

class Customer:
    """Покупатель"""
    email = str
    phone = str
    name = str
    address = list('Address')

class Address:
    """Адрес"""
    customer = 'Customer'
    country = str
    city = str
    street = str
    zip_code = str
    house = int

class Cart:
    """Корзина с товарами"""
    customer = 'Customer' or None
    products = list('CartItem')

class CartItem:
    """Элемент корзины"""
    cart = 'Cart'
    product = 'Product'
    amount = int #1 единица товара

class Order:
    """Заказ"""
    customer = 'Customer'
    created = datetime
    products = list('OrderItem')
    status = 'Status'

class Status:
    """Статус"""
    name = str

class OrderItem:
    """Товар (одна позиция в заказе)"""
    order = 'Order'
    product = 'Product'
    amount = int #количество товаров

class Menu:
    """Меню"""