import ipaddress


def main():
    my_ip = '216.58.194.206'

    print(my_ip)

    addr = ipaddress.ip_address(my_ip)

    print(ipaddress.ip_network(my_ip))
    print('Compressed: ', addr.compressed)
    print('Exploded: ', addr.exploded)
    print('Packed: ', addr.packed)
    print('As int: ', int(addr))
    print('As binary: ', bin(int(addr)))

    print('-------------------')

    network_mask = '192.0.2.0/24'
    print('Network mask: ', network_mask)
    print('Network subnets: ', list(ipaddress.ip_network(network_mask).subnets()))


if __name__ == '__main__':
    main()
