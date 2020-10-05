"""
Author: Nefi Aguilar

Description:
  This program will create a report that will prompt the user for five different
  names of expenses and estimated amounts that the user has for this month.
  Then the program will display a report showing the five different expenses
  and an estimation of how much the user will spend a year for each item based on
  the monthly estimations.
"""

def displayWelcomeMessage():
    print('Welcome to the monthly budget program')
    print('-------------------------------------')
    print('')

def getMonth():
    month = input('Enter Month: ')
    return month
    
def getFirstName():
    name = input('Enter first name: ')
    return name
    
def getSurname():
    surname = input('Enter surname: ')
    return surname
    
def getItemName():
    itemName = input('Enter Item name: ')
    return itemName

def getItemMonthlyExpense():
    monthlyExpense = float(input('Enter Item 1 monthly amount: '))
    return monthlyExpense 

def printReport(month, name, surname, ite1, exp1, ite2, exp2, ite3, exp3,
                ite4, exp4, ite5, exp5):

    print('')
    print('{} Monthly Budget for {} {}'.format(month, name, surname))
    print('{:=^50}'.format(''))
    print('{:<20}{:>10}{:>20}'.format('Item' ,'Month', 'Year'))
    print('{:=^50}'.format(''))
    print('{:<20}${:>9.2f}          ${:>9.2f}'
          .format(ite1, exp1, (exp1 * 12)))
    print('{:<20}${:>9.2f}          ${:>9.2f}'
           .format(ite2, exp2, (exp2 * 12)))
    print('{:<20}${:>9.2f}          ${:>9.2f}'
          .format(ite3, exp3, (exp3 * 12)))
    print('{:<20}${:>9.2f}          ${:>9.2f}'
          .format(ite4, exp4, (exp4 * 12)))
    print('{:<20}${:>9.2f}          ${:>9.2f}'
          .format(ite5, exp5, (exp5 * 12)))
    print('{:=^50}'.format(''))
    monthlyTotExp = sum([exp1, exp2, exp3, exp4, exp5])
    yearlyTotExp = monthlyTotExp * 12
    print('{:<20}${:>9.2f}          ${:>9.2f}'
          .format('Totals', monthlyTotExp, yearlyTotExp))
    

    
#Driver Function 
def main():
    displayWelcomeMessage()
    month = getMonth()
    name = getFirstName()
    surname = getSurname()
    ite1 = getItemName()
    exp1 = getItemMonthlyExpense()
    ite2 = getItemName()
    exp2 = getItemMonthlyExpense()
    ite3 = getItemName()
    exp3 = getItemMonthlyExpense()
    ite4 = getItemName()
    exp4 = getItemMonthlyExpense()
    ite5 = getItemName()
    exp5 = getItemMonthlyExpense()
    printReport(month, name, surname, ite1, exp1, ite2, exp2, ite3, exp3, ite4,
                exp4, ite5, exp5)


main()
