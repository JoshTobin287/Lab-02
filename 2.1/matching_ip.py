import re

pattern = r"\d+\.\d+\.\d+\.\d+"
text = "Failed login from 192.168.0.1 and at 10:30"

print(re.findall(pattern, text))

import re

pattern = r"\d+\.\d+\.\d+\.\d+"
text = "Failed login from 192.168.0.1 and 10.0.0.5at 10:30"

print(re.findall(pattern, text))