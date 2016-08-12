from PersonID import *

#future issue each person needs a unique id
#or we list duplicate and allow the person to select the correct person --

persona = Person("Joe", "Lund")
personb = Person("Liz", "Pier")
personc = Person("Lydia", "Hill")
persond = Person("Scott", "Hill")
peopleList = []

def print_people(peopleList):
    for p in peopleList:
        print(p.fname, p.lname, p.children)

def find_by_name(peopleList, first, last):
    for p in peopleList:
        if p.fname == first and p.lname == last:
            print("Person found")


def add_person(peopleList, person):
    peopleList.append(person)


def remove_person(peopleList, first, last):
    '''if person in peopleList:
        print("Person Found, Deleting...")
        peopleList.remove(person)
    '''
    for p in peopleList:
        if p.fname == first and p.lname == last:
            peopleList.remove(p)

def modify_person(peopleList, person):
    if person in peopleList:
        person.fname = "BBBB"

def add_child(peopleList, person):
    if person in peopleList:
        person.children.append(persond.fname + ' ' + persond.lname)


add_person(peopleList, persona)
add_person(peopleList, personb)
add_person(peopleList, personc)
add_person(peopleList, persond)

add_child(peopleList, personc)

find_by_name(peopleList, "Joe", "Lund")

for p in peopleList:
    print(p.fname, p.lname, p.children)

print("----------")
