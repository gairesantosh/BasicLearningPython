#Write a Python program to print the multiplication table of a given number using a for loop.

n = int(input('enter a number: '))
for i in range (1, 10+1):
    total = (n * i)
    print(f"{n} x {i} =", total)