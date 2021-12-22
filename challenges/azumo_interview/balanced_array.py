n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

lhs = sum(a[:len(a)//2])
rhs = sum(a[len(a)//2:])

print(abs(lhs-rhs))