class Employe:
    def __init__(self,name,employe_id,base_salary,review_performance):
        self.name=name
        self.employe_id=employe_id
        self.base_salary=base_salary
        self.review_performance=review_performance
    def calculate_monthly_salary(self):
        return(self.base_salary)    
    def display_info(self):
        return("The employe's name is "+self.name+", monthly salary "+str(self.base_salary)+" dollars, ID "+self.employe_id+", and performance "+str(self.review_performance)+" stars out of 5 ") 
class Manager(Employe):
     def __init__(self,name,employe_id,base_salary,bonus_percentage,review_performance):
        super().__init__(name,employe_id,base_salary,review_performance)
        self.bonus_percentage=bonus_percentage
     def calculate_monthly_salary(self):
        return(self.base_salary+(self.bonus_percentage*self.base_salary))
     def display_info(self):
        if self.base_salary>=20000:
            self.review_performance+=1
        return("The manager's name is "+self.name+", monthly salary "+str(self.base_salary)+" dollars with a bonus percentage of "+str(100*self.bonus_percentage)+" percent ,ID "+self.employe_id+", and performance "+str(self.review_performance)+" stars out of 5  ")      
class Developer(Employe):
    def __init__(self,name,employe_id,base_salary,programming_language,review_performance):
        super().__init__(name,employe_id,base_salary,review_performance)
        self.programming_language=programming_language
    def display_info(self):
        if self.base_salary>=5000:
            self.review_performance+=0.5
        return("The developer's name is "+self.name+", monthly salary "+str(self.base_salary)+" dollars, emplye ID "+self.employe_id+", programming language "+self.programming_language+" and performance "+str(self.review_performance)+" stars out of 5  ") 
class Department:
    def __init__(self):
        self.employees=[]   
    def add(self,employe):
        self.employees.append(employe)
    def calculate_total_paychecks(self):
        t=0
        for i in range(len(self.employees)):
            t+=self.employees[i].base_salary
        return(t)
    def display_all_info(self):
        for i in range(len(self.employees)):
            print(self.employees[i].calculate_monthly_salary())
            print(self.employees[i].display_info())    
employe=Employe("John","John123",5000,4)
manager=Manager("Bob","Bob423",30000,0.1,3.5)
developer=Developer("Chris","Chris872",10000,"python",2)
employees=Department()
employees.add(employe)
employees.add(manager)
employees.add(developer)
print(employees.calculate_total_paychecks())
employees.display_all_info()


        
