multiply = lambda x: x * 2
print(multiply(5))  # Output: 10


check = lambda x: x in ["apple", "banana", "orange"]
print(check("banana"))  # Output: True
print(check("grape"))   # Output: False


prices = ["#10", "#20", "#30", "#40", "#50"]
print(list(map(float, map(lambda price: price.replace("#", ""), prices))))  # Output: [10.0, 20.0, 30.0, 40.0, 50.0]

k = "#10"
print(k.replace("#", ""))  # Output: 10