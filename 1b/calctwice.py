import pdb

total = 0
offset = 0
first_duplicate = 0

with open('input.txt','r') as fileobj:
    lines = []
    
    duplicate_found = False

    found_frequencies = {total}
    
    while duplicate_found == False:
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

            if total not in found_frequencies:
                print('Adding ',total)
                found_frequencies.add(total)
            else:
                print('Duplicate Found')
                duplicate_found = True
                first_duplicate = total
                break

        fileobj.seek(0) # set file pointer back to beginning of file to repeat the search

print('Final total is ',total)
print('First duplicate is ',first_duplicate)
