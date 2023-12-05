with open('#4\input.txt') as f:
    lines = f.readlines()
import re 


score = 0
for line in lines:
    #get numbers
    splitline = re.split(r"[:|]" , line.strip())
    win = splitline[1].split()
    card = splitline[2].split()

    total = 0
    for number in win:
        number_count = card.count(number)
        total += number_count
    if total > 0:
        score += 2**(total-1)
print(score)