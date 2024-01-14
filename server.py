import http.server
import socketserver

class NoDirectoryListingHandler(http.server.SimpleHTTPRequestHandler):
    def list_directory(self, path):
        self.send_error(404, "Not Found")

# Set the port number you want to use
PORT = 8089

# Create a custom HTTP server using the custom request handler
Handler = NoDirectoryListingHandler

# Use the socketserver module to bind and activate the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    
    # Start the server
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer terminated by user.")
