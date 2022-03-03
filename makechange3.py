amount = float(input('Enter item cost: '))
tender = float(input('Enter amount tendered: '))

change = int((tender - amount)*100)
change = change % 100
quarters = change // 25
change = change % 25
dimes = change // 10
change = change % 10
nickels = change // 5
change = change % 5
pennies = change
#output
print('Quarters:', quarters)
print('Dimes:', dimes)
print('Nickels:', nickels)
print('Pennies:', pennies)