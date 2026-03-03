
# https://www.runoob.com/design-pattern/composite-pattern.html


class Employee:
    def __init__(self, name: str, dept: str, salary: int):
        self.name = name
        self.dept = dept
        self.salary = salary
        self.subordinates = []

    def add(self, e):
        self.subordinates.append(e)

    def remove(self, e):
        self.subordinates.remove(e)

    def get_subordinates(self):
        return self.subordinates

    def __repr__(self):
        return f"employee name: {self.name}, dept: {self.dept}, salary: {self.salary}"


if __name__ == '__main__':
    ceo = Employee("John","CEO", 30000)
    head_sales = Employee("Robert","Head Sales", 20000)
    head_marketing = Employee("Michel","Head Marketing", 20000)
    clerk1 = Employee("Laura","Marketing", 10000)
    clerk2 = Employee("Bob","Marketing", 10000)
    salesExecutive1 = Employee("Richard", "Sales", 10000)
    salesExecutive2 = Employee("Rob","Sales", 10000)

    ceo.add(head_sales)
    ceo.add(head_marketing)

    head_sales.add(salesExecutive1)
    head_sales.add(salesExecutive2)

    head_marketing.add(clerk1)
    head_marketing.add(clerk2)

    print(ceo)
    for e in ceo.get_subordinates():
        print(e)
        for e1 in e.get_subordinates():
            print(e1)
