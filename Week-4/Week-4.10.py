 Perfect Square After adding One

Given an integer N, check whether N the given number can be made a perfect square after adding 1 to it.

Input Format:

Single integer input.

Output Format:

Yes or No.

Example Input:

24

Output:

Yes

Example Input:

26

Output:

No

For example:

Input	Result

24	Yes





import math

n=int(input())

a=n+1

sr=int(math.sqrt(a))

if(sr*sr==a):

    print("Yes")

else:

    print("No")

