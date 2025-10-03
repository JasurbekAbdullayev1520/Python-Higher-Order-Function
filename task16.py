
data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

result = list(filter(lambda d: isinstance(d, str) and len(d) > 5, data))

print(result)

