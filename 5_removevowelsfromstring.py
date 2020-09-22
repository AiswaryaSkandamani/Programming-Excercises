'''
Given a string S, print the reverse of the string after removing the vowels.If the resulting string is empty print '-1'.
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
codekata
OUTPUT
tkdc
'''

try:
    str = input()
    n = int(len(str))
    str1 = str[::-1]
    vow = ['a','e','i','o','u']
    for x in str1:
        if x in vow:
            str1 = str1.replace(x,"")
    if str1 == "":
        print("-1")
    else:
        print(str1)
except:
    print("Errr")

