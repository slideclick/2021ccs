s='()[]{'
stack=[]
map={'(':')','[':']','{':'}'}
def main(exp):
	result = False
	length= len(exp)
	i = 0
	while i < length:		
		c= exp[i]
		stack.append(c)
		if i+1 < length:
			i=i+1   
		else: 
			return print(False)
		secondc=exp[i]
		# if secondc not in map.keys:
		if secondc == map[c] :
			stack.pop()
		else:
			stack.append(secondc)
		i=i+1
	print(len(stack)==0)
if __name__ == '__main__':
	exp=input('give me string: ')
	main(exp)
	exit(0)



