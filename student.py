class Student:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def show_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def year_of_birth(self, current_year):
        return current_year - self.age

    def show_initials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}."