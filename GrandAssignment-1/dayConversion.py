'''Given a number of days (N) as input, write a program to convert N to years (Y), weeks (W), and days (D).
Input
The input will be a single line containing a positive integer (N).
Output
The output should be a single line containing years, weeks, days values separated by spaces.
Explanation
For example, if the given number of days (N) is 1329. 1329365*3+33*7+3 So the output is 3 years 33 weeks 3 days'''




a=int(input())

years = a // 365
remain_years = a % 365

weeks = remain_years // 7
remain_week = remain_years % 7

res = str(years) + " years " + str(weeks) + " weeks "+ str(remain_week) +" days"

print(res)