class Salary:
    def _init_(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_Salary(self):
        return(self.pay*12)+self.bonus
class Employee:
    def _init_(self,name,age,pay,bonus):
        self.name = name
        self.age = age
        self.obj_Salary-Salary(pay,bonus)

    def total_Salary(self):
        return self.obj_Salary.annual_Salary()
    
emp = Employee('rama',30,3000,20)
print('Employee name' = emp.name)
print('Employee age'=emp.age)
print('Employee annual Salary'=emp.total_Salary())
