from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        msg = "Hello this is working"
        self.wfile.write(bytes(msg, "utf-8"))
    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        msg = "Post is working"
        self.wfile.write(bytes(msg, "utf-8"))

        subprocess.run(["python", "./main.py"])
        

with HTTPServer(('', 8000), handler) as server: 
    print("server starting...")
    server.serve_forever()
