import csv
def validateString(msg):
    newValue = input(msg)
    while isInvalid(newValue):
        print('Error! Please enter a real name')
        newValue = input(msg)
    return newValue # only returns once the isInvalid() function returns a False, indicating it's good data

def isInvalid(test_value):
    if test_value.strip() == '' or test_value == None:
        return True #bad data
    if any(i.isdigit() for i in test_value):
        return True
    for character in list(test_value): #converts the test_value to a List and loops through each character one at a time
        if character in [',','.','?','!','@','#','$','%','^','&','*','(',')','[',']','-','_','=','+','/','\\']: #compare the current character to a list of known symbols
            return True #bad data
    return False #none of the previous checks resulted in bad data, must be good data!

def get_integer(msg):
    while True:
        try:
            new_value = int(input(msg))
            return new_value
        except ValueError:
            print('ERROR! Invalid input, please enter a whole number!')  

# Exercise 9.1
def exercise_nine_one():
    grades = [] # Table of grades given by the user
    total = 0  # sum of grades
    grade_counter = 0 # number of grades entered

    grade = get_integer('Enter grade, -1 to end: ')

    # processing phase
    while grade != -1:
        grades.append(grade)
        total += grade
        grade_counter += 1
        grade = get_integer('Enter grade, -1 to end: ')

    # termination phase
    if grade_counter != 0:
        average = total / grade_counter
        print(f'Class average is {average:.2f}')
        with open('grades.txt', mode='w') as grade_file:
            for i in range(len(grades)):
                grade_file.write(f'{str(i+1)} {str(grades[i])}\n')
            grade_file.write(f'Total Grades Entered: {str(grade_counter)}\n')
            grade_file.write(f'Class Average is {average:.2f}\n')

        exercise_nine_two()
    else:
        print('No grades were entered')

# Exercise 9.2
def exercise_nine_two():
    with open('grades.txt', mode='r') as grade_file:
        for record in grade_file:
            if record.startswith('Class') or record.startswith('Total'):
                print(record)
            else:
                index, grade = record.split()
                print(f'Grade {str(index)}: {str(grade)}')

# Exercise 9.3
def exercise_nine_three():
    with open('grades.csv', mode='w', newline='') as grade_file:
        writer = csv.writer(grade_file)
        while True:
            firstname = validateString("Enter student\'s first name ('done' to stop): ")
            if firstname.lower() == 'done':
                break
            lastname = validateString('Enter student\'s last name: ')
            exam1grade = get_integer('Enter Exam 1 grade: ')
            exam2grade = get_integer('Enter Exam 2 grade: ')
            exam3grade = get_integer('Enter Exam 3 grade: ')

            writer.writerow([firstname.title(),lastname.title(),exam1grade,exam2grade,exam3grade])


exercise_nine_one()
exercise_nine_three()