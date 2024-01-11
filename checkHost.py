import socket

hostname = "host.com"

def hostname_resolves(hostname):
    try:
        socket.gethostbyname(hostname)
        return 1
    except socket.error:
        return 0
    

# checkHost = hostname_resolves(hostname)

# if checkHost == 1:
#     print("hostname is valid")
# else: print("hostname is NOT valid")

