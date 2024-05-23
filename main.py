import socket, struct, os, dotenv, sys


def get_var():
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
    hex = add.split("-")

    mac_addr_hex = [int(i, 16) for i in hex]

    packet = struct.pack('BBBBBB', *mac_addr_hex)

    packet = b'\xff' * 6 + packet * 16

    return packet

def send_wol(packet, broadcast):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    try:
        sock.sendto(packet, (broadcast, 9))
        print("Message sent.")
        sock.close()
    except Exception as e:
        print("An error occured ", e)

def main():
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