import datetime

class Person:
    def __init__(self, fname, lname, sex, birthdate, email, phone):
        self.fname = fname
        self.lname = lname
        self.sex = sex
        self.birthdate = birthdate
        self.email = email
        self.phone = phone
        self.age()
        self.marry("spousey","spouse")

        #other attributes
        #parents list
        #children list

    #check age function for proper return
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
