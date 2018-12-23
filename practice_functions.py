import random


def a():
    total = 0
    for x in range(0, 10):
        num = random.random()
        print(num)
        total += num
    print("The sum is equal to", total)


def b(number, odd=True):
    check = number % 2 != 0
    if odd and check is True:
        print(number, "is odd")
    elif odd and check is False:
        print(number, "is even")
    elif not odd and check is True:
        print("Checking for even but is odd")
    else:
        print(number, "is even")


def c():
    iterations = random.randint(0, 100)
    rand_list = []
    for x in range(0, iterations):
        number = [random.randint(0, 9)]
        rand_list.extend(number)
    print("Random list is: ", rand_list)
    return rand_list


def d():
    largest_lst = c()
    largest_lst.sort()
    print("Largest value is", largest_lst[len(largest_lst)-1])


def e():
    sort_lst = c()
    sort_lst.sort()
    print("Sorted list is: ", sort_lst)


def f():
    lst = c()
    maximum = 0
    for a in range(0, len(lst)-1):
        if lst[a] > maximum:
            maximum = lst[a]
    print("Largest value is", maximum)


def exit():
    exit()
