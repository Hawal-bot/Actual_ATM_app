#   Register
# --firstname, lastname, password, email
# --generate user account

#   Login
# account number and password


#   Perform Bank operations 

import random   #for random account numbers
database = {}   #dictionary


#initializing a system
def init():

    print("Welcome to Bank G8")
    
    haveAccount = eval(input("Do you have an account with us? 1 (Yes)   2 (No)\n"))
    if(haveAccount == 1):
        login()
    
    elif(haveAccount == 2):
        register()
    
    else:
        print("Invalid option inputted. Try Again")
        init()


def login():
    print("**************Login to your Account****************")
    
    userAccount = eval(input("Enter your account number: \n"))
    password = input ("Enter password: \n")
    
    for accountNumber, userDetails in database.items():    #this line loops through the dic(database)
        if (accountNumber == userAccount):
            if (userDetails[3] == password):
                BankOperations(userDetails)    
        else:
            print ("Account Not Found\n")


def register():
    print("************************ Register *****************************")

    email = input("Enter your email address: \n")
    firstname = input("Enter your First name: \n")
    lastname = input("Enter your last name: \n")
    password = input("Enter your new password: \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [firstname, lastname, email, password]
    
    print("**********************************************************************")
    print("Your Account has been successfully created :)\n")
    print("Your Account Number is: %d" %accountNumber, "    and password is: %s" %password)
    print("**********************************************************************")    
    print("Make sure you dont share this with anyone...\n")

    login()



def BankOperations(user):
    print("Welcome, ", user[0], user[1])

    selectedOption = eval(input("What would you like to do today?  (1)Withdrawal   (2)Deposit  (3)Logout (4)Exit \n"))

    if (selectedOption == 1):
        withdrawalOperation()
    
    elif(selectedOption == 2):
        depositOperation()
    
    elif(selectedOption == 3):
        Logout()
    
    elif(selectedOption == 4):
        exit()
    
    else:
        print ("Invalid Option Selected\n")
        BankOperations()


#Making withdrawal operations
def withdrawalOperation():
    amountToWithdraw = eval(input("How much do you want to Withdrawal? \n"))
    print("Take your cash. \nThank you for banking with us :)")

    exitAction()


#   Making deposit actions
def depositOperation():
    amountToDeposit = eval(input("Enter amount to Deposit: \n"))
    print("Thank you for banking with us :)")

    exitAction()


#   Generating Account Number
def generateAccountNumber():
    return random.randrange(111111111,999999999)


def exitAction():
    
    userAction = eval(input("Would you like to perform another transaction? (1) Yes  (2) No \n"))
    
    if (userAction == 1):
        Logout()
    
    elif(userAction == 2):
        exit()

def Logout():
    login()



init()