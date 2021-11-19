
# Write a Python program to find all the values in a list are greater than a given number.


lst = []
n = int(input("Enter no of Elements : "))

for i in range(0, n):
    ele = int(input())

    lst.append(ele)

k = int(input("Enter value of K : "))

for num in lst:
    if num > k:
        print(num)
