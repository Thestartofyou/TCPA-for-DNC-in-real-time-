import socket

def connect_to_tcp_server(server_ip, server_port):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the TCP server
        client_socket.connect((server_ip, server_port))

        # Send a request to the server (if needed)
        # client_socket.send(b"REQUEST")

        # Receive data from the server
        response = client_socket.recv(1024)
        print("Received:", response.decode())

        # Close the socket
        client_socket.close()

    except socket.error as e:
        print("Error:", str(e))

if __name__ == "__main__":
    # Replace the following values with the appropriate TCPA/DNC server IP and port
    server_ip = "your_tcpa_dnc_server_ip"
    server_port = 1234

    connect_to_tcp_server(server_ip, server_port)

