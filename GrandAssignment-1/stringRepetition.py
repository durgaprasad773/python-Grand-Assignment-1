'''Write a program to print the given input word N times in a single line
separated by space.
Input
The first line of the input containing a string. The second line of the input containing a integer (N).
Output
The output should be a single line containing the word printed N times separated by space.
Explanation
For example, if the given input is "pen", and N is 2 then you should print "pen pen" separated by space.'''

s=input()
n=int(input())
print((s+" ")*n)
