'''
You are given a task to tell whether the number is pure or not. A pure number is a number whose sum of digits is multiple of 3.

O(1) time and O(1) space

Input Description:
You are given a number n.

Output Description:
Print yes if it is pure else not

Sample Input :
13
Sample Output :
not
'''

try:
    n = int(input())
    a = str(n)
    l = len(a)
    sum = 0
    for i in range(0,l):
        sum = sum+int(a[i])
    if sum%3 == 0:
        print("yes")
    else:
        print("not")
except:
    print("error")
