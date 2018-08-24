def get_ips_from_file(file_ip):
    import sys
    list_ips = []

    print("Opening file...")
    try:
        with open(file_ip, "r") as file:
            for x in file:
                x = x.rstrip()
                list_ips.append(validate_ips(x))
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        exit(0)
    except:
        print("Unexpected error:", sys.exc_info()[0])
    return list_ips

def validate_ips(ip):
    import ipaddress
    try:
        if ipaddress.ip_network(ip).prefixlen == 8 or ipaddress.ip_network(ip).prefixlen >= 16:
            return ip
        elif ipaddress.ip_network(ip).prefixlen < 8:
            raise ValueError
        elif ipaddress.ip_network(ip).prefixlen < 16 and ipaddress.ip_network(ip).prefixlen > 8:
            raise ValueError
    except ValueError:
        print("AWS WAF supports IPv4 address ranges: /8 and any range between /16 through /32")
        exit(0)
