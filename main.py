from fire import Fire
import os
import ipaddress

command = "ip addr {operation} {ip}/{prefix} dev {interface}"

def mount_ip(interface, ip, prefix, number_ips, operation = "add"):
    start = ipaddress.IPv4Address(ip)
    network = ipaddress.IPv4Network(f'{ip}/{prefix}', strict=False)
    it = network.hosts()
    while next(it) < start:
        continue

    for i in range(1, number_ips+1):
        ip = next(it)
        os.system(command.format(ip=str(ip), prefix=prefix, interface=interface, operation=operation))
        if i % 100 == 0:
            print(f"Done {i}/{number_ips} interfaces: {operation}")

    print("All done :)")

if __name__ == "__main__":
    Fire(mount_ip)