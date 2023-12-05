with open('#5\input.txt') as f:
    lines = f.read()
import re



separate_files = lines.split("\n\n")

all_info = []
for file in separate_files:
    add_list = re.split(r":\n|: |\n" , file.strip())
    all_info.append(add_list)
print(all_info)