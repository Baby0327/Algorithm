t1, f1, s1, p1, c1 = map(int, input().split())
t2, f2, s2, p2, c2 = map(int, input().split())
result1 = t1*6 + f1*3 + s1*2 + p1*1 + c1*2
result2 = t2*6 + f2*3 + s2*2 + p2*1 + c2*2
print(result1, result2)