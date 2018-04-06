#! /usr/bin/python
class PFgenerator:

    def __init__(self, len=4, restrictions=(),
                 masterset={0, 1, 2, 3, 4, 5, 6, 7, 8, 9}):
        self.__len = len
        self.__restrictions = restrictions
        self.__masterset = masterset

    def makeAttempt(self):
        import random
        attempt = []
        len_rest = len(self.__masterset) - len(self.__restrictions)
        if self.__len <= len_rest:
            for x in range(self.__len):
                x = random.randint(0, 9)
                while (x in self.__restrictions) or (x in attempt):
                    x = random.randint(0, 9)
                attempt.append(x)
        else:
            old_len = self.__len
            self.__len = len_rest
            attempt = PFgenerator.makeAttempt(self)
            self.__len = old_len - len_rest
            old_restrictions = self.__restrictions
            self.__restrictions = PFgenerator.complement(
                self, self.__restrictions)
            attempt += PFgenerator.makeAttempt(self)
            self.__len = old_len
            self.__restrictions = old_restrictions
            attempt = list(attempt)
            random.shuffle(attempt)
        return tuple(attempt)

    def complement(self, restrictions=()):
        return tuple(self.__masterset - set(restrictions))


firstattempt = PFgenerator()
x = firstattempt.makeAttempt()
print(x)

secondattempt = PFgenerator(restrictions=x)
y = secondattempt.makeAttempt()
print(y)

thirdattempt = PFgenerator(restrictions=x + y)
z = thirdattempt.makeAttempt()
print(z)
