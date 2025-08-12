num = int(input("enter of digits in number: "))

num_str = str(num)
num_digits = len(num_str)
# calculate the number of digits in num
sum_of_powers = 0
temp_num = num
# calculate the sum of digits raised to the power of num_digits

while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers += digit ** num_digits
    temp_num //=10

# check if its an Armstrong number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong  nnumber.")
