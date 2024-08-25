'''Given three sides of the triangle(a, b, c) as input. Write a program to determine whether the triangle is Equilateral, Isosceles or Scalene.
Input
The first line of input will contain an integer A.
The second line of input will contain an integer B.
The third line of input will contain an integer C.
Output
If the given sides A, B and C are equal, print "Equilateral".
In the given sides any of two sides are equal print "Isosceles".
If the given sides A, B, C are not equal to each other, print "Scalene".
Explanation
For example, if the given sides are 4, 4, 4 the output should be "Equilateral". Similarly, if the given sides are 3, 2, 3 the output should be "Isosceles"'''


a=int(input())
b=int(input())
c=int(input())

if a==b==c:
    print("Equilateral")
elif a==b or a==c or b==a or b==c or c==a or c==b:
    print("Isosceles")
else:
    print("Scalene")