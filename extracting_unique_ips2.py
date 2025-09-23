LOGFILE = "sample_auth_small.log"

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


if __name__ == "__main__":

    with open(LOGFILE, "r") as f:
        for line in f:
            print (ip_parser(line.strip()))