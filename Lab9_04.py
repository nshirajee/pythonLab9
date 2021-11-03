
sum = 0
userInput = int(input("Enter an integer value :"))
#loop through number starting 1
for i in range(1,userInput+1):
    #add to sum
    sum = sum + i
#print sum
print(sum)

print("Part b")
for j in range(1,userInput+1):
   total = 0
   #inner loop to calculate consecutive sum
   for i in range(1,j+1):
       total = total + i
   print(total)
