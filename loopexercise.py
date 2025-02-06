#Display all numbers between 0 to 1000 which are divisible by 11
#Hint : modulus operator % gives reminder

for x in range (0,1000):
    if (x % 11 == 0):
        print (x)
        
i =  0 
while i <= 1000:
    if ( i % 11 == 0):
        print (i)
    i += 11
        