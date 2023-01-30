def reverse_change1(w:str):
    vary = [4, 3, 5, 6, 1, 2, 3, 3, 1]
    temp = list(w)
    for i in range(9):
        temp[i] = chr(ord(w[i]) - vary[i])
    return ''.join(temp)

def reverse_change2(w:str):
    vary = [1, 7, 5, 3, 5, 4, 2, 6, 3]
    temp = list(w)
    for i in range(9):
        temp[i] = chr(ord(w[i]) + vary[i])
    return ''.join(temp)

flag = reverse_change2(reverse_change1('djckktjbq'))
print(flag)