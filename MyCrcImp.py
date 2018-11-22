def xor(a,b):
	if(a==b) :
		return '0';
	else:
		return '1'

def compCrc16(datStr):
	temp=datStr
	divisor="10001000000100001"
	b=17
	rem=""
	temp=datStr[:b]
	while(b<len(datStr)):
		if temp[0]=='1':
			div=divisor
		else:
			div="0"*17
		for i,j in zip(temp,div):
			rem+=xor(i,j)
		temp=rem[1:]+datStr[b]
		rem=""
		b+=1
	return temp[1:]
