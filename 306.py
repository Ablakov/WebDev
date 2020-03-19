def mini(a, b):
	if (a > b):
		return b
	elif (a < b):
		return a
	else:
		return a

s = input()

res = [int(i) for i in s.split()]

z = int(res[0])

for i in range (1, len(res)):
	x = mini(res[i - 1], res[i])

	if(x < z):
		z = x

print(z)