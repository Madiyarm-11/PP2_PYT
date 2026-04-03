names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

# enumerate()
for index, name in enumerate(names):
    print(index, name)

# zip()
for name, score in zip(names, scores):
    print(name, score)

# sorted()
print(sorted(scores))

# type conversion
num_str = "123"
num = int(num_str)
print(type(num))