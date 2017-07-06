class Employee:

    def setName(self, name):
        self.name = name

    def setEmail(self, email):
        self.email = email
    def setSalary(self,salary):
        self.salary = salary

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email
    def getSalary(self):
        return self.salary


name = str(input("Enter Your Name : "))
email = str(input("Enter Your Email : "))
salary = int(input("Enter Your Salary : "))

emp = Employee()
emp.setEmail(email)
emp.setName(name)
emp.setSalary(salary)

print('\n'*5)
print('Employee Name : ', emp.getName())
print('Employee Email : ',emp.getEmail())
print('Employee Salary : ', emp.getSalary())