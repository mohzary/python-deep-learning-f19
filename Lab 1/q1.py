#Create Class to solve q1
class Task1Solution: 
    # using a method inside the class
    def Task1LongestSubstring(self, Task1UserInput): 
      # declaring variables and initilizing a set method
        TheLongest, TheLength, iset = '','', set() 

        # using a for loop to get every single character in the string
        for tui in range(0, len(Task1UserInput)):
            ise = Task1UserInput[tui]
            # cleaning TheLongest and iset set
            if ise in iset:
                TheLongest = ''
                iset.clear()
            # Adding the caracters to the variable TheLongest
            TheLongest = TheLongest + ise
            iset.add(ise)
            # if statement to check theLongest's and TheLength's value
            if len(TheLongest) > len(TheLength):
                # modifying the value of TheLength
                TheLength = TheLongest
        return TheLength


if __name__ == "__main__":
    # let the user enter a string/word
    Task1UserInput = input("Please write your string/word to get the output: ")
    
    # store the result of the class in Task1output when it's been called
    Task1output = Task1Solution().Task1LongestSubstring(Task1UserInput)

    print("\nYour string/word you entered is: " + Task1UserInput)
    print ("%s is the longest substring " % Task1output)