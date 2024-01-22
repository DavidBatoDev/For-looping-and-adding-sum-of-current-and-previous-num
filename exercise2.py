# create a for loop with 10 iterations
# each value of the iteration adds the value of the previous iteration value
print('Printing current and previous number sum in a range(10)')
previous_number = 0
for i in range(10):
    sum = i + previous_number
    print(f'Current Number is {i} Previous Number {previous_number} Sum: {sum}')
    # change the previous number after printing the result:
    previous_number = i
    