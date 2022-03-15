'''
Simple Version by overriding __new__ method
'''
class DatabaseConnection:

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(DatabaseConnection, cls).__new__(cls)
        return cls.instance


if __name__ == "__main__":
    conn1 = DatabaseConnection()
    conn2 = DatabaseConnection()
    print(conn1)
    print(conn2)
    print("Connection1 is Connection2:", conn1 is conn2)