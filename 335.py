a = int(input())
b = int(input())

for x in range(1, b + 1):
	if(x * x <= b and x * x >= a):
		print(x * x, end = ' ')
