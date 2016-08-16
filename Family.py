from PersonID import *

#future issue each person needs a unique id
#or we list duplicate and allow the person to select the correct person --

Joe = Person("Joe Lund")
Liz = Person("Liz Pier")
Lydia = Person("Lydia Hill")
Scott = Person("Scott Hill")
Amanda = Person("Amanda Hill")
Peter = Person("Peter Morgan")
Anne = Person("Anne Piller")
Brian = Person("Brian Hill")
Tillie = Person("Tille Yown")

peopleList = []


def get_person(peopleList, name):
    for p in peopleList:
        if p.name == name:
            return p


def print_people(peopleList):
    for p in peopleList:
        print(p.name, " | children: %s" % p.children, " | parents: %s, %s" % (p.parent1,  p.parent2), " | spouse: %s" % p.spouse)

'''
def find_by_name(peopleList, name):
    for p in peopleList:
        if p.name == name:
            # print("Person found")
            return True
    return False
'''

def add_person(peopleList, person):
    if not get_person(peopleList, person.name):
        peopleList.append(person)
    #else:
        #print("person added")


# issue person remains as parent
def remove_person(peopleList, person):

    if not get_person(peopleList, person.name):
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


def add_spouse(peopleList, person1, person2):
    if person1 in peopleList and person2 in peopleList:
        person1.spouse = person2.name
        person2.spouse = person1.name
        for c in person2.children:
            person1.children.add(c)
        for c in person1.children:
            person2.children.add(c)
    else:
        print("One or more person are not currently in the tree")


def add_parent(peopleList, parent, child):
    if child in peopleList:

        if child.parent1 == '?':
            child.parent1 = parent.name
        elif child.parent2 == '?':
            child.parent2 = parent.name
            parent.spouse = child.parent1
            spouse = get_person(peopleList, child.parent1)

            add_spouse(peopleList, parent, spouse)
            '''
            parent.children = spouse.children
            spouse.spouse = parent.name
            '''



def add_child(peopleList, parent, child):
    if parent in peopleList:
        parent.children.add(child.name)

        add_parent(peopleList, parent, child)
        '''
        if child.parent1 == '?':
            child.parent1 = parent.fname + " " + parent.lname
        elif child.parent2 is '?':
            child.parent2 = parent.fname + " " + parent.lname
        '''


add_person(peopleList, Joe)
add_person(peopleList, Liz)
add_spouse(peopleList, Joe, Liz)
add_person(peopleList, Lydia)
add_person(peopleList, Peter)
add_spouse(peopleList, Peter, Lydia)
add_person(peopleList, Scott)
add_person(peopleList, Amanda)

add_person(peopleList, Anne)
add_person(peopleList, Brian)


add_child(peopleList, Lydia, Scott)
add_child(peopleList, Lydia, Amanda)
add_parent(peopleList, Peter, Scott)
add_child(peopleList, Anne, Lydia)
add_child(peopleList, Peter, Brian)


print_people(peopleList)

print("----------")
