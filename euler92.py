def calc_squr(n):
	result = 0
	for c  in str(n):
		result += int(c)**2
	return result

def classify(n):
	while not n == 89 and not n == 1:
		n = calc_squr(n)
	return n

table = dict()
for n in range(567,0,-1):
	table[n] = classify(n)
count = 0
for n in range(2,10000000):
	count += 1 if table[calc_squr(n)] == 89 else 0
print count