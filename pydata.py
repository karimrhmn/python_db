# Imports
import sqlite3



# Creating and /or connecting to the database 
conn = sqlite3.connect("data.db")

# Creating the cursor
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        occupation TEXT
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()



# Function - View the database
#def view_db():

# Function - Add an entry
#def add_entry():

# Function - Delete an entry
#def del_entry():

# Bool to trigger the program on and off
program = True



# Starting the program, and the main menue
while program:
    int_input = int(input("\nView the database: 1,\nAdd an entry: 2,\nRemove an entry: 3\nExit the program: 4\n:"))

    if int_input == 1:

        # Reconnect to the server
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        
        # Fetch all data
        cursor.execute("SELECT * FROM people")
        people = cursor.fetchall()

        # Print all data
        for i in people:
            print(i)

        # Close the connection
        conn.close()


    if int_input == 2:

        user_name = input("Enter your first name!: ")
        user_age = int(input("Enter your age!: "))
        user_occ = input("What's your occupation!: ")


        # Reconnect to the server
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        # Add entry
        cursor.execute('''
         INSERT INTO people (name, age, occupation) 
          VALUES (?, ?, ?)
        ''', (user_name, user_age, user_occ))
        
        conn.commit()
        conn.close()

    if int_input == 3:

        user_prompt = input("Would you like to delete by name or by id?\nReply with 'name' or 'id'! ")

        if user_prompt == "name":

            #Gather name from user
            del_request = input("Enter the name you'd like to delete: ")


            # Connect to the server
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()

            # Delete the chosen user
            cursor.execute('''
            DELETE FROM people WHERE name = ?
            ''', (del_request,))

            # Commit changes and close server
            conn.commit()
            conn.close()
        
        elif user_prompt == "id":

            #Gather id from user
            del_request = int(input("Enter the id you'd like to delete: "))

            # Connect to the server
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()

            # Delete the chosen user
            cursor.execute('DELETE FROM people WHERE id = ?', (del_request,))

            # Commit changes and close server
            conn.commit()
            conn.close()
        else:
            print()
            print("Sorry you need to type either 'name' or 'id?")


    if int_input == 4:
        program = False

#Next update will make use of the functions in python