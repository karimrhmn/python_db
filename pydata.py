program = True

storage = {
    
    1: {"Name": "Karim", "Age": "23", "Occupation": "Courier"},
    2: {"Name": "Essa", "Age": "16", "Occupation": "Student"}

    }

while program:
    int_input = int(input("\nView the database: 1,\nAdd an entry: 2,\nRemove an entry: 3\n:"))

    if int_input == 1:
        print(storage) 

        print() 

    elif int_input == 2:
        index = int(input("Enter your index number!: "))
        new_name = input("Enter your name!: ")
        new_age = int(input("Enter your age!: "))
        new_occ = input("What's your occupation!: ")

        storage[index] = {"Name": new_name, "Age": new_age, "Occupation": new_occ}
        
        print()
        

    elif int_input == 3:
        pop_num = int(input("Enter the index number you wish to remove!: "))

        storage.pop(pop_num)

        print()

    else:
        print("Error, you haven't selected a number")


#I'm pretty sure all the indentation above is not accurate :/

