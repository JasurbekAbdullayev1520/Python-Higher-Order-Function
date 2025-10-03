sentence = "Functional programming in Python is very powerful and elegant"


words = sentence.split()
longest = sorted(words, key=len, reverse=True)[:3]

print(longest)  
