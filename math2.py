def sum(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    return(a/b)

n1=int(input("Please enter a number:"))
n2=int(input("Please enter the second number:"))

choice = input("Enter a for addition, s for subtraction, m for multiplication ,d for division:")

if choice=="a":
    print(sum(n1,n2))

elif choice=="s":
    print(sub(n1,n2))

elif choice=="m":
    print(mul(n1,n2))

elif choice=="d":
    print(div(n1,n2))

else:
    print("Wrong Option")