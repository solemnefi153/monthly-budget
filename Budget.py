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
    
def getItemsInbudget():
    number = input('Enter number of items in budget: ')
    return number

def getItemName():
    itemName = input('Enter Item name: ')
    return itemName

def getItemMonthlyExpense():
    monthlyExpense = float(input('Enter item  monthly amount: '))
    return monthlyExpense 

def printReport(month, name, surname, itemsInBudget):

    print('')
    print('{} Monthly Budget for {} {}'.format(month, name, surname))
    print('{:=^50}'.format(''))
    print('{:<20}{:>10}{:>20}'.format('Item' ,'Month', 'Year'))
    print('{:=^50}'.format(''))
    for item in itemsInBudget:
        print('{:<20}${:>9.2f}          ${:>9.2f}'
          .format(item[0], item[1], (float(item[1]) * 12)))
    print('{:=^50}'.format(''))
    monthlyTotExp = 0
    for item in itemsInBudget:
        monthlyTotExp += float(item[1])
    yearlyTotExp = monthlyTotExp * 12
    print('{:<20}${:>9.2f}          ${:>9.2f}'
          .format('Totals', monthlyTotExp, yearlyTotExp))
    

    
#Driver Function 
def main():
    displayWelcomeMessage()
    month = getMonth()
    name = getFirstName()
    surname = getSurname()
    items = getItemsInbudget()
    itemsInBudget = []
    for i in range(int(items)):
        item_name = getItemName()
        item_cost = getItemMonthlyExpense()
        item = [item_name, item_cost]
        itemsInBudget.append(item)
    printReport(month, name, surname, itemsInBudget)


main()
