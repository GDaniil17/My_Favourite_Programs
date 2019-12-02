from collections import deque as d
def ans(st):
	s = d()
	print(len(st))
	for i in st:
		if i == "(":
			s.append(1)
		elif i == "[":
			s.append(2)
		elif i == "{":
			s.append(3)
		elif i == ")" and s[-1] == 1:
				s.pop()
		elif i == "]" and s[-1] == 2:
				s.pop()
		elif i == "}" and s[-1] == 3:
				s.pop()
	if not s:
		print("Perfect")
	else:
		print("Ugly")
ans(input())
