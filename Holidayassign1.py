L = [45,78,89,34,12,11,23,43,23,45,89,98,76,54,32,21]
count = 0
for i in L:
    count+=i

average=count/len(L)

print("Sum is:", count)
print("Average is:",average)
print("Min is: ", min(L))
print("Max is: ", max(L))

L = [45,78,89,34,12,11,23,43,23,45,89,98,76,54,32,21]

out = []
 
for num in L:
 
    if num % 2 == 0:
        out.append(num)
 
print("The even numbers in the list are: ", out)



