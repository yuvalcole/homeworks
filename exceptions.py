try:
    num = input("Give me a number: ")
    num = int(num)
    num2 = input("Give me another number: ")
    num2 = int(num2)
    result = num / num2

except ValueError:
    print("Please give me a proper number")
except ZeroDivisionError:
    print("The second number can not be 0")
except:
    print("I don't know what the error was...")
else:
    print("Division result = ", result)