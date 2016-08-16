import datetime


class Person:

    def __init__(self, name):#, birthdate, email, phone):
        self.name = name
        self.children = set([])
        self.parent1 = '?'
        self.parent2 = '?'
        self.spouse = '?'
        #self.birthdate = birthdate
        #self.email = email
        #self.phone = phone
        #self.age()

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_parent1(self, parent1):
        self.parent1 = parent1

    def get_parent1(self):
        return self.parent1

    def set_parent2(self, parent2):
        self.parent2 = parent2

    def get_parent2(self):
        return self.parent2

    def set_spouse(self, spouse):
        self.spouse = spouse

    def get_spouse(self):
        return self.spouse


    #other attributes

    #check age function for proper return
    '''
    def age(self):
        if hasattr(self, "_age"):
            return self._age
        now = datetime.date.today()
        age = now.year - self.birthdate.year
        if now < datetime.date(now.year, now.month, now.day):
            age -= 1
        self._age = age
        #return age
    def marry(self, first, last):
        self._spouse = first + " " + last


Scot = Person("Scott Hel")
print(Scot.name, Scot.parent1)
Scot.set_name("Peter")
print(Scot.name, Scot.parent1)


    '''