
#take user input for days
numberDays = int(input("Enter number of days:"))
#initialize variable
salary = 1
totalPay = 0.0
#loop through number of days
for day in range(numberDays):
    #multiply salary to double
    salary = salary * 2
    #convert penny to dollar
    dollar = salary/100.00
    #calculate total in dallar
    totalPay = totalPay + dollar
    print("Day" , str(day+1), "Salary :$", dollar)

print("Total Pay: $",totalPay)