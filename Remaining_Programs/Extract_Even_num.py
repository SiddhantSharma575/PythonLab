# Python program to find the even numbers in a List.

list1 = [1, 2, 3, 4, 5, 6]

for num in list1:
    if num % 2 == 0:
        print(num)

# Take list Input from User
lst = []
n = int(input("Enter no of Elements : "))

for i in range(0, n):
    ele = int(input())

    lst.append(ele)

for num in lst:
    if num % 2 == 0:
        print(num)
