''' Operator Overloading
-> "+ - ? ..." you can Implement your own interpretation.
e.g. '+' is not only sum. Can be for concatenation
'''

# Vault example (all sort of money in Harry Potter)
class Vault:
    def __init__(self, galleons: float = 0, sickles: float = 0, knuts: float = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"galleons: {self.galleons}, sickles: {self.sickles}, knuts: {self.knuts}"

    def __add__(self, other) -> "Vault":
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts

        return Vault(galleons, sickles, knuts)

potter = Vault(100, 50, 25)
#print(potter)

weasley = Vault(25, 50, 100)
#print(weasley)

# galleons = potter.galleons + weasley.galleons
# sickles = potter.sickles + weasley.sickles
# knuts = potter.knuts + weasley.knuts
# total = galleons + sickles + knuts
# print(total)

total = potter + weasley
print(type(total))
print(total)

''' There are a lot more of special methods
Visit --> https://docs.python.org/3/reference/datamodel.html#special-method-names
'''