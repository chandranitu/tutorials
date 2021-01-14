class Employee:
   'Base class for all emp'
   empCount = 0
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)
   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

# creating object

emp1 = Employee("chandra", 25000)
emp2 = Employee("nitu", 51000)
emp1.displayEmployee()
emp2.displayEmployee()

hasattr(emp1, 'salary')    # Returns true if 'salary' attribute exists
getattr(emp1, 'salary')    # Returns value of 'salary' attribute
setattr(emp1, 'salary', 27000) # Set attribute 'salary' at 27000
delattr(emp1, 'salary')    # Delete attribute 'salary'
