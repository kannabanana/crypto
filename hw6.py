import md5
import base64
import random
import sys
import hashlib
import binascii


def hashit(filestring,filestring2,animal,A,B,saltA,saltB):
	f = filestring

	m = hashlib.md5()
	salt = salt_fun()				#get salt
	filestring3 = filestring+salt			#concatenate
	m.update(filestring3)
	has = m.hexdigest()
	has = has[0:3]					#get first 10 hex digits of hasi


	if(animal == "cat"):				#check if cat or dog file and see if there's a match
		check = set(A).intersection(B)
		if(len(check) == 0):				#if there's no match, append
			A.append(has)
			saltA.append(salt)
			loop = 0
		else:
			value = list(check)
			print "the collision is ",value[0]		
			print "\n"
			print "Cat list is ",A
			print "\n"
			print "Dog list is ",B
			loop = 1

	else:
		check = set(A).intersection(B)
		if(len(check) == 0):
			B.append(has)
			saltB.append(salt)
			loop = 0
		else:
			value = list(check)
			print "the collision is ",value[0]		
			print "\n"
			print "Cat list is ",A
			print "\n"
			print "Dog list is ",B
			loop = 1

	return	(loop,A,B,saltA,saltB)

	
#check if 
def match(value,array):
	count = "A"
	value = list(value)
	match = value[0]
	for x in range(0,len(array)):
		if(match == array[x]):
			print array[x]
			count = x
	if (count != "A"):
		return count
	else:
		print "DIDN'T FIND MATCH" 


def salt_fun():
	alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	salt= [None]*1000
        for x in xrange(1000):
                i = random.randint(0,25)
                salt[x] = alpha[i]
	salt = ''.join(salt)
        return salt



def main():
	random.seed()
	A = []
	B = []
	saltA = []
	saltB = []
	animal = "cat"


	with open("UglyCat.jpg","rb") as imageFile:
		filestring = base64.b64encode(imageFile.read())

	with open("UglyDog.jpg","rb") as imageFile:
		filestring2 = base64.b64encode(imageFile.read())

	loop,A,B,saltA,saltB = hashit(filestring,filestring2,animal,A,B,saltA,saltB)

	while loop == 0:
		animal = "dog"
		loop,A,B,saltA,saltB = hashit(filestring2,filestring,animal,A,B,saltA,saltB)
	
		if (loop == 0):
			animal = "cat"
			loop,A,B,saltA,saltB = hashit(filestring,filestring2,animal,A,B,saltA,saltB)


main()
