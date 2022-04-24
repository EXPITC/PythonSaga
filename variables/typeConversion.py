from datetime import date
birth_year = input('Birth year: ') #return as string
# usually I just type date.today().strftime("%Y") on age but I learn how to clean code and easy read
years_now = int(date.today().strftime('%Y')) #return string we need to conversion to int
age = years_now - int(birth_year)
print(birth_year, ':',type(birth_year))
print('Your age is :',age,type(age))


# this is was comment
"""
at python conversion more easy than golang but you know golang is my favorite animal then snake
int()
float()
bool() 
"""
