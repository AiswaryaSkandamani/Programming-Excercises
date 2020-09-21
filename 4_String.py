'''
Given a day, print 'yes' if it is a holiday otherwise print'no'.Assume that weekend days are holidays
Sample Testcase :
INPUT
saturday
OUTPUT
yes
INPUT
monday
OUTPUT
no
'''
try:
    a = {'monday':'no','sunday':'yes','tuesday':'no','saturday':'yes','wednesday':'no','thursday':'no','friday':'no'}
    x = input().lower()
    print(a[x])
except:
    print("Error")
