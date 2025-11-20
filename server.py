#!/usr/bin/env python3
"""
Simple HTTP server with no-cache headers for local network access.
"""
import http.server
import socketserver
import socket
from functools import partial

PORT = 8000

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler with no-cache headers."""

    def end_headers(self):
        """Add no-cache headers to all responses."""
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def get_local_ip():
    """Get the local IP address for network access."""
    try:
        # Create a socket to find the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to an external address (doesn't actually send data)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1"

if __name__ == "__main__":
    local_ip = get_local_ip()

    with socketserver.TCPServer(("", PORT), NoCacheHTTPRequestHandler) as httpd:
        print(f"\n{'='*60}")
        print(f"Server started successfully!")
        print(f"{'='*60}")
        print(f"\nLocal access:")
        print(f"  http://localhost:{PORT}")
        print(f"\nNetwork access (share this with others on your network):")
        print(f"  http://{local_ip}:{PORT}")
        print(f"\n{'='*60}")
        print(f"Press Ctrl+C to stop the server")
        print(f"{'='*60}\n")

        httpd.serve_forever()
