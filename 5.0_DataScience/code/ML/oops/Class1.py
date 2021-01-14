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
print ("Total Employee %d" % Employee.empCount)

del emp1.salary
emp1.salary = 17000

emp1.name = 'name'
----------------------

class Test(object):
    def __init__(self):
        self.__a = 'a'
        self._b = 'b'


t1 = Test()
>>> t1._b
'b'

t1.__a    # error
t1._Test__a


----------------







