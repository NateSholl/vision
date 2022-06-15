from http import server
import socket

msg_from_client = "Hello UDP Server!"
bytes_from_client = str.encode(msg_from_client)
server_address_port = ('127.0.0.1', 20001)
buffer_size = 1024

# CREATE CLIENT SIDE UDP SOCKET

udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# SEND MSG TO SERVER

udp_client_socket.sendto(bytes_from_client,server_address_port)

# RECEIVE MSG FROM SERVER

msg_from_server = udp_client_socket.recvfrom(buffer_size)

msg_out = f'Message from server : {msg_from_server}'

print(msg_out)