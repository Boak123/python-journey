def count_positive(numbers):
    counter = 0
    for i in numbers:
        if i > 0:
            counter += 1
    return counter
number = count_positive([1, -2, 3, 4, 8, 10])
print(number)