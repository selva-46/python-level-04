print("sum of n Number")
print("---------------")
start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
print("**Result**")
for i in range(start, end + 1):
    print("", i)
total =sum(range(start, end + 1))
print("sum of value is:",total)
