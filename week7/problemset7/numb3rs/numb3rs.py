import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


# for testing
# 275.3.6.28
# 127.0.0.1
# 255.255.255.255
# 1.2.3.1000
# 512.512.512.512
# cat.

def validate(ip):
    pattern = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"

    # the actual regex pattern for IPv4 validation is this
    # pattern = r"^(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})$"
    match = re.search(pattern, ip)
    # print(match.groups())
    if match:
        list_groups = match.groups()
        for i in list_groups:
            if int(i) > 255:
                return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()
