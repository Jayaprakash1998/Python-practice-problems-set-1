'''  QUESTION:

Jack and Rose
Jack and Rose are going to a restaurant. Jack have lunch there every fourth day, and Rose has her lunch there every sixth day. 
How many days before Jack and Rose meet again for lunch at the same restaurant.

Input Format : The First line of input consists of two space separated Integers N and M.

Input Constraints : 1<=N<=10^7
1<=M<=10^7

Output Format : Single Integer denoting the number of days.

Sample Input :
608514155 771884537

Sample Output :
469702666790121235


HINTS:

1 - The problem has something to do with the factors of the two numbers.

2 - You have to find the LCM of the given two numbers in an efficient way.

3 - Since finding LCM takes large amount of computation, we can use the formula, LCM(a,b) * GCD(a,b) = a * b.

'''






































































# ANSWER

from math import *
a,b=map(int,input().split())
print((a*b)//gcd(a,b))


