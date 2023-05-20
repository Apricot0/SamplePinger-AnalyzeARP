import dpkt


# Function to convert MAC address to human-readable format
def mac_addr(mac_bytes):
    # return ':'.join('%02x' % ord(b) for b in mac_bytes)
    return ':'.join('{:02x}'.format(byte) for byte in mac_bytes)


# Function to convert IP address to human-readable format
def ip_addr(ip_bytes):
    return '.'.join(str(byte) for byte in ip_bytes)


if __name__ == '__main__':
    # Open the pcap file in binary mode
    with open('my_arp.pcap', 'rb') as pcap_file:
        pcap = dpkt.pcap.Reader(pcap_file)
        packet_no = 0
        # Iterate over each packet in the pcap file
        for ts, buf in pcap:
            packet_no += 1

            # Check if the packet is an ARP packet
            if buf[12:14] == b'\x08\x06':
                arp_header = buf[14:42]
                arp_hardware_type = int.from_bytes(arp_header[0:2], byteorder='big')
                arp_protocol_type = arp_opcode_hex = '0x{:04x}'.format(int.from_bytes(arp_header[2:4], byteorder='big'))
                arp_hardware_size = int.from_bytes(arp_header[4:5], byteorder='big')
                arp_protocol_size = int.from_bytes(arp_header[5:6], byteorder='big')
                arp_opcode = int.from_bytes(arp_header[6:8], byteorder='big')
                arp_sender_mac = arp_header[8:14]
                arp_sender_ip = arp_header[14:18]
                arp_target_mac = arp_header[18:24]
                arp_target_ip = arp_header[24:28]
                if arp_opcode == 1:
                    arp_op_type = "Request"
                elif arp_opcode == 2:
                    arp_op_type = "Reply"
                else:
                    arp_op_type = "???"
                print("===========================================================")
                print(f"No: {packet_no}, Timestamp: {ts}, APR")
                print(f"Type: {arp_op_type}")
                print(f"Hardware type: {arp_hardware_type}\t Protocol type code: {arp_protocol_type}")
                print(f"Hardware size: {arp_hardware_size}\t Protocol size: {arp_protocol_size}")
                print('Sender MAC address:', mac_addr(arp_sender_mac))
                print('Sender IP address:', ip_addr(arp_sender_ip))
                print('Target MAC address:', mac_addr(arp_target_mac))
                print('Target IP address:', ip_addr(arp_target_ip))
                print("===========================================================")
