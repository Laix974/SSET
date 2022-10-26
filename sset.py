import time
import random
import os
import sys


rString = "qwéěeřrťtžzúůuíióopáašsďdfghjklýyxčcvbňnmQWÉĚEŘRŤTŽZÚŮUÍIÓOPÁAŠSĎDFGHJKLÝYXČCVBŇNM ,.1234567890@#€£$_&-+[<{(]>})/★†*”„“»«’‚‘›‹':;¡!¿‽?~`|•√π÷×§¶∆^°=%©®™✓"
#rString = "☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂ÇüéâäůćçłëŐőîŹÄĆÉĹĺôöĽľŚśÖÜŤťŁ×čáíóúĄąŽžĘę¬źČş«»░▒▓│┤ÁÂĚŞ╣║╗╝Żż┐└┴┬├─┼Ăă╚╔╩╦╠═╬¤đĐĎËďŇÍÎě┘┌█▄ŢŮ▀ÓßÔŃńňŠšŔÚŕŰýÝţ´­˝˛ˇ˘§÷¸°¨˙űŘř■ " + '"„“'
sList = ["q","Q","w","W","e","E","r","R","t","T","y","Y","u","U","i","I","o","O","p","P","a","A","s","S","d","D","f","F","g","G","h","H","j","J","k","K","l","L","z","Z","x","X","c","C","v","V","b","B","n","N","m","M","1","2","3","4","5","6","7","8","9","0"]
rList = []
key = 0
pss = False

def encryption(rKey):
	try:

	# Default UI
		print("Encryption" + '\033[0m')
		time.sleep(0.5)

	# User input
		userInput = input('\033[34m' + "Insert your message: " + '\033[0m')
		if rKey:
			key = rKeyMaker()
			print('\033[32m' + "Randomly generated encryption key: " + '\033[1;32m' + str(key))
		else:
			key = (input('\033[32m' + "Insert four digit encryption key: " + '\033[1;32m'))
		slicedInput = []
		slicedKey = []
		output1 = ""
		slicedOutput1 = []
		output2 = ""
		output3 = ""

	# Slice input
		for i in userInput:
			slicedInput.append(i)
		
		for i2 in str(key):
			slicedKey.append(int(i2))

	# 1st level encryption
		for u in range(len(slicedInput)):
			output1 = output1 + slicedInput[u]
			for y in range(slicedKey[0]):
				output1 = output1 + rList[random.randrange(0, len(rList))]

	# Slice output1
		for i3 in output1:
			slicedOutput1.append(i3)

	# 2nd level encryption
		for l in range(len(slicedOutput1)):
			if rList.index(slicedOutput1[l]) >= (len(rList) - int(slicedKey[1])):
				output2 = output2 + (rList[rList.index(slicedOutput1[l]) - (len(rList) - int(slicedKey[1]))])
			else:
				output2 = output2 + (rList[rList.index(slicedOutput1[l])+int(slicedKey[1])])

	# 3rd level encryption
		prefix = ""
		for i4 in range(slicedKey[2]*10 + slicedKey[3]):
			prefix = prefix + rList[random.randrange(0, len(rList))]
		output3 = prefix + output2

	# Printing result
		print('\033[0;0m' + '\033[35m' + "\nEncrypted message: " + '\033[0m' + output3)
	
	# Exception handling
	except ValueError as e:
		print("\n" + '\033[31m' + "Error: " + str(e) + '\033[0;0m')
	except IndexError as e:
		print("\n" + '\033[31m' + "Error: Invalid encryption key" + '\033[0;0m')
	except Exception as e:
		print("\n" + '\033[31m' + "Error: " + str(e) + '\033[0;0m')

