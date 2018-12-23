num = int(input("Please input your number: "))
temp = num
b = 0
while num > 0:
    b = 10*b + (num % 10)
    num= num // 10
    if temp==b:
        print(temp, "is a palindrome")
    else:
        print(temp, "isn't a palindrome")
        break