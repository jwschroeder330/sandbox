import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('tacov2.db')


class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)

    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls, email, password):
        try:
            with DATABASE.transaction():
                cls.create(
                    email=email,
                    password=generate_password_hash(password))
        except IntegrityError:
            raise ValueError("User already exists")


class Taco(Model):
    user = ForeignKeyField(
        rel_model=User,
        related_name='tacos'
    )
    protein = CharField()
    shell = CharField()
    cheese = BooleanField()
    extras = CharField()
    
    class Meta:
        database = DATABASE
        primary_key = CompositeKey('user', 'protein', 'shell', 'cheese', "extras")

    @classmethod
    def create_taco(cls, user, protein, shell, cheese, extras):
        try:
            with DATABASE.transaction():
                cls.create(
                    user=user,
                    protein=protein,
                    shell=shell,
                    cheese=cheese,
                    extras=extras)
        except IntegrityError:
            raise ValueError("Taco already exists")

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Taco], safe=True)
    DATABASE.close()

