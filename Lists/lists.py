numbers = [1, 2, 2, 3, 4, 5, 6]
numbers.append(8)
numbers.insert(4, 5)
print(numbers)

Max = sum(numbers)
print(Max)

print(any([0, 1]))
print(all([0, 1]))

print("Count:", numbers.count(2))
print("idex:", numbers.index(5))
print(7 in numbers)
