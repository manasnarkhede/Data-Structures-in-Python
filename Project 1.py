Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> r = float(input("Input the radius of the circle: "))
Input the radius of the circle: 15
>>> area = math.pi*r*r
>>> print("The area of the circle: %.2f" %area)
The area of the circle: 706.86
>>> 
>>> 
>>> #Program to accept a filename from the user and print the extension of that
>>> filename=input("Enter a filename: ")
Enter a filename: Area.py
>>> index=0
>>> for i in range(len(filename)):
	if filename[i]==".":
		index=i

	
>>> print(filename[index+1: ])
py
>>> 