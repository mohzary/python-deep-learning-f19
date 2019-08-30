#ICP 2
#Muhammad Mohzary

#A program that returns every other char of a given string starting with first

# function to delete characters
def string_alternative(sentence):
    newSentence = slice(0,len(sentence),2)
    return(sentence[newSentence])

# Ask user to enter any sentence 
orginalString = str(input("Please type any sentence: "))

# Call the  string_alternative function and show the the final result
print("The sentence after delete characters : ")
print(string_alternative(orginalString))