def decryption():
	try:

	# Default UI
		print("Decryption")
		time.sleep(0.5)

	# User input
		userInput = input('\033[34m' + "Insert encrypted message: " + '\033[0m')
		key = (input('\033[32m' + "Insert four digit encryption key: " + '\033[1;32m'))
		slicedInput = []
		slicedKey = []
		output1 = ""
		slicedOutput1 = []
		output2 = ""

	# Slice input
		for i in userInput:
			slicedInput.append(i)
		
		for i2 in str(key):
			slicedKey.append(int(i2))

	# 3rd level decryption
		for i3 in range(slicedKey[2]*10 + slicedKey[3]):
			slicedInput.pop(0)

	# 2nd level decryption
		for l in range(len(slicedInput)):
			if rList.index(slicedInput[l]) >= (len(rList) - int(0 - slicedKey[1])):
				output1 = output1 + (rList[rList.index(slicedInput[l]) - (len(rList) - int(0 - slicedKey[1]))])
			else:
				output1 = output1 + (rList[rList.index(slicedInput[l])+int(0 - slicedKey[1])])

	# Slice output1
		for i3 in output1:
			slicedOutput1.append(i3)

	# 1st level decryption
		for i4 in range(int(len(slicedOutput1)/(slicedKey[0]+1))):
			output2 = output2 + slicedOutput1[0]
			for i5 in range(slicedKey[0]+1):
				slicedOutput1.pop(0)

	# Printing result
		print('\033[0;0m' + '\033[35m' + "\nDecrypted message: " + '\033[0m' + output2)
	
	# Exception handling
	except ValueError as e:
		print("\n" + '\033[31m' + "Error: " + str(e) + '\033[0;0m')
	except IndexError as e:
		print("\n" + '\033[31m' + "Error: " + str(e) + '\033[0;0m')
	except Exception as e:
		print("\n" + '\033[31m' + "Error: " + str(e) + '\033[0;0m')

def options():
	clearConsole()
	opt = input('\033[35m' + "SSET (Super Secret Encryption Tool) - by Laix974" + '\033[0m' + "\nCommands:\n  e	Encrypt messages.\n  er	Encrypt messages with randomized key.\n  d	Decrypt messages.\n  man	Display manual.\n\n" + '\033[35m')
	clearConsole()

	if opt == "d":
		decryption()
	elif opt == "e":
		encryption(False)
	elif opt == "er":
		encryption(True)
	elif opt == "sus":
		sus()
	elif opt == "man":
		man()
	elif opt == "fx":
		fx()
	else:
		print('\033[1;31m' + "option (" + opt + ") doesn't exist" + '\033[0;0m')

def clearConsole():
	os.system('cls' if os.name == 'nt' else 'clear')

def rListMaker():
	for q in range(len(rString)):
		rList.append(rString[q])

def rKeyMaker():
	key = random.randrange(1111, 10000)
	return key

def printSupportedSymbols():
	print(rString)

def sus():
	print('\033[1;31m' + 
'''    ⠀⠀⠀⠀⠀  ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀ 
⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀     ⠀⠀⣿⣷⠀ 
⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀ 
⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀ 
⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀ 
⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢸⣿⣧⠀⠀ 
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀ 
⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢸⣿⡇⠀⠀ 
⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⣿⠃⠀⠀ 
⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀ ⢠⣿⣿⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀ ⣿⣿⡇ ⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀'''
 + '\033[0;0m')

def man():
	manual = (
'''
NAME
	SSET - Super Secret Encryption Tool

DESCRIPTION
	SSET is highly sophisticated unbreakable encryption tool which provides algorithms for encryption, decryption and other cryptographic modification of text.
	
	It runs on any terminal and it's made with Python3, so make sure that it is installed. This program is completely free for personal use, with one exception: You have to pay me.
	
	See 'Commands' section to get started with cryptographic tools.

SUPPORTED SYMBOLS
	''' + '\033[0;33m' + rString + '\033[0;0m' + '''

COMMANDS
	man
	e
	er
	d
	fx, fx <index>
	sus

REPORTING BUGS
	Report the bugs to your mom, i don't care.

AUTHOR
	SSET was made by me and it's currently maintained by me.
	- Laix974
''')
	print("Manual (WIP)")
	print('\033[0;0m' + manual)
	input('\033[1;0m' + "\nPress <Enter> go back.\n" + '\033[0;0m')
	clearConsole()
	options()

def fx():
	# add this to options (\n  fx	Fix corrupted messages.)
	
	fxIndexes = ('\033[0;0m' + 
'''Indexes:
  1	Fix messages with <Enter> problems.
  2	placeholder
  3	placeholder
  4	placeholder
  5	placeholder
''')
	
	print("Fixes (WIP)")
	fixIndex = str(input(fxIndexes + '\033[35m' + "\n"))

	if fixIndex == "1":
		fix(1)
	elif fixIndex == "2":
		fix(2)
	elif fixIndex == "3":
		fix(3)
	elif fixIndex == "4":
		fix(4)
	elif fixIndex == "5":
		fix(5)
	else:
		clearConsole()
		print('\033[1;31m' + "Invalid fix index" + '\033[0;0m')

def fix(i):
	if i == 1:
		clearConsole()
		print("do a fix 1")	
	elif i == 2:
		clearConsole()
		print("do a fix 2")
	elif i == 3:
		clearConsole()
		print("do a fix 3")
	elif i == 4:
		clearConsole()
		print("do a fix 4")
	elif i == 5:
		clearConsole()
		print("do a fix 5")

rListMaker()
options()
