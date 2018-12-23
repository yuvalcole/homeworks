sMax = 0
while True:
    summing = 0
    num = input("Give me a number: ")
    try:
        num = int(num)

    except ValueError:
        print("You have not entered a proper number.")
        break

    summing = summing + num

    if summing > sMax:
        sMax = summing + sMax

    print("The Biggest current sum is: ", sMax)