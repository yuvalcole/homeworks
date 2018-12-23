counter = 0
while counter < 10:

    if counter == 5:
        print("This is iteration number: ", counter)
    else:
        print("Loop number:", counter)
    counter += 1

print("\n")

for x in range(0, 3):
    print("This is iteration", x, "of x")
for y in range(0, 3):
    print("This is iteration ", y, "of y")