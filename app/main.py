class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        person = Person(person["name"], person["age"])
        Person.people[person.name] = person
        Person.people[person.name].wife = Person.people[person.name].wife
        Person.people[person.name].husband = Person.people[person.name].husband
        people_list.append(person)
    return people_list
