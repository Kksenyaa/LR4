class Animal:
    """
    Базовый класс для всех животных.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Инициализирует животное с именем и возрастом.

        :param name: Имя животного
        :param age: Возраст животного
        """
        self._name = name  # Непубличный атрибут, так как имя не должно изменяться напрямую
        self.age = age

    def __str__(self) -> str:
        """
        Возвращает строковое представление животного.
        """
        return f"Животное: {self._name}, Возраст: {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает строку, представляющую объект.
        """
        return f"Animal(name={self._name}, age={self.age})"

    def make_sound(self) -> str:
        """
        Метод, который должен быть переопределён в дочерних классах.
        """
        return "Неизвестный звук"

    def get_name(self) -> str:
        """
        Возвращает имя животного (инкапсулировано для предотвращения изменения напрямую).
        """
        return self._name


class Dog(Animal):
    """
    Дочерний класс, представляющий собаку.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Инициализирует собаку с дополнительным параметром - породой.

        :param name: Имя собаки
        :param age: Возраст собаки
        :param breed: Порода собаки
        """
        super().__init__(name, age)
        self.breed = breed

    def __str__(self) -> str:
        """
        Переопределённый метод для представления собаки.
        """
        return f"Собака: {self._name}, Порода: {self.breed}, Возраст: {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает строку, представляющую объект.
        """
        return f"Dog(name={self._name}, age={self.age}, breed={self.breed})"

    def make_sound(self) -> str:
        """
        Переопределённый метод: собаки лают, поэтому возвращается 'Гав!'.
        """
        return "Гав!"

    def fetch(self, item: str) -> str:
        """
        Метод, добавленный в дочернем классе. Собака приносит предмет.

        :param item: Предмет, который собака должна принести.
        :return: Сообщение о принесённом предмете.
        """
        return f"{self._name} принёс {item}!"


if __name__ == "__main__":
    animal = Animal("Неизвестное животное", 5)
    dog = Dog("Бобик", 3, "Лабрадор")

    print(animal)
    print(dog)

    print(animal.make_sound())
    print(dog.make_sound())

    print(dog.fetch("мяч"))
