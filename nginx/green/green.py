import http.server
import socketserver

PORT = 8080

class GreenHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Simple HTML content with blue background
        content = """
        <html>
            <head><title>Green Website</title></head>
            <body style="background-color: green;">
                <h1 style="color: white; text-align: center;">Welcome to the Green Website!</h1>
            </body>
        </html>
        """

        self.wfile.write(content.encode('utf-8'))

with socketserver.TCPServer(("", PORT), GreenHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

