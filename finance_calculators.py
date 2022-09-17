import math


#Prompt the user to choose investment or bond calculator, and explains what each calculator does.
print("Choose either 'investement' or 'bond' from the menu below to proceed: \n")
print("investment - to calculate the amount of interest you'll earn on interest")
print("bond - to calculate the amount you'll have to pay on a home loan \n")

calculator_type = input()  #The user's input is assigned to 'calculator type'.

print("\n")                #Creates a blank line so the output is not cluttered.

#If the user inputs investment then they will be prompted to enter the deposit amount, interest rate, number of years, and interest type (i.e simple or compound).
if calculator_type == "investment":                                                  #If the user inputs investment then:
    
    deposit = float(input("Enter the amount of money that you are depositing: \n"))  #The user is prompted to enter the deposit amount which is converted to float and assigned to 'deposit'.
    print("\n")


    interest_rate = int(input("Enter the interest rate: \n"))         #The user is prompted to enter the interest rate which is converted to an integer and assigned to 'interest_rate'.
    interest_rate1 = float(interest_rate/100)                         #'interest_rate' is divided by 100, which is then converted to float and assigned to 'interest_rate1'.
    rate = round(interest_rate1, 2)                                   #'interest_rate1' is rounded off to two decimals and assigned to 'rate'.
    print("\n")

    
    num_of_years = int(input("Enter the number of years you plan on investing for: \n"))    #Requests the user to enter the number of years the plan to invest, converts it to integer and assigns it to 'num_of_years'.
    print("\n")

    
    interest_type = input("Enter your choice of interest of interest below: \n 'simple' or 'compound': ") #Requests the user to enter simple or compound and assigns it to 'interst_type'.
    print("\n")


    simple = round(float(deposit * (1 + rate * num_of_years)), 2)          #Formula to calculate the total amount the user will receive after investment period if they chose simple interest, which is converted to float, rounded off to two decimals, and assigned to 'simple'.
    compound = round(float(deposit*math.pow((1 + rate), num_of_years)), 2) #Formula to calculate the total amount the user will receive after investment period if they chose compound interest, which is converted to float, rounded off to two decimals, and assigned to 'compound'.


    if interest_type == "simple":        #If the user inputs simple then it prints out the calculated interest rate formula for 'simple'.
        print("The total amount with interest added is R{}".format(simple))
        
    elif interest_type == "compound":    #Else if the user inputs compound then it prints out the calculated interest rate formula 'compound'.
            print("The total amount with interest added is R{}".format(compound))
            
    else:                                #Else if the user inputs anything other than simple or compound then an error message is printed.
        print("You have entered an invalid response.")


elif calculator_type == "bond":          #Else if the user inputs bond then they will be prompted to input value of the house, interest rate, and number of months to repay the bond.

    house_value = float(input("Enter the present value of the house: \n"))  #User's input for present value of house is converted to float and assigned to 'house-value'.
    print("\n")

    #Interest rate is calculated by dividing it by 100, and thereafter dividing it by 12 (months).
    interest_rate = float(input("Enter the interest rate: \n"))             #User's input for interest rate is converted to float and assigned to 'interest_rate'.
    interest_rate_1 = float(interest_rate/100)                              #'interest_rate' is divided by 100, converted to float and assigned to 'interest_rate_1'.
    monthly_interest = (interest_rate_1/12)                                 #'interest_rate_1' is divided by 12 and assigned to 'monthly_interest'.
    print("\n")

    num_of_months = int(input("Enter the number of months to repay the bond: \n"))  #User's input for number of months to repay bond is converted to integer and assigned to 'num_of_months'
    print("\n")

    #monthly_interest, house_value, and num_of_months are assigned to single characters to shorten the spaces needed for the repayment formula.
    i = monthly_interest
    p = house_value
    n = num_of_months


    repayment = (i*p)*(1/(1 - (1+i)**(-n)))    #Formula for the monthly repayment rate is calculated and assigned to 'repayment'.
    monthly_repayment = round((repayment), 2)  #'repayment' is rounded off to two decimals and assigned to 'monthly_repayment'.

    print("The monthly repayment is R{}".format(monthly_repayment))      #Prints out "The monthly repayment is " + 'monthly_repayment'.


else:                                               #Else the user enters anything other than 'investment' or 'bond' then:
    print("You have entered an invalid response.")  #It prints out "You have entered an invalid response."

    
