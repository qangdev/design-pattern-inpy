'''
MetaClass version
'''
class MetaSingleton(type):
    _instance = None
    def __call__(self, *args, **kwds):
        print("Hello!")
        if self._instance is None:
            self._instance = super(MetaSingleton, self).__call__(*args, **kwds)
        return self._instance

class Singleton(metaclass=MetaSingleton):
    def __init__(self, name) -> None:
        print("Hi!")
        self.name = name

    def __repr__(self) -> str:
        return f"{id(self)} - {self.name}"


if __name__ == "__main__": 
    '''
    Singleton = MetaSingleton()
    '''
    f0 = Singleton("Banana")
    print(">", f0._instance)
    f1 = Singleton("Benene")  # This won't change the name of the instance thus it's still Banana
    print(f0)
    print(f1)
    assert f0 is f1
    print("f0 is f1:", f0 is f1)