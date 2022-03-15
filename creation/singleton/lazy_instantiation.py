
class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print(" __init__ method called..")
        else:
            print("Instance already created:", self.getInstance())
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

    def say_hello(self):
        print("Jello!")


if __name__ == "__main__":
    s1 = Singleton()
    print(s1)
    s1.getInstance()
    print(s1)
    s2 = Singleton()
    print(s2)
