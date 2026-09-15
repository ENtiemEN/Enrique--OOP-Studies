class Wizard:
    def __init__(self, name: str):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"
    ...

class Student(Wizard):
    def __init__(self, name: str, house: str):
        super().__init__(name)
        self.house = house
    ...

class Professor(Wizard):
    def __init__(self, name: str, subject: str):
        super().__init__(name)
        self.subject = subject
    ...


student = Student("Harry", "Gryffindor")
professor = Professor("Snape", "Defense Against the Dark Arts")

print(student)
print(professor)