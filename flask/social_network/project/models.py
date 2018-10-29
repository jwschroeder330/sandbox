import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin # is_authenticate, is_active, is_anonymous, get_id()
from peewee import *

DATABASE = SqliteDatabase('social.db') # all caps signifies that this should be a constant

# order inheriting classes by importance: mixin first
class User(
UserMixin,
Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now) # no (), () logs date when script runs
    is_admin = BooleanField(default=False)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',) # - before joined_at tells order_by to do this DESC

    def get_posts(self):
        return Post.select().where(Post.user == self)


    def get_stream(self):
        return Post.select().where(
        # either users i am following or posts that are mine
        (Post.user << self.following()) |
        (Post.user == self)
        )

    def following(self):
        """
            The users that we are following.
        """
        return (
            User.select().join(
                # table we are selecting
                Relationship,
                # how we aer joining data
                on=Relationship.to_user
            ).where(
                # where the from_user == me
                Relationship.from_user == self
            )
        )

    def followers(self):
        """
            Get users following the current user.
        """
        return (
            User.select().join(
                Relationship,
                on=Relationship.from_user
            ).where(
                # the opposite of following
                Relationship.to_user == self
            ))

    # cls instead of self: we do not have to create a user instance to use a user method
    @classmethod # method that belongs to a class, that can create the class it belongs to
    def create_user(cls, username, email, password, admin=False): # cls refers to Class
        try:
            # transaction, try (if works, continue, if not remove whatever you did)
            with DATABASE.transaction():
                cls.create(
                    username=username,
                    email=email,
                    password=generate_password_hash(password),
                    is_admin=admin)
        except IntegrityError: # if username or email are not unique
            raise ValueError("User already exists")


class Relationship(Model):
    # People who are related to me
    from_user = ForeignKeyField(User, related_name='relationships')
    # People I am related to
    to_user = ForeignKeyField(User, related_name='related_to')

    class Meta:
        database = DATABASE
        # how to find data, and if the index is unique?
        indexes = (
            # two fields in index
            (('from_user', 'to_user'),
            # whether index is unique or not
            True),)
            # NOTE: notice the trailing commas after the first tuple - nested tuples


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Post, Relationship], safe=True)
    DATABASE.close()


class Post(Model):
    timestamp = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(
    # model that this field points to
    model=User,
    # if you are a user, what do you call the post model?
    related_name='posts'
    )
    content = TextField()

    class Meta:
        database = DATABASE
        order_by = ('-timestamp',)  # note, these have to be tuples!

# Future version: increment hashing iterations based on failed logins - prevent brute force
