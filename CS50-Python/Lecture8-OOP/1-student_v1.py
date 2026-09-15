'''
    Review of Unpacking a sequence 
    LIST or TUPLE
'''

def main():
    #name = get_name()
    #house = get_house()
    #name, house = get_student() # <-- Unpacking (unpack a sequence)
    student = get_student()
    print(f"{student[0]} from {student[1]}")

# def get_name():    
#     return input("Name: ")

# def get_house():
#     return input("House: ")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    #return (name, house)
    #return name, house  # <- we're returning one value (it's a tuple)
    return [name, house] # <- we're making this mutable

if __name__ == "__main__":
    main()
