"""zaimplementowanie klas abstrakcyjnych"""
import abc


class Animal(abc.ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abc.abstractmethod
    def say_something(self):
        pass


class Giraffe(Animal):
    def say_something(self):
        print('mniam, mniam')


class Dog(Animal):
    def say_something(self):
        print('bark, bark')


class Duck(Animal):
    def say_something(self):
        print('quack, quack')


if __name__ == '__main__':
    dog = Dog('Thor')
    dog.say_something()
    duck = Duck('donald')
    duck.say_something()
    giraffe = Giraffe('Tosia')
    giraffe.say_something()
