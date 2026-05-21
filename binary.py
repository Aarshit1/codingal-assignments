decimal=int(input("enter a decimal number : "))
binary=""

while decimal>0:
    rem=decimal%2
    binary=str(rem)+binary
    decimal=decimal//2

print("binary : ",binary)