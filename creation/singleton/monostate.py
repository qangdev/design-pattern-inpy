
'''
Instances from the Borg class share the same state
'''

class Borg:
    __shared_state = {'key': 'value'}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state


if __name__ == "__main__":
    b0 = Borg()
    b1 = Borg()
    print(b0)
    print(b1)
    print(b0.__dict__)
    print(b1.__dict__)
    b1.x = 13
    print(b0.__dict__)
    print(b1.__dict__)

