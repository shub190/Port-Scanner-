import socket
import termcolor

def scan(target, ports):
    print('\n' + "STARTED SCANNING FOR " + str(target))
    for port in range(1, ports):
        scanport(target, port)

def scanport(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] PORT OPENED " + str(port))
        sock.close()
    except:
        pass

targets = input("[*] ENTER THE TARGET ADDRESS (Separated by ',' if there are multiple addresses) : ")
ports = int(input("[*] ENTER HOW MANY PORTS YOU WANT TO SCAN: "))
if ',' in targets:
    print(termcolor.colored(("[*] SCANNING MULTIPLE TARGETS "), 'green'))
    for ip_ad in targets.split(','):
        scan(ip_ad.strip(), ports)
else:
    scan(targets, ports)

