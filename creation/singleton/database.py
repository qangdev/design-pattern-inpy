import sqlite3

class MetaSingleton(type):
    __instances = {}

    def __call__(self, *args, **kwds):
        if self not in self.__instances:
            self.__instances[self] = super(MetaSingleton, self).__call__(*args, **kwds)
        return self.__instances[self]


class Database(metaclass=MetaSingleton):

    def __init__(self):
        self.connection = None
        self.cursorobj = None

    def connect(self):
        if self.connection is None:
            print("Init connection...")
            self.connection = sqlite3.connect('db.sqlite3')
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


if __name__ == '__main__':
    db0 = Database().connect()
    db1 = Database().connect()
