#You are given Two Numbers, A and B. If C = A + B. Find C.Round off the output to a single decimal place.
'''
Sample Input :
1
1
Sample Output :
2
'''
def sum(a,b):
    try:
        #c = a + b
        c = float(a)+float(b)
        print(round(c,1))
    except ValueError:
        print("Enter only numeric values")       
a,b = (input(),input())
        #a = input()
        #b = input()
sum(a,b)



