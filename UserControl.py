'''
This will be a file for user action rather than hard coding values in the family list
'''
import Family
import PersonID

print("Hello User\nThis is a simple family tree program")
print("Several actions are listed, please select one or exit")
print("1) Print the family tree\n2) Add a new member\n3) Remove a member\n4) Modify a member\n5)Exit")

num_select = 0

while(num_select != "5"):
    num_select = input(">")
    if(num_select == "1"):

        Family.print_people(Family.peopleList)
    elif(num_select == "2"):
        firstname = input("First Name: ")
        lastname = input("Last Name: ")
        person = PersonID.Person(firstname, lastname)
        Family.add_person(Family.peopleList, person)
        print("person added")
    elif(num_select == "3"):
        firstname = input("First Name: ")
        lastname = input("Last Name: ")
        person = PersonID.Person(firstname, lastname)
        Family.remove_person(Family.peopleList, firstname, lastname)
    elif(num_select == "4"):
        firstname = input("First Name: ")
        lastname = input("Last Name: ")
        person = PersonID.Person(firstname, lastname)
        Family.modify_person()
    elif(num_select == "5"):
        break
    else:
        print("Input not valid")

print("goodbyue")