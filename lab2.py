import re

with open('auth.log', 'r') as f:
    for line in f:
        pattern = r"\d+\.\d+\.\d+\.\d+"
        print(line.strip())
        ips = []
        print(re.findall(pattern, line))


