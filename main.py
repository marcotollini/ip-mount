from fire import Fire
import os
import ipaddress

command = "ip addr {operation} {ip}/{prefix} dev {interface}"

def mount_ip(interface, ip, prefix, number_ips, operation = "add"):
    if '.' in ip:
        ip = ipaddress.IPv4Address(ip)
        network = ipaddress.IPv4Network(f'{ip}/{prefix}', strict=False)
        max_ip = max(network)
    else:
        ip = ipaddress.IPv6Address(ip)
        network = ipaddress.IPv6Network(f'{ip}/{prefix}', strict=False)
        max_ip = max(network)

    for i in range(1, number_ips+1):
        if ip > max_ip:
            raise Exception(f'Out of mask. {i-1} ip added')

        os.system(command.format(ip=str(ip), prefix=prefix, interface=interface, operation=operation))
        if i % 100 == 0:
            print(f"Done {i}/{number_ips} interfaces: {operation}")
        ip = next(ip)


    print("All done :)")

if __name__ == "__main__":
    Fire(mount_ip)