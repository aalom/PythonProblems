#this lines stores an integer number in the variable n
n=int(input("Enter number:"))
temp=n
rev=0
#this loop continues while the value of n is greater than 0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    #if temp is equal to rev this line is printed
    print("The number is a palindrome!")
else:
    #if temp is not equal to rev this line is printed
    print("The number isn't a palindrome!")
