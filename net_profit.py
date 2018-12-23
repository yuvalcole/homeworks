
try:
    gross_profit = float(input("Please enter gross salary: "))
    while True:
        kids = int(input("Please enter the number of kids: "))
        if kids > 0:
            break
        else:
            print("Please enter a proper number of children")
except ValueError:
    print("Please give a proper numbers")
except:
    print("Please check input")
else:

    if gross_profit < 1000:
        tax = 0.1
    elif gross_profit < 2000:
        tax = 0.12
    elif gross_profit < 4000:
        tax = 0.14
    else:
        tax = 0.18

    if gross_profit < 2000:
        tax -= 0.01 * kids
    else:
        tax -= 0.005 * kids

    if tax > 0:
        net_profit = gross_profit * (1 - tax)
    else:
        net_profit = gross_profit
    print("The net profit is ", net_profit)
