a  = int(input('enter a first number: '))
b = int(input('enter a second number: '))
c = int(input('enter a third number: '))

if a > b and a > c:
    print (f'{a} is greater number')
elif b > a and b > c:
    print (f'{b} is greater number')
else:
    print (f'{c} is greater number')
    