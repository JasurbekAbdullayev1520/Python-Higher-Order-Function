
nums = list(range(1, 21))
r = list(filter(lambda n: n % 2 == 0 , nums))
result = list(map(lambda i: i ** 2, r))
print( result)