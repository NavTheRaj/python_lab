#WAP TO DEMONSTRATE DICTIONAARY OPERATIONS IN PYTHON

veg_dict={'Brinjal':10,'Cabbage':20,'Pumpkin':25}

print("-------------------\n")
#print("1.View list\n2.Add a new vegetable\n3.Change the price of an vegetable\n4.Delete the vegetable\n5.Quit!")

choice=0

while choice != 5 :
    print("1.View list\n2.Add a new vegetable\n3.Change the price of an vegetable\n4.Delete the vegetable\n5.Quit!")
    print("-------------------\n")
    choice=int(input("Enter your choice "))

    #CHOICE 1 TO SHOW THE ELEMENTS
    if choice == 1:
        print("-------------------\n")
        print(veg_dict)
        print("-------------------\n")

     #CHOICE 2 TO ADD THE NEW VEGETABLE SET
    elif choice == 2:
        print("-------------------\n")
        print("Your vegetable list\n")
        print(veg_dict)
        print("-------------------\n")
        veg_name=input("Enter the new vegetable-> ")
        print("-------------------\n")
        price=input('Enter price of '+veg_name+'-> ')
        print("-------------------\n")
        veg_dict.update({veg_name:price})
        print("Your new vegetable list\n")
        print(veg_dict)
        print("-------------------\n")

    #CHOICE 3 TO EDIT THE PRICE OF THE EXISTING VEGETABLE
    elif choice == 3:
        print("-------------------\n")
        print("Your vegetable list\n")
        print(veg_dict)
        print("-------------------\n")
        veg_change=""
        while veg_change not in veg_dict:
            veg_change=input("Enter the vegetable whose price you wanna change->")
            print("-------------------\n")
            if veg_change in veg_dict:
                print('Current price of '+veg_change+'-> '+str(veg_dict[veg_change]))
                price_change=input('Enter your updated price for '+veg_change+'->')
                print("-------------------\n")
                veg_dict[veg_change]=price_change
                print("Your new vegetable list\n")
                print(veg_dict)
                print("-------------------\n")
                break
            else:
                print("-------------------\n")
                print("Vegetable not found..Try again!")
                print("-------------------\n")

    #CHOICE 4 TO DELETE THE VEGETABLE FROM THE DICTIONARY
    elif choice == 4:
        print("-------------------\n")
        print("Your vegetable list\n")
        print(veg_dict)
        print("-------------------\n")
        veg_delete=""
        while veg_delete not in veg_dict:
            print("-------------------\n")
            veg_delete=input("Enter the vegetable to delete")
            if veg_delete in veg_dict:
                del veg_dict[veg_delete]
                print("-------------------\n")
                print("Deleted "+veg_delete+" successfully!")
                print("-------------------\n")

                break
            else:
                print("-------------------\n")
                print("Vegetable not found..Try again!")
                print("-------------------\n")

    #CHOICE 5 TO SAVE THE UPDATED LIST IN FILE AND EXIT THE PROGRAM
    elif choice == 5:
        print("-------------------\n")
        veg_file=open("veg.txt","w+")
        veg_file.write(str(veg_dict))
        veg_file.close()
        print("Saving the updated list and exiting..")
        exit()
    #CHOICE INVALID TO ITERATE THE WHILE LOOP
    else:
        print("-------------------\n")
        print("Invalid input..Try again!")
        print("-------------------\n")

