# declare list A
A = [10,20,30,40,50]
B = []
size = len(A)
B = [0] * size
B[0] = (A[0] + A[1])
#loop through last index
for i in range(1,size-1):
    # sum of its neighbors and itself and assign to new list B
    B[i] = A[i - 1] + A[i] + A[i + 1]

lastIndex = size - 1
#update last index outside the loop
B[lastIndex] = A[lastIndex] + A[lastIndex -1]
print(B)




