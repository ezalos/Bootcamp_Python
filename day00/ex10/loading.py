import sys
from time import sleep

listy = range(1000)
ret = 0

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def ft_progress(listy):
	total = len(listy);
	unit = int(total / 20);
	for i in listy:
		print("ETA: " + str(truncate((total * 0.01) - (i * 0.01), 2)) + "s ",
		"[ " if i < (total // 10) else "[", str(((i * 100)// total)) + '%' + ']' +
		'[' + (i // unit) * '=' + '>' + ((total - i - 1) // unit) * ' ' + '] ' +
		str(i) + '/' + str(total) +
		" | elapsed time " + str(truncate(i * 0.01, 2)) + "s  ",
		end="\r")
		yield i

for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print("---")
print(ret)
