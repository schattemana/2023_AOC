#need list with original scores

with open('#4\input.txt') as f:
    lines = f.readlines()
import re 


score = []
cards = [1]*189 #189 cards so we start with one card of each
for line in lines:
    #get numbers
    splitline = re.split(r"[:|]" , line.strip())
    win = splitline[1].split()
    card = splitline[2].split()

    total = 0
    for number in win:
        number_count = card.count(number)
        total += number_count
    score.append(total)

cards = [1]*189 #189 cards so we start with one card of each
for i, points in enumerate(score):
    
    cards[i+1:i+points+1] = [x+1 *cards[i] for x in cards[(i+1):(i+points+1)]]
print(sum(cards))