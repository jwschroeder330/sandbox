import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin # is_authenticate, is_active, is_anonymous, get_id()
from peewee import *

DATABASE = SqliteDatabase('social.db') # all caps signifies that this should be a constant

# order inheriting classes by importance: mixin first
class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now) # no (), () logs date when script runs
    is_admin = BooleanField(default=False)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',) # - before joined_at tells order_by to do this DESC

    # cls instead of self: we do not have to create a user instance to use a user method
    @classmethod # method that belongs to a class, that can create the class it belongs to
    def create_user(cls, username, email, password, admin=False): # cls refers to Class
        try:
            cls.create(
                username=username,
                email=email,
                password=generate_password_hash(password),
                is_admin=admin)
        except IntegrityError: # if username or email are not unique
            raise ValueError("User already exists")

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()



# Future version: increment hashing iterations based on failed logins - prevent brute force
