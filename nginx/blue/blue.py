import http.server
import socketserver

PORT = 8080

class BlueHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Simple HTML content with blue background
        content = """
        <html>
            <head><title>Blue Website</title></head>
            <body style="background-color: blue;">
                <h1 style="color: white; text-align: center;">Welcome to the Blue Website!</h1>
            </body>
        </html>
        """

        self.wfile.write(content.encode('utf-8'))

with socketserver.TCPServer(("", PORT), BlueHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
