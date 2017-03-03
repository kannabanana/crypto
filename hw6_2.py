import md5
import random
import sys
import hashlib
import binascii


def hashit(filename,animal,A,B,count):
	hash_md5 = hashlib.md5()

	salt = salt_fun(count)
#	filename = filename[:-4]
#	filename = filename+salt

	with open(filename,"rb") as f:
		for chunk in iter(lambda: f.read(4096),b""):
			hash_md5.update(chunk)

	x = hash_md5.hexdigest()
	ten = x[0:9]
	#check if it's a match to opposite array
	if(animal == "cat"):
		check = match(ten,B)
		if(check == 0):
			A.append(ten)
		else:
			return (check,A,B)
	else:
		check = match(ten,A)
		if(check == 0):
			B.append(ten)
		else:
			return (check,A,B)
	return	(check,A,B)


	
def salt_fun(count):
	random.seed(count)
	alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	salt= [None]*100
        for x in range(0,100):
                i = random.randint(0,25)
		#print (alpha[i])
                salt[x] = alpha[i]
	salt = ''.join(salt)
        return salt

#check if 
def match(value,array):
	check = 0
	for x in range(0,len(array)):
		if(value == array[x]):
			check = x
	return check


def main():

	A = []
	B = []
	animal = "cat"
	match,A,B = hashit(sys.argv[1],animal,A,B,0)
"""
	count = 1
	while match == 0:	
	
		count = count +1
		animal = "dog"
		match,A,B = hashit(sys.argv[2],animal,A,B,count)
		print A
		print B
		if (match == 0):
			count = count+1
			animal = "cat"
			match,A,B = hashit(sys.argv[1],animal,A,B,count)
			print A
			print B
		else:
			break
	
	print "MATCH FOUND ",match
	print A
	print B
"""	
main()
