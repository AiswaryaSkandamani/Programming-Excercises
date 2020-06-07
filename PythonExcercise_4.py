#Greatest of two numbers
try:
    a , b = map(int,input().split())
    if a>b:
        print(b)
    else:
        print(a)
except ValueError:
    print("Enter only int objects")
