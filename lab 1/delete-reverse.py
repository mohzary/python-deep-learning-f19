# Muhammad Mohzary ICP 1
# Python script to delete at least 2 characters and reverse the result
  
# function to delete 2 characters and call the the reverse function
def deleteFromOriginal(string):

    # To show the first 3 characters in the word and from the 5th characters to the end
    string = string[0:3] + string[5:]
    return(string)
# Function to reverse a string 
def reverseString(string): 
    string = string[::-1] 
    return string 
# Ask user to enter any word 
orginalString = str(input("Please type any word: "))

# Call the delete function and stor the result in new variable
afterDelete = deleteFromOriginal(orginalString)

# Call the rverse function and show the the final result
print("The string after delete 2 characters and reverse it: ")
print(reverseString(afterDelete))