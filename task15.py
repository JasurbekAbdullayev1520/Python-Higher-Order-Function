votes = [
  {"option": "A", "votes": 123},
  {"option": "B", "votes": 145},
  {"option": "C", "votes": 97}
]
mx = max(votes, key=lambda v: v['votes'])
print(mx)