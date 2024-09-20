# Display My Coffe and Muffic Shop
print('***************************************')
print('My Coffee and Muffin Shop')
coffees = int(input('Number of coffees bought? ')) # Getting input of number of coffees from user.
muffins = int(input('Number of muffins bought? ')) # Getting input of number of muffins from user.
print('***************************************')
# Puts a white space.
print(' ')
# Display The receipt of the total cost, cost per item, and tax.
print('***************************************')
print('My Coffee and Muffin Shop Receipt')
print(str(coffees) + " Coffee at $5 each: $" + f"{coffees * 5:.2f}") # Total Cost of coffees, then formating the total to receive two decimal places.
print(str(muffins) + " Muffins at $4 each: $" + f"{muffins * 4:.2f}") # Total Cost of muffins, then formating the total to receive two decimal places.
subtotal = (coffees * 5) + (muffins * 4) # Calculating Total cost of coffees and muffins.
tax = round(subtotal * 0.06, 2) # Calculating the tax of the subtotal, then rounding it up to the hundredths
total = subtotal + tax # Calculating the Total Cost of subtotal and tax.
print('6% tax: $' + f"{tax:.2f}".lstrip('0')) # Telling the user there was a 6% of tax, then formating the tax to receive two decimal places, then afterwards removes the beginning zero of the 0.00 if there is one by using the lstrip function.
print('---------')
print('Total: $' + f"{total:.2f}") # Telling the user of the total cost, then formating the total to receive two decimal places.
print('***************************************')
