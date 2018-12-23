max = 0
while True:
    sum = 0
    num = input("Type a number: ")
    try:
        num = int(num)

    except ValueError:
        print("Please enter a valid number.")
        break

    sum = sum + num

    if sum > max:
        max = sum + max
        print("The Biggest current sum is: ", max)
    else:
        print("The number you inputed is smaller than the older sum, so this is the last sum for the program", max)
        break