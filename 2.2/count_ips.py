
def ip_parser(line):
    if " from " in line:
        ip = line.split() 
        try:    
            anchor = ip.index("from")    
            ips = ip[anchor+1]    
            return ips.strip()       

        except (ValueError, IndexError):
            return None

    return None

from collections import defaultdict

counts = defaultdict(int)           

with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            # extract ip
            ip = ip_parser(line)
            if ip:
                counts[ip] += 1
print(counts)