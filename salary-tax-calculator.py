'''
Write a Python program to calculate City Tax (10%) and Net Salary for a given list of salaries. 
Display the results in a tabular format with Salary, City Tax, and Net Salary columns.
'''

salary=[1500,2000,1200,3200,3500,5000,1900]
print ('salary  City Tax    Net Salary')
for s in salary:
    CT = (s*10)/100
    NS = s - CT
    print (f' {s}     {CT}      {NS}')
    
