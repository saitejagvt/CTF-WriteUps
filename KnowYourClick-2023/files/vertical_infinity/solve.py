import string

with open('vertical_infinity.txt','r') as file:
	conts=file.read()#text is in octal form

def octal_to_chr(octals):#function to convert octal to ascii numbers
    string = ""
    for octal in octals.split(" "):
        string += chr(int(octal, 8))
    return string

nums=octal_to_chr(conts).split(' ')
nums.pop()#remove last empty element in list
for i in nums:
	print(chr(int(i)),end='')
print('\n')
output = (4, 15, 12, 12, 1, 18, 6, 12, 1, 7, 15, 16, 5, 14, 2, 18, 1, 3, 5, 4, 5, 6, 21, 19, 1, 12, 28, 4, 5, 12, 20, 1, 3, 12, 15, 19, 5, 2, 18, 1, 3, 5)

d={27:' ',28:'_'}
for key,val in enumerate(list(string.ascii_lowercase)):#create key value dictionary
	d[key+1]=val

for i in output:
	print(d[i],end='')
print()
#flag - KYC{defusal_delta}