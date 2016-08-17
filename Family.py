from PersonID import *
import pickle
import tkinter as tk
#future issue each person needs a unique id
#or we list duplicate and allow the person to select the correct person --


peopleList = []

def update_file():
    with open("list.pkl", "wb") as f:
        f.write(pickle.dumps(peopleList))

def get_person(peopleList, name):
    for p in peopleList:
        if p.name == name:
            #print("person already exists")
            return p
    else:
        print(name + " does not currently exist, would you like to create this person?y/n")
        uinput = input(">").lower()
        if(uinput == 'y'):
            person = Person(name)
            add_person(peopleList, person)
            return person
        else:
            return None


def print_people(peopleList):
    #sorted(peopleList, Person.birthyear)
    for p in peopleList:
        print(" %s | children: %s | parents: %s, %s | spouse: %s | Birth Year: %s | Age: %s" % (p.name, p.children, p.parent1,  p.parent2, p.spouse, p.birthyear, p.age))
    print("-----------------------")


def add_person(peopleList, person):
    peopleList.append(person)
    update_file()


# issue person remains as parent
def remove_person(peopleList, person):

    #if not get_person(peopleList, person.name):
    #    print("Person was not found")
    #else:
    for p in peopleList:
        if p.name == person.name:
            if p.spouse != '?':
                spouse = get_person(peopleList, p.spouse)
                spouse.spouse = '?'
            if len(p.children) is not 0:  # mark parent as removed
                for c in p.children:
                    kid = get_person(peopleList, c)
                    if p.name == kid.parent1:
                        kid.parent1 = '?'
                    if p.name == kid.parent2:
                        kid.parent2 = '?'
            peopleList.remove(p)

        if person.name in p.children: #remove person from list of children
            p.children.remove(person.name)

        update_file()

    else:
        print("Person was not found")

# issue of changing attributes could have to do with get_person function


def modify_person(peopleList, person):
    if get_person(peopleList, person.name):
        print("Modify How?")
        print("1) Modify Name\n2) Add Child\n3) Cancel")  # should become window option
        user_input = input(">")
        if user_input == "1":
            user_input2 = 'y'
            while user_input2 != 'y' or user_input2 != 'n':
                print("Modify Name?\n y/n")
                user_input2 = input(">").lower()
                if user_input2 == 'y':
                    new_name = input("Please enter the new first name: ")
                    #print(new_name)
                    person = person.set_name(new_name)
                    #peopleList.append(person1)
                    # person.set_name(new_name)
                    print(person)
                    # print(Joe.name)
                    break
                elif user_input2 == 'n':
                    print("Returning...")
                    break
                else:
                    print("Not valid: press y or n")

        elif user_input == "2":
            name = input("Enter child's name: ")
            new_child = Person(name)
            add_child(peopleList, person, new_child)

    else:
        print("Person was not found")


def add_spouse(peopleList, person1, person2):
    persona = get_person(peopleList, person1.name)
    personb = get_person(peopleList, person2.name)
    if persona is not None and personb is not None:
        persona.spouse = personb.name
        personb.spouse = persona.name
        # link any children previously set to parent to be children of spouse
        for c in personb.children:
            persona.children.add(c)
            ch = get_person(peopleList, c)
            add_parent(peopleList, persona, ch)
        for c in persona.children:
            personb.children.add(c)
            ch = get_person(peopleList, c)
            add_parent(peopleList, personb, ch)
    update_file()


def add_parent(peopleList, parent, child):
    p = get_person(peopleList, parent.name)
    c = get_person(peopleList, child.name)

    if p is not None and c is not None:
        p.children.add(c.name)

        if c.parent1 == '?':
            c.parent1 = p.name
            if p.spouse != '?':
                c.parent2 = p.spouse
                sp = get_person(peopleList, p.spouse)
                sp.children.add(c.name)
        elif c.parent2 == '?':
            c.parent2 = p.name

    update_file()


def add_child(peopleList, parent, child):

    parent.children.add(child.get_name())
    add_parent(peopleList, parent, child)
    if parent.spouse != '?':
        spouse = get_person(peopleList, parent.spouse)
        add_parent(peopleList, spouse, child)
    update_file()


def get_missing_parents(peopleList):
    for p in peopleList:
        if p.parent1 != '?':
            par = get_person(peopleList, p.parent1)
            if par.spouse != '?':
                p.parent2 = par.spouse

    update_file()

def set_birthyear(name, year):
    p = get_person(peopleList, name)
    p.birthyear = year
    p.get_age(year)
    update_file()
