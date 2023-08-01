# Define the class of Person (the cookie cutter)
class Student:
    def __init__(self, firstName, lastName, course):
        self.firstname = firstName
        self.lastname = lastName
        self.Course = course
# Define the object of a person (the cookie)
Person0 = Student("Belinda", "Willis", "COMP642")
Person1 = Student("Cassie", "Lieu", "COMP639")
Person2 = Student("Sarah", "Lind", "ACC201")
# Create a list of my students
myStudents = []
myStudents.append(Person0)
myStudents.append(Person1)

# Define a method to add a new person to myStudents list.
myStudents.insert(1, Person2)

# Print the length of the myStudents list
print(len(myStudents))

# Define a method to remove a person from myStudents list.
myStudents.pop(1)

# Print the length of the myStudents list
print(len(myStudents))

# # Define the method to print the list of students
# def print_students(myStudents):


# # Print the list of students
# print("My students are:" + myStudents)