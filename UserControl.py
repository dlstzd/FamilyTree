'''
This will be a file for user action rather than hard coding values in the family list
'''
import Family
#import PersonID
from PersonID import *
from tkinter import *
print("Hello User\nThis is a simple family tree program")
print("Several actions are listed, please select one or exit")
print("1) Print the family tree\n2) Add a new member\n3) Remove a member\n4) Modify a member\n5) Exit\n7) Add Child\n8) Add Spouse\n6) Print options")

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
        parent_name = input("Enter the parent: ")
        child_name = input("Enter the child name: ")

        parent = Family.get_person(Family.peopleList, parent_name)
        child = Family.get_person(Family.peopleList, child_name)
        if(parent is None or child is None):
            print("returning")
        else:
            Family.add_child(Family.peopleList, parent, child)
    elif num_select == "8":
        spouse1 = input("Enter Person: ")
        spouse2 = input("Enter Person: ")
        Family.add_spouse(Family.peopleList, spouse1, spouse2)
    else:
        print("Input not valid")

print("goodbye")
