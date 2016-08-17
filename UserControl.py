'''
This will be a file for user action rather than hard coding values in the family list
'''
import Family
from PersonID import *
import tkinter as tk
import sys
import time

Dean = Person("Dean")
Zach = Person("Zach")
Devon = Person("Devon")
Alice = Person("Alice")
Family.add_person(Family.peopleList, Dean)
Family.add_person(Family.peopleList, Zach)
Family.add_person(Family.peopleList, Devon)
Family.add_person(Family.peopleList, Alice)


class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.welcome = tk.Label(self, text= "Hello, this is a simple Family Tree program.\n\nSeveral options are listed, select one or exit\n__________________")

        self.button_1 = tk.Button(self, text="Print Family",
                                command=self.print_family)
        self.button_2 = tk.Button(self, text="Add Member",
                                command=self.add_member)
        self.button_3 = tk.Button(self, text="Remove Member",
                                command=self.remove_member)
        self.button_4 = tk.Button(self, text="Add Parent",
                                command=self.add_parent)

        self.welcome.pack(side="left")
        self.button_1.pack(side="top", expand=True)
        self.button_2.pack(side="top", expand=True)
        self.button_3.pack(side="top", expand=True)
        self.button_4.pack(side="top", expand=True)



    def print_family(self):
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Print Family Tree")

        Family.print_people(Family.peopleList)
        l = tk.Label(t, text="See Shell for output")
        l.pack(side="top", fill="both", expand=True, padx=50, pady=50)

    def add_member(self):
        t = tk.Toplevel(self)
        t.wm_title("Add Member")
        l = tk.Label(t, text="Name: ")
        entry = tk.Entry(t)

        def on_button():
            s = entry.get()
            Family.get_person(Family.peopleList, s)
            time.sleep(1)
            t.destroy()

        button = tk.Button(t, text="Add", command=on_button)
        l.grid(row=0)
        entry.grid(row=0, column=1)
        button.grid(row=1)

    def remove_member(self):
        t = tk.Toplevel(self)
        t.wm_title("Remove Member")
        l = tk.Label(t, text="Name: ")
        entry = tk.Entry(t)

        def on_button():
            s = entry.get()
            g = Person(s)
            Family.remove_person(Family.peopleList, g)
            time.sleep(1)
            t.destroy()

        button = tk.Button(t, text="Remove", command=on_button)
        l.grid(row=0)
        entry.grid(row=0, column=1)
        button.grid(row=1)
    def add_parent(self):
        t = tk.Toplevel(self)
        t.wm_title("Add Parent")
        l = tk.Label(t, text="Parent Name: ")
        l2 = tk.Label(t, text="Child Name: ")
        entry1 = tk.Entry(t)
        entry2 = tk.Entry(t)

        def on_button():
            p_name = entry1.get()
            c_name = entry2.get()
            parent = Person(p_name)
            child = Person(c_name)
            #Family.remove_person(Family.peopleList, g)
            Family.add_parent(Family.peopleList, parent, child)
            time.sleep(1)
            t.destroy()

        button = tk.Button(t, text="Add", command=on_button)
        l.grid(row=0)
        l2.grid(row=1)
        entry1.grid(row=0, column=1)
        entry2.grid(row=1, column=1)
        button.grid(row=2)

if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True, padx=50, pady=50)
    root.mainloop()



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
'''

