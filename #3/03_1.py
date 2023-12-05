symbols = '@-#=/*+%$&'
with open('#3\input.txt') as f:
    lines = f.readlines()
import re 

for line in lines:
    #get numbers
    splitline = re.split(r"\D+" , line.strip())
    print(splitline)

