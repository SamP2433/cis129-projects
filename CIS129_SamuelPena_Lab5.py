# Module 4 Lab-4
# Samuel Pena
# 10/11/24
# A bottle return program that loops 7 times asking for the number of bottles returned each day and repeats when asked

# declare keepGoing as 'y' so the loop on line 9 starts
keepGoing = str('y')

while keepGoing == 'y':
    # declare local variables
    totalBottles = 0 # Store's bottles values
    counter = 0        # Controls the loop
    todayBottles = 0 # Store's number of bottles returned on a day
    totalPayout = 0  # Calculated value of totalBottles times .10

    # Loops for the 7 days
    for counter in range(7):
        counter = counter + 1
        todayBottles = int(input('Enter number of bottles for day #' + str(counter) + ': '))
        totalBottles = totalBottles + todayBottles

    # Calcs The total payout and rounds it by the tenths place
    totalPayout = round(totalBottles * .1, 1)

    # Displays the user the totalBottles and totalPayout
    print(f'\nThe total number of bottles collected is {totalBottles}')
    print(f'The total paid out is $ {totalPayout}\n')

    # Askes the user if they want to do another week (another loop)
    print('Do you want to enter another week’s worth of data?')
    keepGoing = input('(Enter y or n) : ')