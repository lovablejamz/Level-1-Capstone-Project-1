# Level-1-Capstone-Project-1

This program (finance_calculators.py) allows the user to access two different financial calculators:
1 - an investment calculator
2 - a home loan repayment calculator

The investment calculator is used to calculate the amount of interest the user will earn on interest.
This is calculated by prompting the user to input the fillowing:
- the deposit amount
- the interest rate
- the number of years the user plans on investing for

After inputting the above details, the user is then prompted to choose between "simple" or "compound" interest.
Simple interest is calculated using the following formula:
> simple = P x (1 + i x t)
> P = deposit
> i = interest rate
> t = number of years
Compound interest is calculated using the following formula:
> compound = P x math.pow((1 + i), t)
> P = deposit
> i - interest rate
> t = number of years

The home loan repayment calculator ("Bond") prompts the user to input the following:
- the present value of the house
- the interest rate
- the number of months they plan to take to repay the bond.

The Bond repayment calculator formula is as follows:
> repayment = (i x p) x (1/ (1 - (1 + i) x (-n)))
> i = monthly interest
> p = house value
> n = number of months
