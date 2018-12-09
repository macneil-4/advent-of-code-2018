import pdb

def check_one_char_diff(line1, line2):
    if line1 == line2:
        return False

    num_mismatches = 0
    count = 0

    for char in line1:
        if char != line2[count]:
            num_mismatches += 1
        count += 1

    if num_mismatches == 1:
        return True
    else:
        return False

def strip_mismatching_chars(line1, line2):
    count = 0
    new_str = ""
    for char in line1:
        if char == line2[count]:
            new_str += char
        count += 1

    return new_str

###

with open('box_ids.txt','r') as fileobj:
    lines = []
    check_lines = []
    checked = {''}

    for line in fileobj:
        lines.append(line.strip())

    for line1 in lines:
        for line2 in lines:
            diff = check_one_char_diff(line1, line2)
            if diff == True:
                print('line1 = ',line1)
                print('line2 = ',line2)
                result = strip_mismatching_chars(line1, line2)
                print('result = ',result)
