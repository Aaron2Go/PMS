from sqlobject import *
from sqlobject.sqlite import builder


class User(SQLObject):
    name=StringCol(unique=True)
    code=StringCol()
    level=IntCol(default=0)

    def __str__(self):
        return self.name


def set_user_table(db_name):
    User._connection=builder()(db_name)
    User.createTable(ifNotExists=True)

set_user_table('data\\user')