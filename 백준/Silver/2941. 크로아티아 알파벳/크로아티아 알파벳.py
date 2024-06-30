word = input()
ABC = ['c=', 'c-', 'dz=', 'd-', 'd-', 'lj', 'nj', 's=', 'z=']

for i in ABC:
    word = word.replace(i, 'X')

print(len(word))