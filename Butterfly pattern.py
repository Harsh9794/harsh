#Using for loop

n=int(input("Enter a number"))
for i in range(1,n+1):
    gap = 2 * n - 2 * i
    for j in range(1,2*n+1):
        if j<=i:
            print("*",end=" ")
        elif i<j<=i+gap:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
for i in range(n,0,-1):
    gap = 2 * n - 2 * i
    for j in range(1,2*n+1):
        if j<=i:
            print("*",end=" ")
        elif i<j<=i+gap:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

#calling a function

n=int(input('Enter a number: '))
def butter_fly():
    gap = 2 * n - 2 * i
    for j in range(1, 2 * n + 1):
        if j <= i:
            print("*", end=" ")
        elif i < j <= i + gap:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
for i in range(1,n+1):
    butter_fly()
for i in range(n,0,-1):
    butter_fly()