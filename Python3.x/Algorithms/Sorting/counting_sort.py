def counting_sort(a):
	n = len(a)
	k = max(a)
	b = []
	c = []
	for i in range(0, k + 1):
		c.append(0)
	for i in range(0, n):
		b.append(0)
	for j in range(0, n):
		c[a[j]] += 1
	for i in range(1, k + 1):
		c[i] += c[i - 1]
	for j in reversed(range(n)):
		b[c[a[j]]-1] = a[j]
		c[a[j]] -= 1
	return b
arr = [2, 0, 1, 2, 3, 1, 4, 3]
print("Before Sorting:", arr)
print("After Sorting:", counting_sort(arr))
