'''Abhinav and Anjali are playing a game called Rock-Paper- Scissors. It's a hand game usually played between two people. In this game, they both show their hands in one of three ways: Rock, Paper, or Scissors.
For example,
If Abhinav shows Rock and Anjali shows Scissors, Abhinav wins because Rock blunts Scissors.
If Anjali shows Paper and Abhinav shows Scissors, Abhinav wins because Scissors cut Paper.
If Abhinav shows Paper and Anjali shows Rock, Abhinav wins because Paper wraps Rock.
If both players show the same thing, it's a tie. For example, if Abhinav and Anjali both show Rock, it's a tie.
Write a program that reads two strings representing what Abhinav and Anjali showed and prints the winner of the game based on the shapes the players choose.
Input
The first line of input contains a string representing the shape chosen by Abhinav.
The second line of input contains a string representing the shape chosen by Anjali.
Output
The output should be a single line containing a string. Abhinav Wins should be printed if Abhinav wins the game or Anjali Wins should be printed if Anjali wins the game. Otherwise, Tie should be printed.
Explanation
For example,
If Abhinav shows Rock and Anjali shows Paper, Anjali wins because Paper wraps Rock.
So, the output should be Anjali Wins.
For example,
If Abhinav shows Rock and Anjali shows Scissors, Abhinav wins because Rock blunts Scissors.
So, the output should be Abhinav Wins.
For example,
If Abhinav shows Paper and Anjali shows Paper, it's a tie.
As both players show the same thing, it's a tie.
So, the output should be Tie.
'''



abhinav = input()
anjali = input()

if abhinav=="Rock" and anjali=="Paper":
    print("Anjali Wins")
elif abhinav=="Scissors" and anjali == "Rock":
    print("Anjali Wins")
elif abhinav =="Rock" and anjali=="Scissors":
    print("Abhinav Wins")
elif abhinav =="Scissors" and anjali=="Paper":
    print("Abhinav Wins")
    
elif abhinav == anjali:
    print("Tie")