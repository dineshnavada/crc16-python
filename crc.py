import random
from MyCrcImp import *

n=random.randint(0,65536)
aug_n=n<<16
dataStr=str(bin(n))[2:]
augStr=str(bin(aug_n))[2:]
encRem=compCrc16(augStr)
codeData=dataStr+encRem
decRem=compCrc16(codeData)
print("-"*40)
print("|"+" "*9+"CRC16 Implementation"+" "*9+"|")
print("-"*40)
print("CRC-16 Generator:10001000000100001")
print("Dataword:"+dataStr)
print("Augumented Dataword:"+augStr)
print("Remainder generated at sender:"+encRem)
print("Codeword:"+codeData)
print("Remainder generated at receiver:"+decRem)
if('1' in decRem):
	print("Data rejected")
else:
	print("Data accepted")
