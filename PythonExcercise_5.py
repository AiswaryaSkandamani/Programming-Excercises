'''You are given with a number ‘n’. You have to count the pair of two numbers a and b such that sum of two numbers are equal to n.

 

Note:Both numbers lie in range 1<=a,b<n

Input Description:
You are given a number ‘n’

Output Description:
Print the number of pairs satisfying above condition

Sample Input :
5
Sample Output :
4



1 + 4
2 + 3
3 + 2
4 + 1
'''
i = 1
while(i):
    try:
        n = int(input())
        if n <= 0:
            print("Only  num value greater than 1")
            i = 0
            break
        count = 0
        for a in range(1,n):
            for b in range(1,n):
                c = a + b
                if  c== n:
                    count = count+1
                    #print("{0} + {1}".format(a,b))
        print(count)
        i = 0
    except ValueError:
        i =0
        print("ENter integer value alone")
        


