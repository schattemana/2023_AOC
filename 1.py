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



def replace_numbers(line):
    numberdict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
  "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0" }
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    locations = []
    for number in numbers:
        if number in line:
            locations.append(line.find(number))
        else:
            locations.append(-1)
    lowest = min(n for n in locations  if n>0)
    highest = max(locations)
    print(highest, lowest)


    return newline


print(replace_numbers("eightwothree"))

