class Person:
    department='School of Information'

    def set_name(self,name):
        self.n=name
    def set_location(self,location):
        self.l=location

person=Person()
person.set_name('ishita')
person.set_location('Mp')
print('{} lives in {} and works in the department of {}'.format(person.n, person.l, Person.department))
