import socket, struct, os, dotenv, sys


def get_var():
    """
    loads the environment variables and retrieves the MAC address and broadcast address.
    :param:
    :return secrets: a dictionary containing 'mac' (the MAC addr) and 'broadcast' (the broadcast addr)
    :raise: exception if there is an issue retrieving the environment variables.
    """
    dotenv.load_dotenv()

    try:
        secrets = {
            'mac' : os.environ['MAC'],
            'broadcast': os.environ['BROADCAST']
        }
    except Exception as e: 
        raise e

    return secrets

def wol_packet(add):
    """
    Creates a Wake-on-LAN magic packet from a MAC addr
    :param add: the MAC addr in the format "XX-XX-XX-XX-XX-XX"
    :return packet: return the constructed magic packet
    """
    hex = add.split("-")

    mac_addr_hex = [int(i, 16) for i in hex]

    packet = struct.pack('BBBBBB', *mac_addr_hex)

    # a magic packet is formed by 6 bytes of 0xFF followed by 16 repetitions of the MAC address
    packet = b'\xff' * 6 + packet * 16

    return packet

def send_wol(packet, broadcast):
    """
    sends the Wake-on-LAN magic packet to the broadcast addr
    :param packet: the magic packet to be sent
    :param broadcast: the broadcast addr
    :return:
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    try:
        sock.sendto(packet, (broadcast, 9))
        print("Message sent.")
        sock.close()
    except Exception as e:
        print("An error occured ", e)

def main():
    """
    Main function to run the WoL script
    """
    print("Wol script running...")
    try: 
        secret = get_var()
    except Exception as e:
        print("An error occured ", e)
        print("MAC or broadcast missing.\nexiting...")
        sys.exit()

    packet = wol_packet(secret['mac'])
    send_wol(packet, secret['broadcast'])

if __name__ == "__main__":
    main() 