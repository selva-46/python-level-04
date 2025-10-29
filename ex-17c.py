print("sum of n number in difference")
print("-----------------------------")
start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
diff=int(input("Enter the difference:"))
print("//Result\\")
print("series")
count=0
sum=0
for i in range (start,end,diff):
    print("+",+i)
    sum=sum+i;
    count=diff;
print("sum value:",sum)
print("count value:",count)
