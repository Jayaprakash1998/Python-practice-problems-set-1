'''     QUESTION:

Katie and spells:

Katie is a little girl and she is from a witch family. Nobody in her school knows that she is a witch. She always carries some spells in her bag to make things easy. 
Like calculating maths, she uses a spell. If she is hungry then she uses a spell to make whatever food she wants. But she doesn’t know the danger value of the spell. 
If there are 2 spells of 2ml and 2ml quantity then the danger value is 4. She wants to calculate the danger value for n spells. Can you help Katie by writing a program?

Input Format : The first line contains a single integer n--the total number of spells Katie has.
The second line contains n integers denoting the quantity of each spell q1,q2......qn.

Input Constraints : 1<=n<=1000
1<=qi<=100

Output Format : Print a single integer denoting the danger value of n spells.

Sample Input :
3
2 2 1

Sample Output :
4







HINTS:

1 - Repeated addition is called multiplication.

2 - You have to find the product of all the elements of the array.

3 - Don't forget to initialize the answer variable with 1 rather than 0.

'''





























































# ANSWER:

n = int(input())
list = list(map(int,input().split()))

p = 1
for i in range(n):
  p = p * list[i]

print(p)  
