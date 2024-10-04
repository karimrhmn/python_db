# Json for saving and loading dictionaries to the txt file
import json

# Bool to trigger the program on and off
program = True

# Starting the program, and the main menue
while program:
    int_input = int(input("\nView the database: 1,\nAdd an entry: 2,\nRemove an entry: 3\nExit the program: 4\n:"))

    if int_input == 1:
        
        with open("data.txt", "r+") as file:
            storage = file.read()
            print(storage)
            print() 

    if int_input == 2:
        index = int(input("Enter your index number!: "))
        new_name = input("Enter your name!: ")
        new_age = int(input("Enter your age!: "))
        new_occ = input("What's your occupation!: ")
            
        new_entry = {"Index": index, "Name": new_name, "Age": new_age, "Occupation": new_occ}

        with open("data.txt", "a+") as file:
            file.write(json.dumps(new_entry) + "\n")
            print()

    if int_input == 3:
        #Delete function not usable yet
        pop_num = int(input("Enter the index number you wish to remove!: "))

        storage.pop(pop_num)

        print()

    if int_input == 4:
        program = False



#I'm pretty sure all the indentation above is not accurate :/

