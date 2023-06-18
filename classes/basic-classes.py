class BasicUser:
    pass


my_basic_user = BasicUser()
print(my_basic_user)  # <__main__.User object at 0x0000025542EFDEE0>
print(type(my_basic_user))  # <class '__main__.User'>


class User:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name


my_user = User("Iva", "Ivanova")
print(my_user.first_name)  # Iva


class Car:
    def __init__(self, model) -> None:
        self.model = model

    def car_info(self):
        return f"Car model is {self.model}"


my_car = Car("xyz")
print(my_car.car_info())  # Car model is xyz


class Employee:
    @classmethod
    def from_text(cls, text_data):
        name, department, experience = text_data.split(",")
        return cls(name, department, int(experience))

    def __init__(self, name, department, experience) -> None:
        self.name = name
        self.department = department
        self.experience = experience


my_employee = Employee.from_text("Iva,Marketing,2")
print(my_employee.department)  # Marketing
