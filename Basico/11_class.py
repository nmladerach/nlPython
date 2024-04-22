### class ###
### CamelCase ###

class MyEmpyPerson:
    pass

### __init__ -> Constructor de clase -> Esta persona puede recibir parametros
class Person:
    def __init__(self, param_name, param_surname):
        self.name = param_name
        self.surname = param_surname
        self.fullname = f"{param_name} {param_surname}"

    def walk (self):
        print(f"{self.fullname} Esta caminando")

my_person = Person("Juan","Perez")
print(my_person.name, my_person.surname)
print(f"{my_person.name} {my_person.surname}")
print(my_person.fullname)
my_person.walk()