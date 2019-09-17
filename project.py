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

def check_balance():
    print("this is the balance checker place holder")

def withdrawal():
    print("this is the withrawal place holder")

def deposit():
    print("this is the deposit")

def exit():
    print("you chose to exit - are you sure?")
    check_choice = input("Enter yes or no: ")
    #if check_choice.lower() == "yes":
    #   return loop = False
    #elif check_choice.lower() == "no":
    #    return loop = True
    #else:
    # #   return raw_input("Wrong option selection. Enter any key to try again..")



def print_menu():       ## Your menu design here
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. view current balance")
    print("2. add a debit (withdrawal)")
    print("3. add a credit (deposit)")
    print("4. Exit")
    print(67 * "-")
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")
     
    if int(choice) == 1:     
        print("Menu 1 - current balance has been selected")
        ## You can add your code or functions here
        check_balance()
    elif int(choice) == 2:
        print("Menu 2 - add a debit (withdrawal) has been selected")
        ## You can add your code or functions here
        withdrawal()
    elif int(choice) == 3:
        print("Menu 3 - add a credit (deposit) has been selected")
        ## You can add your code or functions here
        deposit()
    elif int(choice) == 4:
        print("Menu 4 has been selected")
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as 
        # not value of loop is set to False
        exit()
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")





