import mysql.connector
from mysql.connector import errorcode
import csv
import tkinter as tk
from tkinter import *

cnx = mysql.connector.connect(user='root',
                              password='root',
                              host='127.0.0.1',
                              port="3306"
                              #unix_socket= ''
                              )

DB_NAME = 'ränne_2'


cursor = cnx.cursor()

def create_database(cursor, DB_NAME):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

# creates the table marina and defines the columns
def create_table_marina(cursor):
    create_marina = "CREATE TABLE `marina` (" \
                     "  `id` int(20) NOT NULL," \
                     "  `name` varchar(50)," \
                     "  `dock_count` int(20),"\
                     "  PRIMARY KEY (`id`)" \
                     ") ENGINE=InnoDB"

    try:
        print("Creating table marina: ")
        cursor.execute(create_marina)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("table marina already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


# creates the table dock and defines the columns
def create_table_dock(cursor):
    create_dock = "CREATE TABLE `dock` (" \
                     "  `number` int(20) NOT NULL," \
                     "  `marina_id` int(20)," \
                     "  `max_capacity` int(20),"\
                     "  PRIMARY KEY (`number`)" \
                     ") ENGINE=InnoDB"

    try:
        print("Creating table dock: ")
        cursor.execute(create_dock)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("table dock already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


# creates the table boat and defines the columns
def create_table_boat(cursor):
    create_boat = "CREATE TABLE `boat` (" \
                     "  `id` int(20) NOT NULL," \
                     "  `name` varchar(50)," \
                     "  `owner_id` int(20),"\
                     "  `size` varchar(50)," \
                     "  `dock` int(20)," \
                     "  PRIMARY KEY (`id`)" \
                     ") ENGINE=InnoDB"

    try:
        print("Creating table boat: ")
        cursor.execute(create_boat)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("table boat already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


# creates the table person and defines the columns
def create_table_person(cursor):
    create_person = "CREATE TABLE `person` (" \
                     "  `id` int(20) NOT NULL," \
                     "  `name` varchar(50)," \
                     "  `boat_id` int(20),"\
                     "  `phone` varchar(50)," \
                     "  `email` varchar(50)," \
                     "  PRIMARY KEY (`id`)" \
                     ") ENGINE=InnoDB"

    try:
        print("Creating table person: ")
        cursor.execute(create_person)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("table person already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


# creates the table staff and defines the columns
def create_table_staff(cursor):
    create_staff = "CREATE TABLE `staff` (" \
                     "  `id` int(20) NOT NULL," \
                     "  `marina_id` int(20)," \
                     "  `name` varchar(50)," \
                     "  `phone` varchar(50),"\
                     "  `email` varchar(50)," \
                     "  `role` varchar(50)," \
                     "  PRIMARY KEY (`id`)" \
                     ") ENGINE=InnoDB"

    try:
        print("Creating table staff: ")
        cursor.execute(create_staff)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("table staff already exists.")
        else:
            print(err.msg)
    else:
        print("OK")



# use csv reader to insert values in to marina
def insert_into_marina(cursor):
    with open('marina.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        for line in csv_reader:
            x0 = line[0]
            x1 = line[1]
            x2 = line[2]

            #insert values in to table
            sql = "INSERT INTO marina (id,name,dock_count) VALUES (%s, %s, %s)"
            val = (x0, x1, x2)
            cursor.execute("USE {}".format(DB_NAME))
            cursor.execute(sql, val)
            cnx.commit()


# use csv reader to insert values in to dock
def insert_into_dock(cursor):
    with open('dock.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        for line in csv_reader:
            x0 = line[0]
            x1 = line[1]
            x2 = line[2]

            # insert values in to table
            sql = "INSERT INTO dock (marina_id,number,max_capacity) VALUES (%s, %s, %s)"
            val = (x0, x1, x2)
            cursor.execute("USE {}".format(DB_NAME))
            cursor.execute(sql, val)
            cnx.commit()


# use csv reader to insert values in to boat
def insert_into_boat(cursor):
    with open('boat.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        for line in csv_reader:
            x0 = line[0]
            x1 = line[1]
            x2 = line[2]
            x3 = line[3]
            x4 = line[4]

            # insert values in to table
            sql = "INSERT INTO boat (id,name,owner_id,size,dock) VALUES (%s, %s, %s, %s, %s)"
            val = (x0, x1, x2, x3, x4)
            cursor.execute("USE {}".format(DB_NAME))
            cursor.execute(sql, val)
            cnx.commit()


# use csv reader to insert values in to person
def insert_into_person(cursor):
    with open('person.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        for line in csv_reader:
            x0 = line[0]
            x1 = line[1]
            x2 = line[2]
            x3 = line[3]
            x4 = line[4]

            # insert values in to table
            sql = "INSERT INTO person (id,name,boat_id,phone,email) VALUES (%s, %s, %s, %s, %s)"
            val = (x0, x1, x2, x3, x4)
            cursor.execute("USE {}".format(DB_NAME))
            cursor.execute(sql, val)
            cnx.commit()


# use csv reader to insert values in to staff
def insert_into_staff(cursor):
    with open('staff.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        for line in csv_reader:
            x0 = line[0]
            x1 = line[1]
            x2 = line[2]
            x3 = line[3]
            x4 = line[4]
            x5 = line[5]

            # insert values in to table
            sql = "INSERT INTO staff (id,marina_id,name,phone,email,role) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (x0, x1, x2, x3, x4, x5)
            cursor.execute("USE {}".format(DB_NAME))
            cursor.execute(sql, val)
            cnx.commit()


# graphical interface to run the queries from.
def gui(cursor):

    root = Tk()

    frameQ = LabelFrame(root)
    frameQ.pack(padx=10, pady=10)


    def query_get_phone_number():

        output.delete("1.0", "end")
        boat_name = phone_entry.get()
        phone_entry.delete("0", "end")

        query = "SELECT boat.name as boat_name, person.name as owner, person.phone " \
                "FROM `boat` JOIN person ON boat.id = person.boat_id " \
                "WHERE boat.name = \"{}\"".format(boat_name)
        cursor.execute(query)
        result = cursor.fetchall()
        for y in result:
            #print(y)
            output.insert("1.0", y)

    def query_show_all_boats():

        output.delete("1.0", "end")

        query = "SELECT dock, size, count(*) as count " \
                "FROM boat GROUP BY size, dock " \
                "ORDER BY dock, size"
        cursor.execute(query)
        result = cursor.fetchall()

        output.insert("end", "dock, size class, count \n")

        for y in result:
            #print(y)
            output.insert("end", y)
            output.insert("end", "\n")

    def query_get_marina_capacity():

        output.delete("1.0", "end")
        marina_name = capacity_entry.get()
        capacity_entry.delete("0", "end")

        query = "SELECT marina.name, SUM(max_capacity) as marina_total_capacity " \
                "FROM marina JOIN dock ON marina.id = dock.marina_id " \
                "WHERE marina.name = \"{}\"".format(marina_name)
        cursor.execute(query)
        result = cursor.fetchall()

        output.insert("end", "name, capacity \n")

        for y in result:
            #print(y)
            output.insert("end", y)
            output.insert("end", "\n")

    def query_get_boat_count():
        output.delete("1.0", "end")
        dock_number = boat_count_entry.get()
        boat_count_entry.delete("0", "end")

        query = "SELECT count(*) as boats_at_dock_1 " \
                "FROM `boat` " \
                "WHERE boat.dock = \"{}\"".format(dock_number)
        cursor.execute(query)
        result = cursor.fetchall()

        output.insert("end", "boats at dock " + dock_number + ": \n")

        for y in result:
            #print(y)
            output.insert("end", y)
            output.insert("end", "\n")

    def query_show_used_capacity_view():
        cursor.execute("SELECT * FROM v_marina_used_capacity")
        output.delete("1.0", "end")
        result = cursor.fetchall()

        output.insert("end", "name, used capacity \n")
        output.insert("end", result)


    def query_staff_count_by_role():
        output.delete("1.0", "end")

        query = "SELECT role, count(*) as count " \
                "FROM staff GROUP BY role " \
                "ORDER BY count DESC"
        cursor.execute(query)
        result = cursor.fetchall()

        output.insert("end", "role, count \n")

        for y in result:
            # print(y)
            output.insert("end", y)
            output.insert("end", "\n")


    def query_staff_list_from_role():
        output.delete("1.0", "end")
        role = staff_from_role_entry.get()
        marina = staff_from_role_entry2.get()

        staff_from_role_entry.delete("0", "end")
        staff_from_role_entry2.delete("0", "end")

        query = "SELECT staff.name, staff.role, staff.phone, staff.email " \
                "FROM staff JOIN marina ON staff.marina_id = marina.id " \
                "WHERE role= \"{}\" AND marina.name= \"{}\"".format(role, marina)
        cursor.execute(query)
        result = cursor.fetchall()

        output.insert("end", "name, role, phone, email \n")

        for y in result:
            # print(y)
            output.insert("end", y)
            output.insert("end", "\n \n")





    #get phone number
    button_phone = Button(frameQ, text="get phone number", command=query_get_phone_number, padx=45)
    button_phone.grid(row=1, column=0)

    phone_entry = Entry(frameQ, width=25)
    phone_entry.insert(0, "enter boat name")
    phone_entry.grid(row=1, column=1)

    #check marina capacity
    button_capacity = Button(frameQ, text="show marina total capacity", command=query_get_marina_capacity, padx=24)
    button_capacity.grid(row=2, column=0)

    capacity_entry = Entry(frameQ, width=25)
    capacity_entry.insert(0, "enter marina name")
    capacity_entry.grid(row=2, column=1)

    #group boat by size, dock
    button_group_boat = Button(frameQ, text="show all boats (grouped)", command=query_show_all_boats, padx=29)
    button_group_boat.grid(row=3, column=0)

    group_boat_entry = Entry(frameQ, width=25)
    group_boat_entry.insert(0, "no input needed!")
    group_boat_entry.grid(row=3, column=1)

    #get boat count at dock
    button_boat_count = Button(frameQ, text="show boat count at dock", command=query_get_boat_count, padx=29)
    button_boat_count.grid(row=4, column=0)

    boat_count_entry = Entry(frameQ, width=25)
    boat_count_entry.insert(0, "enter dock number")
    boat_count_entry.grid(row=4, column=1)

    #marina used capacity
    button_boat_count = Button(frameQ, text="show marina used capacity", command=query_show_used_capacity_view, padx=23)
    button_boat_count.grid(row=5, column=0)

    used_capacity_entry = Entry(frameQ, width=25)
    used_capacity_entry.insert(0, "no input needed!")
    used_capacity_entry.grid(row=5, column=1)

    #group staff by role
    button_staff_role = Button(frameQ, text="show staff count by role", command=query_staff_count_by_role, padx=31)
    button_staff_role.grid(row=6, column=0)

    staff_role_entry = Entry(frameQ, width=25)
    staff_role_entry.insert(0, "no input needed!")
    staff_role_entry.grid(row=6, column=1)

    #get staff from role
    button_staff_role = Button(frameQ, text="get staff from role", command=query_staff_list_from_role, padx=47)
    button_staff_role.grid(row=7, column=0)

    staff_from_role_entry = Entry(frameQ, width=25)
    staff_from_role_entry.insert(0, "enter role name")
    staff_from_role_entry.grid(row=7, column=1)
    staff_from_role_entry2 = Entry(frameQ, width=25)
    staff_from_role_entry2.insert(0, "enter marina name")
    staff_from_role_entry2.grid(row=7, column=2)

    #Output
    frameO = LabelFrame(root)
    frameO.pack(padx=10,pady=10)

    outputLabel = Label(frameO, text="Output")
    outputLabel.grid(row=0,column=0)

    output = Text(frameO, undo=True, height=16, width=40)
    output.grid(row=1,column=0)



    root.mainloop()


def create_view():
    query = "create view v_marina_used_capacity as " \
            "SELECT marina.name, count(*) " \
            "FROM marina JOIN dock ON marina.id = dock.marina_id JOIN boat ON dock.number = boat.dock " \
            "GROUP BY marina.name"
    cursor.execute(query)


# try to open gui
try:
    cursor.execute("USE {}".format(DB_NAME))
    gui(cursor)

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database {} does not exists.".format(DB_NAME))
        create_database(cursor, DB_NAME)
        print("Database {} created successfully.".format(DB_NAME))

        cnx.database = DB_NAME

        create_table_marina(cursor)
        insert_into_marina(cursor)

        create_table_dock(cursor)
        insert_into_dock(cursor)

        create_table_boat(cursor)
        insert_into_boat(cursor)

        create_table_person(cursor)
        insert_into_person(cursor)

        create_table_staff(cursor)
        insert_into_staff(cursor)

        create_view()

        gui(cursor)
    else:
        print(err)
