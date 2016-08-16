'''
This will be a file for user action rather than hard coding values in the family list
'''
import Family
import PersonID

print("Hello User\nThis is a simple family tree program")
print("Several actions are listed, please select one or exit")
print("1) Print the family tree\n2) Add a new member\n3) Remove a member\n4) Modify a member\n5) Exit\n6) Print options")

num_select = 0

while(num_select != "5"):
    num_select = input(">")
    # print family list
    if(num_select == "1"):

        Family.print_people(Family.peopleList)
    # add family member
    elif(num_select == "2"):
        name = input("Name: ")
        person = PersonID.Person(name)
        Family.add_person(Family.peopleList, person)

    # delete family member
    elif(num_select == "3"):
        name = input("Name: ")
        person = PersonID.Person(name)
        Family.remove_person(Family.peopleList, person)
    # modify family member
    elif(num_select == "4"):
        name = input("Name: ")
        person = PersonID.Person(name)
        Family.modify_person(Family.peopleList, person)
    elif(num_select == "5"):
        break
    elif(num_select == "6"):
        print("1) Print the family tree\n2) Add a new member\n3) Remove a member\n4) Modify a member\n5) Exit\n6) Print options")
    else:
        print("Input not valid")

print("goodbye")