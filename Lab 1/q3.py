# -*- coding: utf-8 -*-
"""

# Approach
We have decided to create an Airline System.

- There are four classes in this system, which are Task3Flight, Task3Person, Task3Employee, and Task3Passenger.
## Task3Flight
This class focuses on the flight information such as its ID, departure and  destination places. It also has a variable for how many stops the flight will take.
The class stores the person Id as a private ID, and it stores the type of the person, which means it will determine whether the person is an employee or a passenger.
## Task3Person
This is a very important class since it takes the data of the flights, passangers, and employees. It also inherits the Task3Flight class.
## Task3Employee
It inherits from the Flight class, and it takes care of the Pilots data. 
## Task3Passenger
This is the class where we can add people for a flight. It is similar to the others in how it inherited the flight data.

Both classes, Task3Flight and Task3Person, are for storing the data whereas the others are used to insert the data.
"""

# We create a class for flight data in order to share its data items with the instances
# Class 1: it will contain variables for the flight like its ID, Departure and Destination, and so on.

class Task3Flight():
    # initiate the default constructor for this class
    def __init__(self, FlightIDt3, FlightDeparturet3, FlightDestinationt3, FlightStopst3, FlightTypet3, PersonIDt3, PersonTypet3):
        self.FlightIDt3 = FlightIDt3 # This is for the ID number of the flight
        self.FlightDeparturet3 = FlightDeparturet3 # This is for where the flight departs
        self.FlightDestinationt3 = FlightDestinationt3 # This is for where the flight will stop
        self.FlightStopst3 = FlightStopst3 # This is for the number of stops during the flight
        self.FlightTypet3 = FlightTypet3 # This is for what airline it's been used
        self.__PersonIDt3 = PersonIDt3 # here we store a unique ID for both a massenger and employee, and it is private
        self.PersonTypet3 = PersonTypet3 # This is to determine whether it's a Passenger or  an employee

# We  also create another class for the people data in order to share their information
# Class 2: it will inherit our superclass Task3Flight and has variables for people, such as their ids, names and so on.
class Task3Person(Task3Flight):
    # initiate the Task3Person class's constructor
    def __init__(self, PersonIDt3, PersonTypet3, PersonGendert3, PersonNamet3, PersonPhoneNumbert3, FlightIDt3, FlightDeparturet3, FlightDestinationt3, FlightStopst3, FlightTypet3):
        self.PersonNamet3 = PersonNamet3
        self.PersonGendert3 = PersonGendert3
        self.PersonPhoneNumbert3 = PersonPhoneNumbert3
        Task3Flight.__init__(self, FlightIDt3, FlightDeparturet3, FlightDestinationt3, FlightStopst3, FlightTypet3, PersonIDt3, PersonTypet3)

# Class 3: This class is for employees; it inherits the Task3Peron class to store the data
class Task3Employee(Task3Person):
    # initiating its constructor
    def __init__(self, PersonIDt3, PersonTypet3, PersonGendert3, PersonNamet3, PersonPhoneNumbert3, FlightIDt3, FlightDeparturet3, FlightDestinationt3, FlightStopst3, FlightTypet3):
        Task3Person.__init__(self, PersonIDt3, PersonTypet3, PersonGendert3, PersonNamet3, PersonPhoneNumbert3, FlightIDt3, FlightDeparturet3, FlightDestinationt3, FlightStopst3, FlightTypet3)

     # a method used in this class to get the employee's information
    def GetEmployeeT3(self):
        print("\033[91m{}\033[00m" .format("Pilot %s here is the information about the flight" % self.PersonNamet3))
        print("---")
        print("The flight number is:", self.FlightIDt3)
        print("Departure point is:", self.FlightDeparturet3)
        print("Destination point is:", self.FlightDestinationt3)

# Class 4: It is for passengers, and it also takes inheritance from Task3Peron class
class Task3Passenger(Task3Person):
    names, FPn = [], dict()
    # initiateint its default constructor
    def __init__(self, PersonIDt3, PersonTypet3, PersonGendert3, PersonNamet3, PersonPhoneNumbert3, FlightIDt3, FlightDeparturet3, FlightDestinationt3, FlightStopst3, FlightTypet3):
        Task3Person.__init__(self, PersonIDt3, PersonTypet3, PersonGendert3, PersonNamet3, PersonPhoneNumbert3, FlightIDt3, FlightDeparturet3, FlightDestinationt3, FlightStopst3, FlightTypet3)

        # we used dictionary to store the Flight Number as a key and the passenger name as the value
        if self.FlightIDt3 in Task3Passenger.FPn.keys():
            Task3Passenger.FPn[self.FlightIDt3].append(self.PersonNamet3)
        else:
            Task3Passenger.FPn[self.FlightIDt3] = [self.PersonNamet3]

        # This method is to print the passanger info.
    def GetPassangerT3(self):
        print("\033[91m{}\033[00m" .format("%s's flight details" % self.PersonNamet3))
        print("---")
        print("The Flight ID is:",   self.FlightIDt3)
        print("The Flight Type is:", self.FlightTypet3)
        print("Departure point is:", self.FlightDeparturet3)
        print("Destination point is:", self.FlightDestinationt3)

    # a method to print the passengers info. from the dictionary
    def GetTravelerT3(self):
        print("\033[91m{}\033[00m" .format("Those passengers who are on the flight:\n"))
        print(Task3Passenger.FPn)

# This is to insert information about a passenger
PassengerT3 = Task3Passenger("452", "Passenger", "Male", "Khalid", 7377810393, "F2115", "USA", "KSA", 3, "Delta Airlines")

#This method prints the travel details for the passenger
PassengerT3.GetPassangerT3()

# Adding information about an employee to the system
EmployeeT3 = Task3Employee("E234", "Employee", "Male", "Michael", 5125442475, "F1855", "USA", "KSA", 3, "Delta Airlines")
#This method will print the employee detail
EmployeeT3.GetEmployeeT3()

#This method prints the travelling passengers on that flight
# it is to print the passengers, who are trabelling 
PassengerT3.GetTravelerT3()