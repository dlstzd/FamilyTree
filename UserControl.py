'''
This will be a file for user action rather than hard coding values in the family list
'''
import Family
#import PersonID
from PersonID import *

print("Hello User\nThis is a simple family tree program")
print("Several actions are listed, please select one or exit")
print("1) Print the family tree\n2) Add a new member\n3) Remove a member\n4) Modify a member\n5) Exit\n7) Add Child\n6) Print options")
'''
num_select = 0

while(num_select != "5"):
    num_select = input(">")
    # print family list
    if(num_select == "1"):

        Family.print_people(Family.peopleList)
    # add family member
    elif(num_select == "2"):
        name = input("Name: ")
        person = Person(name)
        Family.add_person(Family.peopleList, person)

    # delete family member
    elif(num_select == "3"):
        name = input("Name: ")
        person = Person(name)
        Family.remove_person(Family.peopleList, person)
    # modify family member
    elif(num_select == "4"):
        name = input("Name: ")
        person = Person(name)
        Family.modify_person(Family.peopleList, person)
    elif(num_select == "5"):
        break
    elif(num_select == "6"):
        print("1) Print the family tree\n2) Add a new member\n3) Remove a member\n4) Modify a member\n5) Exit\n6) Print options")
    elif(num_select == "7"):
        parent = input("Enter the parent")
        if(Family.get_person(Family.peopleList, parent)):
            child_name = input("Enter the child name")
            child = Person(child_name)
            Family.add_child(Family.peopleList, parent, child)
    else:
        print("Input not valid")

print("goodbye")

'''
Dean = Person("Dean")
Devon = Person("Devon")
Michael = Person("Michael")
Alice = Person("Alice")
Zachary = Person("Zachary")
William = Person("William")
Anne = Person("Anne")

Family.add_person(Family.peopleList, Devon)
Family.add_child(Family.peopleList, Michael, Dean)
Family.add_person(Family.peopleList, Zachary)
Family.add_person(Family.peopleList, Alice)
Family.add_person(Family.peopleList, Michael)
Family.add_child(Family.peopleList, Alice, Devon)
Family.add_spouse(Family.peopleList, Michael, Alice)
#Family.add_parent(Family.peopleList, Alice, Devon)
Family.add_person(Family.peopleList, Dean)
Family.add_child(Family.peopleList, Michael, Zachary)
Family.add_person(Family.peopleList, William)
Family.add_child(Family.peopleList, Anne, William)
Family.add_child(Family.peopleList, Anne, Michael)




Family.print_people(Family.peopleList)
