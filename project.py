# python_project_Command_Line_Checkbook_Application

# create a command line checkbook application that allows 
# users to track their finances with a command line interface.

# When run, the application should welcome the user,
#  and prompt them for an action to take:

  # - view current balance
  # - add a debit (withdrawal)
  # - add a credit (deposit)
  # - exit

# The application should persist between times that it is run,
# that is, if you run the application, add some credits,
# exit the application and run it again, you should still see 
# the balance that you previously created. 

# In order to do this, your application will need to store its data
# in a text file. Consider creating a file where each line
# in the file represents a single transaction.



    # making menu
    # working on sub routines
        # check balance
        # add
        # remove
    # also look at clearing screen before reprint of menu.



def print_menu():       ## Your menu design here
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Menu Option 1")
    print("2. Menu Option 2")
    print("3. Menu Option 3")
    print("4. Menu Option 4")
    print("5. Exit")
    print(67 * "-")
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")
     
    if int(choice) == 1:     
        print("Menu 1 has been selected")
        ## You can add your code or functions here
    elif int(choice) == 2:
        print("Menu 2 has been selected")
        ## You can add your code or functions here
    elif int(choice) == 3:
        print("Menu 3 has been selected")
        ## You can add your code or functions here
    elif int(choice) == 4:
        print("Menu 4 has been selected")
        ## You can add your code or functions here
    elif int(choice) == 5:
        print("Menu 5 has been selected")
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")
