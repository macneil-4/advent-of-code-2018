total = 0
offset = 0

with open('input.txt','r') as fileobj:
    lines = []

    for line in fileobj:
        lines.append(line.strip())

        operator = line[0]
        offset = int(line[1:])

        if operator == '+':    
            total += offset 
        elif operator == '-':
            total -= offset
        else:
            print('invalid sign')

print('Final total is ',total)
