with open('#1/data.txt') as f:
    lines = f.readlines()

def replace_numbers(line):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    locations_min = []
    locations_max = []
    #find locations of first written numbers from the back and the front as these are the only ones needed to replace
    for number in numbers:
        if number in line:
            locations_min.append(line.index(number))
            locations_max.append(line.rindex(number))
        else:
            locations_min.append(-1)
            locations_max.append(-1)
    #if there are written numbers, replace the first and the last by their digit
    if max(locations_min) != -1:
        lowest = locations_min.index(min(n for n in locations_min  if n>=0))
        highest = locations_max.index(max(locations_max))
        #had to do the -1 to get rid of overlaps
        newline = line.replace(numbers[lowest][:-1], str(lowest))

        #replace last written number from the back
        old = numbers[highest]
        new = str(highest)
        newline = new.join(newline.rsplit(old))
        return newline
    else:
        return line 

total = 0
for line in lines:
    line = replace_numbers(line)
    for a in line:
        if a.isdigit():
            one = a
        
    for b in reversed(line):
        if b.isdigit():
            two = b
    number = int(two + one)
    total += number
print(total)