'''
MetaClass version
'''
class OnlyOne(type):
    _instances = {}

    def __call__(self, *args, **kwds):
        if self not in self._instances:
            self._instances[self] = super(OnlyOne, self).__call__(*args, **kwds)
        return self._instances[self]

class Food(metaclass=OnlyOne):
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"{id(self)} - {self.name}"


if __name__ == "__main__": 
    f0 = Food("Banana")
    f1 = Food("Banana")
    print(f0)
    print(f1)
    assert f0 is f1
    print("f0 is f1:", f0 is f1)