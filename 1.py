with open('data.txt') as f:
    lines = f.readlines()
    
total = 0
for line in lines:
    for a in line:
        if a.isdigit():
            one = a
    for b in reversed(line):
        if b.isdigit():
            two = b
    number = int(two + one)
    total += number
print(total)