# checker = int(input())

# if checker % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

total = 0
number = int(input())

for i in range(1, number):
    if i % 2 == 0:
        total += i
print(total)

        