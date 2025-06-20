class Person:
    def __init__(self,name,number):
        self.name = name
        self.number = number

class Student(Person):
    

    def __init__(self,name,number,gpa):
        super().__init__(name,number)
        self.gpa = gpa
        self.classes = []
        def setGpa(self,gpa):
            return self.__gpa

    def enrollCourse(self,course):
        self.classes.append(course)

    def __str__(self):
        return "\n이름="+self.name+"\n주민번호="+self.number+\
               "\n수강과목="+str(self.classes)+"\n평점="+str(self.gpa)

class Teacher(Person):
    def __init__(self,name,number):
        super().__init__(name,number)
        self.courses = []
        self.salary = 3000000

    def assignTeaching(self,course):
        self.courses.append(course)

    def __str__(self):
        return "\n이름="+self.name+"\n주민번호="+self.number+\
               "\n강의과목="+str(self.courses)+"\n월급="+str(self.salary)

hong = Student("홍길동","12345678",4.0)
hong.enrollCourse("자료구조")
print(hong)

kim = Teacher("김철수","123456790")
kim.assignTeaching("Python")
print(kim)

        
