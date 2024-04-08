class VECTOR:
	def __init__(self, maxsize):
		self.maxsize = maxsize
		self.vlist = ["X"]*maxsize
		self.tail = 0

	def push(self, data):
		print("Push", data)
		if (self.tail >= self.maxsize) or (self.tail <= self.maxsize // 2) : self.resize()
		self.vlist[self.tail] = data
		self.tail += 1

	def pop(self):
		print("Pop")
		if self.tail <= 0 : return print("Vector is empty")
		self.vlist.pop(self.tail)
		self.tail -= 1
		if (self.tail >= self.maxsize) or (self.tail <= self.maxsize // 2) : self.resize()

	def resize(self):
		print("Resizing: ")
		if (self.tail >= self.maxsize): 
			print("Too small of an array. Making it bigger... ")
			self.maxsize += self.maxsize // 2 + 1
			self.temp = self.vlist
			self.vlist = ["X"]*self.maxsize
			for x in range(len(self.temp)): self.vlist[x] = self.temp[x]
		elif (self.tail <= self.maxsize // 2): 
			print("Too big of an array. Making it smaller... ")
			self.maxsize -= (self.maxsize - self.tail) // 2
			self.temp = self.vlist
			self.vlist = ["X"]*self.maxsize
			for x in range(len(self.vlist)): self.vlist[x] = self.temp[x]

# Testing
vector = VECTOR(5)
vector.push(3)
vector.pop()
vector.pop()
print("tail: ", vector.tail)

for x in range(100):
	vector.push(x)
	

for x in range(102):
	vector.pop()

Output: 

Push 3
Resizing: 
Too big of an array. Making it smaller... 
Pop
Resizing: 
Too big of an array. Making it smaller... 
Pop
Vector is empty
tail:  0
Push 0
Resizing: 
Too big of an array. Making it smaller... 
Push 1
Resizing: 
Too small of an array. Making it bigger... 
Push 2
Resizing: 
Too small of an array. Making it bigger... 
Push 3
Push 4
Resizing: 
Too small of an array. Making it bigger... 
Push 5
Push 6
Push 7
Resizing: 
Too small of an array. Making it bigger... 
Push 8
Push 9
Push 10
Push 11
Resizing: 
Too small of an array. Making it bigger... 
Push 12
Push 13
Push 14
Push 15
Push 16
Push 17
Resizing: 
Too small of an array. Making it bigger... 
Push 18
Push 19
Push 20
Push 21
Push 22
Push 23
Push 24
Push 25
Push 26
Resizing: 
Too small of an array. Making it bigger... 
Push 27
Push 28
Push 29
Push 30
Push 31
Push 32
Push 33
Push 34
Push 35
Push 36
Push 37
Push 38
Push 39
Push 40
Resizing: 
Too small of an array. Making it bigger... 
Push 41
Push 42
Push 43
Push 44
Push 45
Push 46
Push 47
Push 48
Push 49
Push 50
Push 51
Push 52
Push 53
Push 54
Push 55
Push 56
Push 57
Push 58
Push 59
Push 60
Push 61
Resizing: 
Too small of an array. Making it bigger... 
Push 62
Push 63
Push 64
Push 65
Push 66
Push 67
Push 68
Push 69
Push 70
Push 71
Push 72
Push 73
Push 74
Push 75
Push 76
Push 77
Push 78
Push 79
Push 80
Push 81
Push 82
Push 83
Push 84
Push 85
Push 86
Push 87
Push 88
Push 89
Push 90
Push 91
Push 92
Resizing: 
Too small of an array. Making it bigger... 
Push 93
Push 94
Push 95
Push 96
Push 97
Push 98
Push 99
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Resizing: 
Too big of an array. Making it smaller... 
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Resizing: 
Too big of an array. Making it smaller... 
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Resizing: 
Too big of an array. Making it smaller... 
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Resizing: 
Too big of an array. Making it smaller... 
Pop
Pop
Pop
Pop
Pop
Pop
Pop
Resizing: 
Too big of an array. Making it smaller... 
Pop
Pop
Pop
Pop
Pop
Pop
Resizing: 
Too big of an array. Making it smaller... 
Pop
Pop
Pop
Pop
Resizing: 
Too big of an array. Making it smaller... 
Pop
Pop
Pop
Resizing: 
Too big of an array. Making it smaller... 
Pop
Pop
Resizing: 
Too big of an array. Making it smaller... 
Pop
Pop
Resizing: 
Too big of an array. Making it smaller... 
Pop
Resizing: 
Too big of an array. Making it smaller... 
Pop
Resizing: 
Too big of an array. Making it smaller... 
Pop
Resizing: 
Too big of an array. Making it smaller... 
Pop
Resizing: 
Too big of an array. Making it smaller... 
Pop
Resizing: 
Too big of an array. Making it smaller... 
Pop
Vector is empty
Pop
Vector is empty
