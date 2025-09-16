with open('auth.log', 'r') as f:
    for line in f:
        line = auth.log.readlines()
        print(line.strip())

import re
pattern = r"\d+\.\d+\.\d+\.\d+"

print(re.findall(pattern, line))