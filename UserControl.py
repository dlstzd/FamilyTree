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
Dean.get_age(1994)


class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.welcome = tk.Label(self, text= "Hello, this is a simple Family Tree program.\n\nSeveral options are listed, select one or exit\n__________________")

        self.button_1 = tk.Button(self, text="Print Family",
                                command=self.print_family, width=15, background='green')
        self.button_2 = tk.Button(self, text="Add Member",
                                command=self.add_member, width=15)
        self.button_3 = tk.Button(self, text="Remove Member",
                                command=self.remove_member, width=15, background='red')
        self.button_4 = tk.Button(self, text="Add Parent",
                                command=self.add_parent, width=15)
        self.button_5 = tk.Button(self, text="Add Spouse",
                                command=self.add_spouse, width=15)
        self.button_6 = tk.Button(self, text="Set Birth Year",
                                command=self.get_birthyear, width=15)
        self.welcome.pack(side="left")
        self.button_1.pack(side="top", expand=True, padx=10)
        self.button_2.pack(side="top", expand=True, padx=10)
        self.button_3.pack(side="top", expand=True, padx=10)
        self.button_4.pack(side="top", expand=True, padx=10)
        self.button_5.pack(side="top", expand=True, padx=10)
        self.button_6.pack(side="top", expand=True, padx=10)


    def print_family(self):
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Print Family Tree")

        Family.print_people(Family.peopleList)
        l = tk.Label(t, text="See Shell for output")
        l.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        #t.after(1000, t.destroy())

    def add_member(self):
        t = tk.Toplevel(self)
        t.wm_title("Add Member")
        l = tk.Label(t, text="Name: ")
        entry = tk.Entry(t)

        def on_button():
            s = entry.get()
            Family.get_person(Family.peopleList, s)
            t.after(1000, t.destroy())

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
            t.after(1000, t.destroy())

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
            Family.add_parent(Family.peopleList, parent, child)
            t.after(1000, t.destroy())

        button = tk.Button(t, text="Add", command=on_button)
        l.grid(row=0)
        l2.grid(row=1)
        entry1.grid(row=0, column=1)
        entry2.grid(row=1, column=1)
        button.grid(row=2)

    def add_spouse(self):
        t = tk.Toplevel(self)
        t.wm_title("Add Parent")
        l = tk.Label(t, text="Enter Name: ")
        l2 = tk.Label(t, text="Enter Name: ")
        entry1 = tk.Entry(t)
        entry2 = tk.Entry(t)

        def on_button():
            p_name = entry1.get()
            c_name = entry2.get()
            parent = Person(p_name)
            child = Person(c_name)
            Family.add_spouse(Family.peopleList, parent, child)
            t.after(1000, t.destroy())

        button = tk.Button(t, text="Add", command=on_button)
        l.grid(row=0)
        l2.grid(row=1)
        entry1.grid(row=0, column=1)
        entry2.grid(row=1, column=1)
        button.grid(row=2)

    def get_birthyear(self):
        t = tk.Toplevel(self)
        t.wm_title("Set Age")
        l = tk.Label(t, text="Name: ")
        l2 = tk.Label(t, text="Year Born: ")
        entry1 = tk.Entry(t)
        entry2 = tk.Entry(t)

        def on_button():
            p_name = entry1.get()
            age = int(entry2.get())
            #person = Person(p_name)
            Family.set_birthyear(p_name, age)
            t.after(1000, t.destroy())

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
