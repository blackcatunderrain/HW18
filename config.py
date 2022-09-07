# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.
from sqlalchemy import false


class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_TRACK_MODIFICATIONS = false
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'

