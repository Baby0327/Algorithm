"""
베스트셀러
"""

n = int(input())
books = {}

for i in range(n):
    title = input()
    books[title] = books.get(title, 0) + 1

sorting = sorted(list(books.items()), key=lambda x : (-x[1], x[0]))

print(sorting[0][0])