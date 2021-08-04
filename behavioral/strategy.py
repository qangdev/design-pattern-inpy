"""
DOCSTRING:
According to "https://refactoring.guru/design-patterns/strategy"

- Strategy: A behavioral design pattern that lets you define a family of algorithm,
put each of them into a separate class, and make their objects interchangeable

- Gut feeling: Make simple change easy. Lego

- Given example: A navigation app. It can help travelers go from A to B by car/walking/public transport/etc
It started with by Car and time by time users require more option so walking added, then public transport added to the system
The system ends up with a massive class that any change to one of the class will cause high potential bugs.
Team became inefficient because of code conflict and

- Learning example: Says there is a master list context (manager). Its job is to to a un-order list and based on the choice of client
it will hand the data in the worker to do the allocated job
The Context has two worker under it. Sorter and Reverser so bases on the client command
If the job is to sort the data then the Sorter will be invoked
in the other hands if the job is to revere the data then Reverser will be in charge
"""


from abc import ABC, abstractmethod


class Slave(ABC):
    @abstractmethod
    def process(self, data: list):
        raise NotImplementedError


class Context:
    def __init__(self, slave: Slave = None):
        self._slave = slave

    @property
    def slave(self):
        return self._slave

    @slave.setter
    def slave(self, slave: Slave):
        self._slave = slave

    def do_work(self, data: list) -> list:
        return self._slave.process(data)


class SlaveSort(Slave):
    def process(self, data: list):
        return sorted(data)


class SlaveRevered(Slave):
    def process(self, data: list):
        return list(reversed(data))


def test_sort():
    data = ["a", "c", "f", "b", "z"]

    context = Context()

    context.slave = SlaveSort()
    sorted_data = context.do_work(data.copy())
    assert ["a", "b", "c", "f", "z"] == sorted_data


def test_revered():
    data = ["a", "c", "f", "b", "z"]

    context = Context()
    context.slave = SlaveRevered()
    reversed_data = context.do_work(data.copy())
    assert ["z", "b", "f", "c", "a"] == reversed_data


def test_sort_and_revered():
    data = ["a", "c", "f", "b", "z"]

    context = Context()

    context.slave = SlaveSort()
    sorted_data = context.do_work(data.copy())
    assert ["a", "b", "c", "f", "z"] == sorted_data

    context.slave = SlaveRevered()
    reversed_data = context.do_work(data.copy())
    assert ["z", "b", "f", "c", "a"] == reversed_data
