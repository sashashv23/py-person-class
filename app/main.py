class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        person = Person(person["name"], person["age"])
        people_list.append(person)

    return people_list
