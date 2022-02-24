a = 0
b = 1
f = 1
n = int(input("The No of Values to be Generated in a Fibonacci Series: "))
while b <= n:
    f = a+b
    a = b
    b = f
    print(a)
