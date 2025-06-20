class Person:
    def __init__(self, name,number):
        self.name = name
        self.number = number

class Student(Person):
    def __init__(self,name,number):
        super().__init__(name,number)
        self.classes = []
        self.gpa = 0

    def setClasses(self, course):
        self.classes.append(course)
        

    def __str__(self):
        return self.name+self.number+str(self.classes)+str(self.gpa)

class Teacher(Person):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.courses = []
        self.salary = 3000000

    def setCourses(self, course):
        self.courses.append(course)

    def __str__(self):
        return self.name+self.number+str(self.courses)+str(self.salary)

hong = Student('홍길동','12345678')
hong.setClasses('자료구조')
print(hong)

kim = Teacher('김철수','123456790')
kim.setCourses('Python')
print(kim)
