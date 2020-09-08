'''     QUESTION:

UHD movies:

Dhinesh has a Hard disk and he has n movies in that hard disk. Each movie is of different file size in GB. He wants to know the size of Ultra High Definition (UHD) movies. 
UHD movie is the highest size movie in the hard disk. There is at least one UHD movie in the hard disk. Help him find the size of the UHD movie.

Input Format : The first line contains a single integer n--the number movies in that hard disk.
The second line contains n integers g1,g2,g3......gn where gi is the size of the i-th movie.

Input Constraints : 1<=n<=10^7
-10^7<=gi<=10^7

Output Format : Print a single integer denoting the size of the UHD movie.

Sample Input :
2
-1 1

Sample Output :
1








HINTS:

1 - The more the size is, more the definition is.

2 - You have to find the maximum element of the array.

3 - Initialize the answer with the smallest possible value so that the least element in the list is greater than that number always.

'''





























































# ANSWER:

n = int(input())
a = list(map(int, input().split()))
print(max(a))
