def find_average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)
    return average

numbers = [1,2,3,4,5,6]
average = find_average(numbers)
print(f"The average is: {average}")
