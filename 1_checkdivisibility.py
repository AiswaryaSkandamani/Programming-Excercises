'''
Given a number N, print yes if the number is a multiple of 7 else print no.
Sample Testcase :
INPUT
49
OUTPUT
yes
'''
try:
    n = int(input())
    if n % 7 == 0:
        print("yes")
    else:
        print("no")
except:
    print("Error")
    
