'''Given the number of the month, write a program to print the name of the month.
Input
The input will be a single line containing a integer N
Output
If the given number of the month is 1, print "January".
If the given number of the month is 2, print "February".
If the given number of the month is 3, print "March".
If the given number of the month is 4, print "April".
If the given number of the month is 5, print "May".
If the given number of the month is 6, print "June".
If the given number of the month is 7, print "July".
If the given number of the month is 8, print "August".
If the given number of the month is 9, print "September".
If the given number of the month is 10, print "October".
If the given number of the month is 11, print "November".
If the given number of the month is 12, print "December".
If the given number of the month is less than 1 or greater than 12, print "Invalid Month Number".
Explanation
For example, if the given number of month is 4, the output should be "April".
Similarly, if the given number of month is 13, the output should be "Invalid Month Number".'''




n=int(input())

if n==1:
    print("January")
elif n==2:
    print("February")
elif n==3:
    print("March")
elif n==4:
    print("April")
elif n==5:
    print("May")
elif n==6:
    print("June")
elif n==7:
    print("July")
elif n==8:
    print("August")
elif n==9:
    print("September")
elif n==10:
    print("October")
elif n==11:
    print("November")
elif n==12:
    print("December")
else:
    print("Invalid Month Number")