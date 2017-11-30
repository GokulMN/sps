
import random
from random import randint

def R_user_vs_computer (q,w):

	if q ==	w :
	 	print("match draw")
	elif q == '1' and w == '2':
	 	print("computer wins!!!")
	elif q == '2' and w == '3':
	 	print("computer wins !!")
	elif q == '3' and w == '1':
	 	print("computer wins!!")
	elif q == '2' and w == '1':
	 	print("user win!!")
	elif q == '3' and w == '2':
	 	print("user win!1")
	elif q == '1' and w == '3':
	 	print("user wins!!")


def R_user_vs_user (q,w):

	if q ==	w :
	 	print("match draw")
	elif q == '1' and w == '2':
	 	print("user_2 wins!!!")
	elif q == '2' and w == '3':
	 	print("user_2 wins !!")
	elif q == '3' and w == '1':
	 	print("user_2 wins!!")
	elif q == '2' and w == '1':
	 	print("user_1 win!!")
	elif q == '3' and w == '2':
	 	print("user_1 win!1")
	elif q == '1' and w == '3':
	 	print("user_1 wins!!")	 	


print("Enter no.of user ")
print("1 for single user")
print("2 for double user ")
no = input()

print ("enter the values...user_1""\n" "1 for stone""\n""2 for paper""\n""3 for scissors")

user_1 = input()

if user_1 == '1':
	a = ["stone"]
	a_N ='1'
elif(user_1 == "2"):
	a = ["paper"]
	a_N ='2'
elif(user_1 == "3"):
	a = ["scissors"]
	a_N ='3'

print(a[0])
print(a_N)

if no == '2':

	print ("enter the values...user_2""\n" "1 for stone""\n""2 for paper""\n""3 for scissors")

	user_2 = input()

	if user_2 == '1':
		b = ["stone"]
		b_N ='1'
	elif (user_2 == '2'):
		b = ["paper"]
		b_N ='2'
	elif(user_2 == '3'):
		b = ["scissors"]
		b_N ='3'

	print(b[0])
	print(b_N)

	R_user_vs_user (a_N,b_N)
elif no == '1':
	
	comp = random.randint(1,3)
	#print(comp)

	if comp == 1 :
		c = ["stone"]
		c_N ='1'
	elif (comp ==  2):
		c = ["paper"]
		c_N ='2'
	elif (comp == 3 ):
		c = ["scissors"]
		c_N ='3'
	print(c[0])
	print(c_N)

	R_user_vs_computer(a_N,c_N)
