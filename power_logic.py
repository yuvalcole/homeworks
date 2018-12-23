num = int(input("Please input a number: "))
exponent = int(input("Please give the exponent: "))

base_number = num
multiple = 0
for y in range(0, num):
    multiple += base_number
base_number = multiple
print(num, "to the power of", exponent, "equals", base_number)
