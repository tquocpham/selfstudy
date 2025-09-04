# TCP Server
import socket
import threading


def handle_client(client_socket, address):
    """Handle individual client connection"""
    print(f"Connection from {address}")
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Received: {data}")
            # Echo back to client
            client_socket.send(f"Echo: {data}".encode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print(f"Connection closed with {address}")


def tcp_server(host='localhost', port=8080):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((host, port))
    server.listen(5)
    print(f"TCP Server listening on {host}:{port}")

    try:
        while True:
            client, address = server.accept()
            # Handle each client in a separate thread
            client_thread = threading.Thread(
                target=handle_client, args=(client, address))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server.close()

# TCP Client


def tcp_client(host='localhost', port=8080):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((host, port))

        while True:
            message = input("Enter message (or 'quit' to exit): ")
            if message.lower() == 'quit':
                break

            client.send(message.encode('utf-8'))
            response = client.recv(1024).decode('utf-8')
            print(f"Server response: {response}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

# UDP Server


def udp_server(host='localhost', port=8081):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")

    try:
        while True:
            data, address = server.recvfrom(1024)
            message = data.decode('utf-8')
            print(f"Received from {address}: {message}")

            # Echo back to client
            response = f"Echo: {message}"
            server.sendto(response.encode('utf-8'), address)

    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server.close()

# UDP Client


def udp_client(host='localhost', port=8081):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            message = input("Enter message (or 'quit' to exit): ")
            if message.lower() == 'quit':
                break

            client.sendto(message.encode('utf-8'), (host, port))
            response, server = client.recvfrom(1024)
            print(f"Server response: {response.decode('utf-8')}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()


# Example usage:
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(
            "Usage: python script.py [tcp_server|tcp_client|udp_server|udp_client]")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "tcp_server":
        tcp_server()
    elif mode == "tcp_client":
        tcp_client()
    elif mode == "udp_server":
        udp_server()
    elif mode == "udp_client":
        udp_client()
    else:
        print("Invalid mode. Use: tcp_server, tcp_client, udp_server, or udp_client")
