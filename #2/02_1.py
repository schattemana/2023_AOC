with open('#2\input.txt') as f:
    lines = f.readlines()

import re

constraints_dict = {'red': 12, 'green': 13, 'blue': 14}
total = 0
minus = 0
for i,line in enumerate(lines):

    line = line[line.index(':')+1:].strip()
    total += (i+1)
    draws = re.split(',|;', line )
    for colour in draws:
       #list with a number at index 0  and a colour at index 1
       splitlist = (colour.strip().split())
       if int(splitlist[0]) > constraints_dict[splitlist[1]]:
           minus += (i+1)
           break
result = total-minus
        

print(result)
