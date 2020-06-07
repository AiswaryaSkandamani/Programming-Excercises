#You are given with a number "N", find its cube.Allow negative numbers
c = 0
while c != 1:
    try:
        n = input()
        number = int(n)
        def cube(n):
            return pow(n,3)
    except ValueError:
        print("only int obj")
        break
    #if (number <= 0):
        #print('Negative numbers not allowed')
        c = 1
    else:
        output = cube(number)
        print(output)
        c = 1
    
