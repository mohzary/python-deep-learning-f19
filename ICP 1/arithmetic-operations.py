# Muhammad Mohzary ICP 1
# Python script to take two numbers from user and perform arithmetic operations on them

# Function to perform arithmetic operations such as  addition, subtraction, multiplication, and division on user inputs
def mathOperations(number1, number2):
    print("The addition of " + str(number1) + " & " + str(number2) + " is: " + str(number1 + number2))
    print("The subtraction of " + str(number1) + " & " + str(number2) + " is: " + str(number1 - number2))
    print("The multiplication of " + str(number1) + " & " + str(number2) + " is: " + str(number1 * number2))
    print("The division of " + str(number1) + " & " + str(number2) + " is: " + str(number1 / number2))

#To ask the user to enter two numbers

n1 = float(input("Please Enter the first number: "))
n2 = float(input("Please Enter the second number: "))

#To call the mathOperations function 
mathOperations(n1,n2)
