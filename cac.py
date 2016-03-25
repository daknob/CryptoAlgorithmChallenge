#!/usr/bin/python

from random import randint

def initBlock():
	BLOCK = []
	for i in range(0,4):
		BLOCK.append([])
		for j in range(0,4):
			BLOCK[i].append(0)
	return BLOCK

def printBlock(BLOCK):
	for row in BLOCK:
		synth = ""
		for column in row:
			synth += str(column) + "\t"
		print(synth)

def printBlockCh(BLOCK):
	for row in BLOCK:
		synth = ""
		for column in row:
			if(0x20 <= column <= 0x7e):
				synth += str(chr(column)) + "\t"
			else:
				synth += ".\t"
		print(synth)

def writeMessageToBlock(MSG, BLOCK):
	if(len(MSG) > 16):
		return False
	for i in range(0, len(MSG)):
		BLOCK[int(i/4)][i%4] = ord(MSG[i])
	return BLOCK

def newKey(BLOCK):
	ret = initBlock()
	for i in range(0,4):
		for j in range(0,4):
			ret[i][j] = randint(0,255)
	return ret

def xorBlocks(BLOCK1, BLOCK2):
	ret = initBlock()
	for i in range(0,4):
		for j in range(0,4):
			ret[i][j] = BLOCK1[i][j] ^ BLOCK2[i][j]
	return ret

def rotatecwBlock(BLOCK):
	ret = initBlock()
	for i in range(0,4):
		for j in range(0,4):
			ret[i][j] = BLOCK[4-j-1][i]
	return ret

def rotateccwBlock(BLOCK):
	return rotatecwBlock(rotatecwBlock(rotatecwBlock(BLOCK)))

print("We start with an empty block:")
Message = initBlock()
printBlock(Message)
print("We also start with a random key:")
Key = newKey(initBlock())
printBlock(Key)
print("We add the message 'Hello World':")
Message = writeMessageToBlock("Hello World", Message)
printBlock(Message)
print("A more humanly readable format:")
printBlockCh(Message)
print("The XOR Output is:")
CipherText = initBlock()
CipherText = xorBlocks(Message, Key)
printBlock(CipherText)
print("Or, in English:")
printBlockCh(CipherText)
print("Here's how it looks decrypted:")
printBlockCh(xorBlocks(CipherText, Key))
print("Let's do some rotation to the CipherText:")
RotateCW = rotatecwBlock(CipherText)
printBlock(RotateCW)
print("Let's rotate the CipherText back to the original:")
printBlock(rotateccwBlock(RotateCW))
print("We're now going to rotate and XOR repeatedly...")
Input = CipherText
ROUNDS = 4
for round in range(0,ROUNDS):
	print("Entering Round #" + str(round+1))
	Input = xorBlocks(Key, rotatecwBlock(Input))
	printBlockCh(Input)
print("We're now going to reverse the procedure...")
for round in range(0,ROUNDS):
	print("Entering Round #" + str(ROUNDS-round))
	Input = xorBlocks(Key, rotateccwBlock(Input))
	printBlockCh(Input)
print("Let's see the output of the decryption:")
PlainText = xorBlocks(Input, Key)
printBlockCh(PlainText)
