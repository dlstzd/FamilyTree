from PersonID import *

#future issue each person needs a unique id
#or we list duplicate and allow the person to select the correct person --

persona = Person("Joe Lund")
personb = Person("Liz Pier")
personc = Person("Lydia Hill")
persond = Person("Scott Hill")
persone = Person("Amanda Hill")
personf = Person("Peter Morgan")

peopleList = []


def print_people(peopleList):
    for p in peopleList:
        print(p.name, "children: %s" % p.children, "parents: %s, %s" % (p.parent1,  p.parent2), "spouse: %s" % p.spouse)
        print('\n')


def find_by_name(peopleList, name):
    for p in peopleList:
        if p.name == name:
            # print("Person found")
            return True
    return False


def add_person(peopleList, person):
    if not find_by_name(peopleList, person.name):
        peopleList.append(person)
    #else:
        #print("person added")


# issue person remains as parent
def remove_person(peopleList, person):

    if not find_by_name(peopleList, person.name):
        print("Person was not found")
    else:
        for p in peopleList:
            if p.fname == person.name:
                peopleList.remove(p)

        print("person deleted")


def modify_person(peopleList, person):
    print("must be edited")
    '''
    if find_by_name(peopleList, person.fname):
        print("Modify How?")
        print("1) Modify Name\n2) Add Child\n3) Cancel")  # should become window option
        user_input = input(">")
        if user_input == "1":
            print("Modify first or last name?\n1) First\n2) Last\n3) Cancel")
            user_input2 = input(">")
            if(user_input2 == "1"):
                new_first = input("Please enter the new first name: ")
                person.fname = new_first
            elif(user_input2 == "2"):
                new_last = input("Please enter the new last name: ")
                person.lname = new_last
            elif(user_input2 == "3"):
                print("Cancelled")
        elif user_input == "2":
            first_name = input("Enter child's first name")
            last_name = input("Enter child's last name")
            new_child = Person(first_name, last_name)
            add_child(peopleList, person, new_child)

    else:
        print("Person was not found")
    '''



def add_parent(peopleList, parent, child):
    if child in peopleList:
        if child.parent1 == '?':
            child.parent1 = parent.name
        elif child.parent2 == '?':
            child.parent2 = parent.name
            parent.spouse = child.parent1
            #find_by_name(peopleList, )

def add_child(peopleList, parent, child):
    if parent in peopleList:
        parent.children.append(child.name)

        add_parent(peopleList, parent, child)
        '''
        if child.parent1 == '?':
            child.parent1 = parent.fname + " " + parent.lname
        elif child.parent2 is '?':
            child.parent2 = parent.fname + " " + parent.lname
        '''



add_person(peopleList, persona)
add_person(peopleList, personb)
add_person(peopleList, personc)
add_person(peopleList, persond)
add_person(peopleList, persone)
add_person(peopleList, personf)

add_child(peopleList, personc, persond)
add_child(peopleList, personc, persone)
add_parent(peopleList, personf, persond)


print_people(peopleList)

print("----------")
