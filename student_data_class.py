from dataclasses import dataclass

@dataclass

class Student:  # creating student object
    # def __init__(self, name, school_id, gpa): #adding additional data to student
        # self.name = name    # data in student object
        # self.school_id = school_id
        # self.gpa = gpa
         name: str
         school_id: str
         gpa: float

         def __str__(self): # this method is going to return a string version of object created
            return f'Student name: {self.name}, ID: {self.school_id}, GPA: {self.gpa} '
def main():
    chris = Student("Chris", "hsgdhg", 3.2) #student object saved to variable and printed out
    print(chris.name)
    print(chris.school_id)
    print(chris)

    jessie = Student("Jessie", "uiyiuy", 3.5)
    print(jessie)

main() #calling main method

