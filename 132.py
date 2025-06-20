class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary  = salary

    def getSalary(self):
        return self.salary

class Manager(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus

    def getSalary(self):
        salary = super().getSalary()
        return salary + self.bonus

    def __repr__(self):
        return self.name+str(self.salary)+str(self.bonus)

kim = Manager("김철수",20000000,10000000)
print(kim)
    
