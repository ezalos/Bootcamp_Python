import math
max_size = 10

def setup(tab, case):
	for i in range(len(tab)):
		tab[i] = 0
	i = 0
	while case > 0:
		tab[i] = case % n
		case = int(case / n)
		i = i + 1
	return tab

def check_it(tab, check):
	for i in range(len(tab)):
		if check[i] != tab[i]:
			return 0
	# print("VICTORY")
	return 1

def count(tab):
	check = [0] * len(tab)
	sum = 0
	for elem in tab:
		sum = sum + elem
	if n != sum:
		return 0
	# print(tab, n, sum)
	for i in range(len(check)):
		for j in range(len(tab)):
			if tab[j] == i:
				check[i] = check[i] + 1
	# print("~~~~~~~~~~~~~~~~~")
	ans = check_it(tab, check)

	if ans:
		print("         ", top)
		print("TAB IS   ", tab)
		print("")
		print("")
		# print("CHECK IS ", check)
	return(ans)

speed = 1
n = 0
for n in (range(1, max_size + 1)):
	tab = [0] * n
	top = []
	for i in range(0, n):
		top.append(i)
	possibilities = pow(n, n)
	for i in range(0, possibilities):
		setup(tab, i)
		if speed and n <= 4:
			if count(tab):
				print("\tWas try ", i, "/", possibilities)
		else:
			if count(tab):
				print(i)
				break
