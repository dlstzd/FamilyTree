from datetime import date


class Person:

    def __init__(self, name):#, birthdate, email, phone):
        self.name = name
        self.children = set([])
        self.parent1 = '?'
        self.parent2 = '?'
        self.spouse = '?'
        self.birthyear = None
        #self.birthdate = birthdate
        #self.email = email
        #self.phone = phone
        self.age = 0

    def get_age(self, yeart):
        print('here')
        #if hasattr(self, "age"):
        #    return self.age
        #if self.birthyear is 0:
        #    print("Birth year must be specified to calculate age")
        #    return None
        if self.birthyear is None:
            self.birthyear = yeart
        now = date.today()
        age = now.year - yeart
        print(age)
        self.age = age
        return age

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
