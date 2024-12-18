# Lab 12
# Samuel Pena 
# 12/17/24

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

class Pet:
    # Constructor
    def __init__(self, n='', t='', a=0): # Found this in 10.2.2 and 10.4.1
        self.name = n
        self.type = t
        self.age = a

    # Mutators
    def setName(self, name):
        self.name = name
	
    def setType(self, type):
        self.type = type
		
    def setAge(self, age):
        self.age = age

    # Accessors
    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAge(self):
        return self.age

def main():
	# Declare input variables
    inputName = ''
    inputType = ''
    inputAge = 0

    # Class variable to hold a pet
    Animal = Pet()

    inputName = validateString('Enter a pet name: ')
    Animal.setName(inputName)

    inputType = validateString('Enter a pet type: ')
    Animal.setType(inputType)
		
    inputAge = get_integer('Enter a pet age:')
    Animal.setAge(inputAge)
		
    print('The pet name :', Animal.getName())
    print('The pet type :', Animal.getType())
    print('The pet age :',  Animal.getAge())

main()