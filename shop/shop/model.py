from datetime import datetime

from pony.orm import (
    Required, Optional, Set, PrimaryKey
)

from . import pony

db = pony.db


class Category(db.Entity):
    """Категория товара"""
    parent = Optional('Category', reverse='children')
    children = Set('Category', reverse='parent')
    title = Required(str)
    products = Set('Product')


class Product(db.Entity):
    """Товар"""
    category = Required('Category')
    title = Required(str)
    description = Optional(str)
    unit = Required(str)
    price = Required(float)
    # alt_categories = Set('Category')
    # amount = int # сколько товаров в магазине сейчас
    history = Set('ProductHistory')
    cart_items = Set('CartItem')
    order_items = Set('OrderItem')


class ProductHistory(db.Entity):
    product = Required('Product')
    created = Optional(datetime, default=datetime.now)
    price = Required(float)


class Customer(db.Entity):
    """Покупатель"""
    email = Required(str, unique=True)
    phone = Optional(str)
    name = Optional(str)
    addresses = Set('Address')
    cart = Optional('Cart')
    orders = Set('Order')


class Address(db.Entity):
    """Адрес"""
    country = Required(str)
    city = Required(str)
    street = Required(str)
    zip_code = Required(str)
    house = Required(str)
    customers = Set('Customer')


class Cart(db.Entity):
    """Корзина с товарами"""
    customer = Optional('Customer')
    products = Set('CartItem')


class CartItem(db.Entity):
    """Элемент корзины"""
    cart = Required('Cart')
    product = Required('Product')
    amount = Optional(int, default=1) # 1 единица товара


class Status(db.Entity):
    """Статус"""
    name = PrimaryKey(str)
    title = Required(str)
    orders = Set('Order')


class Order(db.Entity):
    """Заказ"""
    customer = Required('Customer')
    created = Optional(datetime, default=datetime.now)
    products = Set('OrderItem')
    status = Required('Status')


class OrderItem(db.Entity):
    """Товар (одна позиция) в заказе"""
    order = Required('Order')
    product = Required('Product')
    amount = Optional(int, default=1) # 1 единица товара
