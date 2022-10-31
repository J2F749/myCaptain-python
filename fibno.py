n = int(input("enter the fibnacci range ="))
a=0
b=1
Sum=0
count=1

for Num in range(0,n):
    print(a,end=" ")
    Sum = Sum + a
    Next = a + b
    a = b
    b = Next
print(Sum)    
