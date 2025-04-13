# Request three integers from the user
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter one more number: "))

# Print the sum of all, num1 - num2, num3 x num1, sum of all divided by num3
sum = num1+num2+num3
subt = num1-num2
mult = num3*num1
sum2 = round((sum/num3),2)  # I'm choosing to keep this as a float
print(f"{sum}\n{subt}\n{mult}\n{sum2}")