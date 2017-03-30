class Employee:
    def __init__(self, name, base_salary, phone_number):
        self.name = name
        self.base_salary = base_salary
        self.phone_number = phone_number

    @property
    def name(self):
        return self.__name

    @property
    def base_salary(self):
        return self.__base_salary

    @property
    def phone_number(self):
        return self.__phone_number

    @name.setter
    def name(self, name):
        self.__name = name

    @base_salary.setter
    def base_salary(self, base_salary):
        self.__base_salary = float(base_salary)

    def mutator(self, base_salary):
        self.base_salary = base_salary

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number

    def salary_total(self):
        return self.base_salary

    def __str__(self):
        return type(self).__name__ + str((self.name, self.phone_number, self.salary_total()))

    def __repr__(self):
        return str(type(self)) + str(self.__dict__)


class Engineer(Employee):
    def __init__(self, name, base_salary, phone_number):
        super(Engineer, self).__init__(name, base_salary, phone_number)


class Manager(Employee):
    def __init__(self, name, base_salary, phone_number, bonus):
        super(Manager, self).__init__(name, base_salary, phone_number)
        self.bonus = bonus

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus):
        self.__bonus = bonus

    def salary_total(self):
        return self.base_salary + self.bonus


class CEO(Manager):
    def __init__(self, name, base_salary, phone_number, bonus, stock_options):
        super(CEO, self).__init__(name, base_salary, phone_number, bonus)
        self.stock_options = stock_options

    @property
    def stock_options(self):
        return self.__stock_options

    @stock_options.setter
    def stock_options(self, stock_options):
        self.__stock_options = stock_options

    def salary_total(self):
        return self.base_salary + self.bonus + self.stock_options


def print_staff(staff):
    for employees in staff:
        print(employees)


def main():
    palm_beach_county = [Employee("Tyler Moak", 12000, "355-1234"), Employee("Micheal", 45000, "355-1235"),
                         Employee("Angel", 45500, "355-1236"), Engineer("DJ", 70000, "355-1237"),
                         Engineer("Paul", 100000, "355-1238"), Manager("Amit", 120000, "355-1239", 10000),
                         CEO("Steve", 242024.64, "1240", 50000, 40000)]
    print_staff(palm_beach_county)


if __name__ == "__main__":
    main()
