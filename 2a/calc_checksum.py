# map <'char','int'>
# map <'char','count of char'>

# 2 of a, 3 of b

appears_twice = 0
appears_thrice = 0

with open('box_ids.txt','r') as fileobj:
    lines = []

    for line in fileobj:
        lines.append(line.strip())

        index = {}

        for char in line:
            if char == '\n':
                break
            elif char not in index:
                index[char] = 1
            else:
                index[char] += 1;

        found_double = False
        found_triple = False
        # its not clear from the instructions but only 1 double and 1 triple can be counted per word
        for key in index:
            if index[key] == 2 and found_double == False:
                appears_twice += 1
                found_double = True
            elif index[key] == 3 and found_triple == False:
                appears_thrice += 1
                found_triple = True

        index.clear()

checksum = appears_twice * appears_thrice
print('appears_twice * appears_thrice = checksum')
print(appears_twice ,' * ', appears_thrice,' = ', checksum)
