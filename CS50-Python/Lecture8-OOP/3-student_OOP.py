'''
    Decorators (e.g. `@property`) ---> Functions that modify the behavior of other functions
'''

class Student:
    def __init__(self, name: str, house: str): # <-- instance method
        self.name = name    # <- instance variable
        self.house = house

    def __str__(self) -> str:
        return f"Student -> {self.name} from {self.house}"

    # Getter
    @property
    def house(self):
        return self._house

    @property
    def name(self):
        return self._name

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Value")
        self._name = name

def main():
    student = get_student()
    student._house = "Facultad de Ciencias Matemáticas" # <-- Just Honor system (if a instance variable star with a '_' don't touch it)
    print(student)

def get_student():
    name: str = input("Name: ")
    house: str = input("House: ")
    return Student(name, house)
    
if __name__ == "__main__":
    main()

'''
e.g. of clases built-in Python

INTEGERS
`class int(x, base=10)`

STRINGS
`class str(object='')`
`str.lower()`
`str.strip([chars])`

LIST
`class list([iterable])`
`list.append(x)`

DICTIONARIE
`dict`

'''