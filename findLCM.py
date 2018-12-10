#this line stores the first number in the variable a
a=int(input("Enter the first number: "))
#this line stores the second number in the variable b
b=int(input("Enter the second number: "))
#this line checks whether a is greater than b or not. If a is greater than b, then the value of a is stored in min1
if(a>b):
    min1=a
else:
#If a is not greater than b, then the value of b is stored in min1
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print("LCM is:",min1)
        #if the if condition is true then the LCM will be printed and the while loop will break
        break
    min1=min1+1
