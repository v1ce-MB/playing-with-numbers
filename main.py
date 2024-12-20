number= input("Enter the number to check:")

def checkpalindrome(n):
    reversed = (n[::-1])
    if n == reversed:
        print("this is a palindrome")
    else :
        print("this is not a palindrome")

checkpalindrome(number)
