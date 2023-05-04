import psycopg2
import os, csv
connection = psycopg2.connect(
    host="localhost",
    dbname = "postgres",
    user = "postgres",
    password = "1234",
    port = 5432)

cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS phone_book(
name VARCHAR(225),
number VARCHAR(225) PRIMARY KEY
);""")


def execute(comm):
    option = ""
    key = ""

    if(comm=="ADD"):
        option = input("Print CONSOLE to add by console "+"\n"+
                       "Print CSV to add by csv file")
        if(option == "CONSOLE"):
            os.system('cls')
            name_=input("NAME: ")
            phone_ = input("PHONE: ")
            cursor.execute("""INSERT INTO phone_book (name,number) VALUES (%s,%s)""", (name_,phone_) )
        if(option == "CSV"):
            with open(r'C:\Users\77002\Desktop\LAB10 PP2\test.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                   print(row)
                   cursor.execute("INSERT INTO phone_book (name,number) VALUES (%s,%s)",row)
        connection.commit()
    if(comm == "DELETE"):
        os.system('cls')
        option = input("Print NAME to delete by name"+"\n"+
                       "Print PHONE to delete by phone"+"\n")
        if(option == "NAME"):
            key = input("NAME: ")
            cursor.execute("""DELETE FROM phone_book WHERE name = %s""",(key,))
        if(option == "PHONE"):
            key = input("PHONE: ")
            cursor.execute("""DELETE FROM phone_book WHERE number = %s""",(key,))
        connection.commit()
    if(comm == "SHOW"):
        os.system('cls')
        cursor.execute("""SELECT name, number FROM phone_book ORDER by name""")
        rows = cursor.fetchall()
        print("Total number of people: ",cursor.rowcount)
        for row in rows:
            print(row)
    if(comm == "UPDATE"):
        option = input("Print NAME to update name"+"\n"+
                       "Print PHONE to phone phone"+"\n")
        if(option == "NAME"):
            key = input("PHONE: ")
            new_value = input("NEW NAME: ")
            cursor.execute("""UPDATE phone_book SET name = %s WHERE number = %s""",(new_value,key))
        if(option == "PHONE"):
            key = input("NAME: ")
            new_value = input("NEW PHONE: ")
            cursor.execute("""UPDATE phone_book SET number = %s WHERE name = %s""",(new_value,key))
        connection.commit()
    if(comm== "SEARCH"):
        key = input("PATTERN: ")
        cursor.execute("""SELECT * FROM phone_book WHERE name LIKE """+"\'%"+key+"%\'")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    if(comm=="FILTER"):
        key = input("PATTERN: ")
        offset = input("OFFSET: ")
        limit = input("LIMIT: ")
        cursor.execute("""SELECT * FROM phone_book WHERE name LIKE """+"\'%"+key+"%\'"+"""OFFSET %s LIMIT %s""", (offset,limit))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
os.system('cls')
running = True
while(running):
    command = input("Type ADD to add a phone number to the phone_book"+"\n"+
                    "Type DELETE to delete a phone number"+"\n"+
                    "Type UPDATE to update contact info by name"+"\n"+
                    "Type SHOW to print all data"+"\n"+
                    "Type FILTER to search by pattern, offset and limit"+"\n"+
                    "Type SEARCH to search by name"+"\n"+
                    "Type EXIT to exit"+"\n"+"\n")
    execute(command)
    
connection.commit()
cursor.close()
connection.close()
