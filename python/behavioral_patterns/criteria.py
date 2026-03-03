
# https://www.runoob.com/design-pattern/filter-pattern.html
from abc import ABCMeta, abstractmethod


class Person:
    def __init__(self, name: str, gender: str, marital_status: str):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status

    def get_gender(self):
        return self.gender

    def get_marital_status(self):
        return self.marital_status

    def get_name(self):
        return self.name

    def __repr__(self):
        return f"name {self.name}, gender: {self.gender}, marital_status: {self.marital_status}"


class Criteria(metaclass=ABCMeta):
    @abstractmethod
    def meet_criteria(self, persons: list[Person]):
        pass


class CriteriaMale(Criteria):
    def meet_criteria(self, persons: list[Person]):
        male_persons = []
        for person in persons:
            if person.get_gender() == "Male":
                male_persons.append(person)
        return male_persons


class CriteriaFemale(Criteria):
    def meet_criteria(self, persons: list[Person]):
        male_persons = []
        for person in persons:
            if person.get_gender() == "Female":
                male_persons.append(person)
        return male_persons


class CriteriaSingle(Criteria):
    def meet_criteria(self, persons: list[Person]):
        single_persons = []
        for person in persons:
            if person.get_marital_status() == "Single":
                single_persons.append(person)
        return single_persons


class AndCriteria(Criteria):
    def __init__(self, criteria: Criteria, other_criteria: Criteria):
        self.criteria = criteria
        self.other_criteria = other_criteria

    def meet_criteria(self, persons: list[Person]):
        return self.other_criteria.meet_criteria(self.criteria.meet_criteria(persons))


class OrCriteria(Criteria):
    def __init__(self, criteria: Criteria, other_criteria: Criteria):
        self.criteria = criteria
        self.other_criteria = other_criteria

    def meet_criteria(self, persons: list[Person]):
        first_criteria_persons = self.criteria.meet_criteria(persons)
        for person in self.other_criteria.meet_criteria(persons):
            if person not in first_criteria_persons:
                first_criteria_persons.append(person)
        return first_criteria_persons


if __name__ == '__main__':
    persons = []
    persons.append(Person("Robert","Male", "Single"))
    persons.append(Person("John","Male", "Married"))
    persons.append(Person("Laura","Female", "Married"))
    persons.append(Person("Diana","Female", "Single"))
    persons.append(Person("Mike","Male", "Single"))
    persons.append(Person("Mike","Male", "Single"))

    male = CriteriaMale()
    female = CriteriaFemale()
    single = CriteriaSingle()
    single_male = AndCriteria(male, single)
    single_or_female = OrCriteria(female, single)

    print(male.meet_criteria(persons))
    print(female.meet_criteria(persons))
    print(single.meet_criteria(persons))
    print(single_male.meet_criteria(persons))
    print(single_or_female.meet_criteria(persons))
