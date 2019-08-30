#ICP 2
#Muhammad Mohzary

# A program which reads weights (lbs.) of N students into a list and convert these weights to kilograms in a separate list using

# the convert function to convert ibs to kgs
def convertInput(weights):
    weightskg = []
    for w in weights:
        t = w / 2.205
        kgVal = round(t,2)
        weightskg.append(kgVal)
    return(weightskg)


#T ask user to enter the number of students
studentsN = int(input("Please enter the number of students: "))
# to initi the list
weightslbsList = []

# Using loop to enter student weights
for x in range(studentsN):
    w = float(input("Please enter student number " + str(x + 1) +" weight: "))
    weightslbsList.append(w)
print(weightslbsList)
# To call the convert function
print(convertInput(weightslbsList))