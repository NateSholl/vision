import socket

local_ip_address = '127.0.0.1'
local_port = 20001
buffer_size = 1024

msg_from_server = 'Hello UDP Client!'
bytes_from_server = str.encode(msg_from_server)

# CREATE DATAGRAM SOCKET

udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# BIND ADDRESS TO PORT

udp_server_socket.bind((local_ip_address,local_port))
print("UDP Server up and listening.")

# LISTEN

while(True):
    byte_address_pair = udp_server_socket.recvfrom(buffer_size)
    message = byte_address_pair[0]
    address = byte_address_pair[1]

    client_msg = f"Message from Client : {message}"
    client_address = f"Address of Client : {address}"

    print(client_msg)
    print(client_address)

    # SENDING REPLY TO CLIENT

    udp_server_socket.sendto(bytes_from_server,address)