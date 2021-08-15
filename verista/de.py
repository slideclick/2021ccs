import sys
x = input("Name: ")
for line in sys.stdin: print(line)

with open('ch.txt',encoding='utf-8') as f:
	for ln in f:
		print(ln)