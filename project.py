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

  # DONT RUN THIS
# def exit():
    #print("you chose to exit - are you sure?")
    #check_choice = input("Enter yes or no: ")
    #if check_choice.lower() == "yes":
    #   return loop = False
    #elif check_choice.lower() == "no":
    #    return loop = True
    #else:
    # #   return raw_input("Wrong option selection. Enter any key to try again..")


def print_menu():       ## Your menu design here
    #print(30 * "-" , "MENU" , 30 * "-")
    print("\n")
    print("~~~ Welcome to your terminal checkbook! ~~~")
    print("\n")
    print("What would you like to do?")
    print("\n")
    print("1. view current balance")
    print("2. add a debit (withdrawal)")
    print("3. add a credit (deposit)")
    print("4. Exit")
    print(67 * "-")
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-4]: ")
     
    if choice == '1':     
        print("Menu 1 - current balance has been selected")
        ## You can add your code or functions here
        check_balance()
    elif choice == '2':
        print("Menu 2 - add a debit (withdrawal) has been selected")
        ## You can add your code or functions here
        withdrawal()
    elif choice == '3':
        print("Menu 3 - add a credit (deposit) has been selected")
        ## You can add your code or functions here
        deposit()
    elif choice == '4':
        print("Menu 4 has been selected")
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as 
        # not value of loop is set to False
        #exit()  # turned the fx exit() off
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")






### going over optimistic steps for reading balance function

# open file
    # read text - convert if necessary ie JSON imports as str?
    # find last balance
        # return to menu with balance info

### going over optimistic steps for withrawal function
    # open file
        # check the balance IF withdraw > balance then:
                # YOU CAN ONLY WITHDRAW UPTO ... balance
            # ELSE subtract amount from balance AND
                # write a new balance
        # return to menu with new_balance info

### going over optimistic steps for credit function
    # open file
        # add credit_amount to balance
        # write a new balance
        # return to menu with new_balance info

######### ||||||||||||||||||||||||||||||||||||||  ###########
#####   DICT and JSON file schema

  #----- Fx Variables
  # read file - get running_balance
  check_balance Fx
current_balance = call JSON file
     find transactions[-1], get running_balance # find the last transaction
       # note - might have to add transaction_ID as integer and perform an order function
          # due to string ordering vs number ordering, ie  1, 2, 22, 3 vs 1, 2, 3, 22
        return running_balance

  make withdrawal Fx
      get withrawal_amount_to_check
      call JSON file, call check_balance fx
       IF withrawal_amount_to_check > current_balance then:
                YOU CAN ONLY WITHDRAW UPTO ... balance
        ELSE subtract amount from current_balance AND
                write a new balance to running_balance
                save to JSON file
        call check_balance fx , get current_balance
        return to menu with current_balance info
    
make deposit Fx
      call JSON file, get running_balance
       deposit_to_write = add amount_to_credit to running_balance
      save amount_to_credit and running_balance to JSON file



  #---- dictionary 
tranaction_ID # for keeping track of transactions
running_balance # actually balance at open before read and writing JSON file
time_stamp # use a time function to write a simple time stamp to each transaction
  # optional
  category # to list the category - make menu list?
  description # default to "BLANK" if nothing noted

