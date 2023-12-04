with open('#2\input.txt') as f:
    lines = f.readlines()

import re 
total = 0
for line in lines:

    line = line[line.index(':')+1:].strip()
    draws = re.split(',|;', line )
    min_dict = {'red': [0], 'green': [0], 'blue': [0]}
    for colour in draws:
       #list with a number at index 0  and a colour at index 1
       splitlist = (colour.strip().split())
       min_dict[splitlist[1]].append(int(splitlist[0]))
    r = max(min_dict['red'])
    g = max(min_dict['green'])
    b = max(min_dict['blue'])
    power = r*g*b
    total += power
print(total)