'''You are given a number ‘n’. You have to tell whether a number is great or not.
A great number is a number whose sum of digits let (m) and product of digits let(j) when summed together gives the number back

Sample Input :
59
Sample Output :
Great
'''
sum = 0
prd = 1
def mydigitfn(num,sum,prd):
    for x in range(length):
        sum = sum + int(num[x])
        prd = prd * int(num[x])
    return sum + prd
try:
    n = input()
    length = len(n)
    num = str(n)
    result = mydigitfn(num,sum,prd)
    if(result == int(num)):
        print("Great")
    else:
        print("no")
except ValueError:
        print("give only int object type")
        


