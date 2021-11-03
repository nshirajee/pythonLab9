#function to calculate Fibonacci sequence
def fibonaccisequence(number):
    #Initialize variable
    #second seq starts with 1
    firstseq = 0
    secondseq = 1
    #loop through number of sequence parameter
    for x in range(number):
        #only print second seq, first time it'll print 1, after that it'll print bothseq variable
        print(secondseq)
        #sum of first abd second seq and store in variable
        bothSeq = firstseq + secondseq
        # switch first seq to second seq
        firstseq = secondseq
        # set second seq to variable which is first + second seq
        secondseq = bothSeq

#
userInput = int(input("Enter an Integer:"))
fibonaccisequence(userInput)
