"""
USAGE:

   python devserver.py

   OR

   python3 devserver.py

   THEN open up http://localhost:8000 in your browser
"""
import http.server
import socketserver

# Print starting messages
print("Watching files...")

"""If you want to define a custom port, then change the value below and uncomment the line"""
PORT = 8000
# PORT = sys.argv[1]
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at http://localhost:", PORT)
    print("Press CTRL C to stop this server.")
    httpd.serve_forever()

