from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class handler(BaseHTTPRequestHandler):
    """
    HTTP request handler class that processes GET and POST requests

    :method do_GET: Handles GET requests. Responds with a simple text message
    :method do_POST: Handles POST requests. Responds with a simple text message and runs an external python script using subprocess
    """

    def do_GET(self):
        """
        Handles GET requests

        Reponds with a 200 status code and a text message 
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        msg = "Hello this is working"
        self.wfile.write(bytes(msg, "utf-8"))
    
    def do_POST(self):
        """
        Handles POST requests

        Responds with a 200 status code and a text message. Additionally, runs an external python script
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        msg = "Post is working"
        self.wfile.write(bytes(msg, "utf-8"))

        # Running the external script './main.py' using subprocess
        subprocess.run(["python", "./main.py"])
        

if __name__ == "__main__":
    """ 
    The entry point of the script

    Starts a HTTP server on port 8000 with the handler class to handle incoming requests
    """
    with HTTPServer(('', 8000), handler) as server: 
        print("server starting...")
        server.serve_forever()
