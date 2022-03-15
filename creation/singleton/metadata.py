'''
MetaClass version
'''
class MetaSingleton(type):
    _instances = None
    def __call__(self, *args, **kwds):
        if self._instances is None:
            self._instances = super(MetaSingleton, self).__call__(*args, **kwds)
        return self._instances

class SingleTon(metaclass=MetaSingleton):
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"{id(self)} - {self.name}"


if __name__ == "__main__": 
    f0 = SingleTon("Banana")
    f1 = SingleTon("Benene")  # This won't change the name of the instance thus it's still Banana
    print(f0)
    print(f1)
    assert f0 is f1
    print("f0 is f1:", f0 is f1)