import math
def volume(r):
	v = ((4/3)*(math.pi))*(r**3)
	print (v)

print ("The sphere's radius = ", end="") 

r = int(input())
while r <= 0:
	print ("The sphere's variable must be positive")
	print ("Please re-enter the value: ", end="")
	r = int(input())
volume(r)
