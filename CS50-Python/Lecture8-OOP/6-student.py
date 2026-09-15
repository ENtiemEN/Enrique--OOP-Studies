class Student:
    def __init__(self, name: str, house: str):
        self.name = name
        self.house = house

    def __str__(self) -> str:
        return f"{self.name} form {self.house}"

    @classmethod
    def get(cls) -> "Student":
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
        

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()

