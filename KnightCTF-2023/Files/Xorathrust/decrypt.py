output = ''
with open('flag.enc.txt', 'rb') as file:
    flag = file.read()
    flag = list(flag)
    for character in flag:
        output += chr(character ^ 0x66)
print(output)