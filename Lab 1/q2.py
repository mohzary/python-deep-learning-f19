# To create Python object of type tuple

studentTuple = (( 'John', ('Physics', 80)) , ('Daniel', ('Science', 90)), ('John', ('Science', 95)), ('Mark',('Maths', 100)), ('Daniel', 
('History', 75)), ('Mark', ('Social', 95)))

# To create an empty dictionary

studentDictionary = dict()

# To iterate through tuple items and insert them to dictionary as key and value, student is the key, course is the value

for student,course in studentTuple:

    # if the student (key) already exists in the student dictionary append the course (value) to the student (key)

    if student in studentDictionary:
        studentDictionary[student].append(course)

    # if the student (key) does not exist in the student dictionary create a new key and add the course (value) to that student (key)
    else:
        studentDictionary[student] = [course]


print(studentDictionary)