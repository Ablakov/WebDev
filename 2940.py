d = 109
v = int(input())
t = int(input())
y = int()

y = d+(v * t % d)

print(y%d)