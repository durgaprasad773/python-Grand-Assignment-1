'''Given an amount, write a program to find a minimum number of currency notes of different denominations that sum to the given amount. Available note denominations are 1000, 500, 100, 50, 20, 5, 1.
Input
The input contains single integer N.
Output
The first line of output should contain the number of 1000 notes, print "1000:a"
The second line of output should contain the number of 500 notes, print "500:b"
The third line of output should contain the number of 100 notes, print "100:c".
The fourth line of output should contain the number of 50 notes, print "50:d".
The fifth line of output should contain the number of 20 notes., print "20:e".
The sixth line of output should contain the number of 5 notes, print "5:f".
The seventh line of output should contain the number of 1 notes, print
"1:g".
In place of (a, b, c, d, e, f, g), print the count of corresponding notes.

Explanation
For example, if the given amount is 8593, in this problem you have to give the minimum number of notes that sum up to the given amount. Since we only have notes with denomination 1000, 500, 100, 50, 20, 5 and 1, we can only use these notes.
Number of 1000 notes Rightarrow 1theta*theta*theta * 8 = 8theta*theta*theta
Number of 500 notes 5theta*theta * 1 = 5theta*theta
Number of 100 notes 1theta*theta*theta =
Number of 50 notes 5theta * 1 = 5theta
Number of 20 notes 2theta * 2 = 4theta
Number of 5 notes 5 x 0 =
Number of 1 notes 1 * 3 = 3
Total 8593
So the output should be
1000:8
500:1
100:0
50:1
20:2
5:0
1:3
'''



a=int(input())

thousands = a // 1000
remaine_thousands = a % 1000
print("1000:"+str(thousands))

five_hundred = remaine_thousands // 500
remaine_five_hundred = remaine_thousands % 500
print("500:"+str(five_hundred))

hundred = remaine_five_hundred // 100
remaine_hundred = remaine_five_hundred % 100
print("100:"+str(hundred))

fifty = remaine_hundred // 50
remaine_fifty = remaine_hundred % 50
print("50:"+str(fifty))

twenty = remaine_fifty // 20
reamine_twenty = remaine_fifty % 20
print("20:"+str(twenty))

five = reamine_twenty // 5
remaine_five = reamine_twenty % 5
print("5:"+str(five))

print("1:"+str(remaine_five))
