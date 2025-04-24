import http.server
import socketserver

PORT = 80

Handler = http.server.SimpleHTTPRequestHandler

print(f"Serving fake Google website on port {PORT}")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
