import md5
import base64
import random
import sys
import hashlib
import binascii


def hashit(filestring,filestring2,animal,A,B,presalt):

	m = hashlib.md5()
	salt = salt_fun()				#get salt
	filestring = filestring+salt			#concatenate
	m.update(filestring)
	has = m.hexdigest()
	has = has[0:3]					#get first 10 hex digits of hasi

	if(animal == "cat"):				#check if cat or dog file and see if there's a match
		check = set(A).intersection(B)
		if(len(check) == 0):				#if there's no match, append
			A.append(has)
			loop = 0
		else:
			print "MATCH IN CAT"
			filestring = filestring+salt
			fh = open("UglyCat2.jpg","wb")
			fh.write(filestring.decode('base64'))
			fh.close()

			filestring2 = filestring2+presalt
			fh = open("UglyDog2.jpg","wb")
			fh.write(filestring2.decode('base64'))
			fh.close()

			loop = 1

	else:
		check = set(A).intersection(B)
		if(len(check) == 0):
			B.append(has)
			loop = 0
		else:
			print "MATCH IN DOG"
			filestring = filestring+salt
			fh = open("UglyDog2.jpg","wb")
			fh.write(filestring.decode('base64'))
			fh.close()

			filestring2 = filestring2+presalt
			fh = open("UglyCog2.jpg","wb")
			fh.write(filestring2.decode('base64'))
			fh.close()

			loop = 1

	presalt = salt
	return	(loop,A,B,presalt)
	


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
	animal = "cat"

	with open("UglyCat.jpg","rb") as imageFile:
		filestring = base64.b64encode(imageFile.read())

	with open("UglyDog.jpg","rb") as imageFile:
		filestring2 = base64.b64encode(imageFile.read())

	presalt = ""
	loop,A,B,presalt = hashit(filestring,filestring2,animal,A,B,presalt)
				

	while loop == 0:
		animal = "dog"
		loop,A,B,presalt = hashit(filestring2,filestring,animal,A,B,presalt)
		if (loop == 0):
			animal = "cat"
			loop,A,B,presalt = hashit(filestring,filestring2,animal,A,B,presalt)


main()
