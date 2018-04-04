#! /usr/bin/python
class PFgenerator:

	def __init__ (self, len, restricitions):
		self.__len = len
		self.__restricitons = restricitions

	def makeAttempt (self):
		import random
		attempt = []
		for x in range(self.__len):
			x = random.randint(0, 9) 
			while (x in self.__restricitons) or (x in attempt):
				x = random.randint(0, 9)
			attempt.append(x)	
		return tuple(attempt)

firstattempt = PFgenerator(4, (1, 2))
x = firstattempt.makeAttempt()
print (x)