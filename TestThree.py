class Student():
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f"Name: {self.name}, Student ID: {self.student_id}"  
    
class Course():
    def __init__(self,course_name,students):
       self.course_name = course_name
       self.students = students

    def __str__(self):
       return f"Course Name: {self.course_name}, Students: {', '.join(str(student) for student in self.students)}"
   
    def add_student(self, student):
       self.students.append(student)
       print(f"Student added: {student}")

    def remove_student(self,student):
       if student in self.students:
           self.students.remove(student)
           print(f"Student Removed {student}")
       else:
           print("Student is not found in this course")

    def display_students(self):
        if not self.students:
            print("No students enrolled in this course.")

        else:
            print("Enrollled Student")
            for student in self.students:
                print(student)

        

# Example usage
course = Course("Python Programming", [])
student1 = Student("Alice", "S001")
student2 = Student("Bob", "S002")

course.add_student(student1)
course.add_student(student2)

course.display_students()   
course.remove_student(student1)
course.display_students()
course.remove_student(student1)  # Attempt to remove a student that is not enrolled
course.add_student(student1)  # Re-adding the student
course.display_students()  # Display students after re-adding
course.remove_student(student2)
course.display_students()  # Display students after removing the second student
course.remove_student(student2)  # Attempt to remove a student that is not enrolled
course.add_student(student2)  # Re-adding the second student
course.display_students()  # Display students after re-adding the second student
course.remove_student(student2)  # Remove the second student again
course.display_students()  # Display students after removing the second student again
course.remove_student(student1)  # Remove the first student again
course.display_students()  # Display students after removing the first student again
course.remove_student(student1)  # Attempt to remove a student that is not enrolled
course.display_students()  # Display students after attempting to remove a student that is not enrolled
