from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

def get_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

port = 8080
server_address = ('', port)

print(f"Starting server on port {port}")
print(f"Try accessing:")
print(f"1. http://localhost:{port}")
print(f"2. http://127.0.0.1:{port}")
print(f"3. http://{get_ip()}:{port}")

httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print("Server is running...")
httpd.serve_forever() 