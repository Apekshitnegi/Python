class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000


lucky = Employee()
lucky.language = "JavaScript" # This is an instance attribute
print(lucky.language, lucky.salary)
 