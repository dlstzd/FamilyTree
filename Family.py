from PersonID import *
import datetime
persona = Person("Joe", "Lund", "M", datetime.date(1989, 6, 12), "da@mail.com", "9389949195")
personb = Person("Liz", "Pier", "F", datetime.date(1992, 9, 2), "dm@mail.com", "614-567-4432")
personc = Person("Lydia", "Hill", "F", datetime.date(1995, 10, 14), "lh@mail.com", "832-986-4432")


peopleList = []
peopleList.append(personb)
peopleList.append(persona)
peopleList.append(personc)
#tester commet
for p in peopleList:
    print(p.fname, p.lname)
    print(p._age)
    print(p._spouse)
