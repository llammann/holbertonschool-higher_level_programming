from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class APIServer(BaseHTTPRequestHandler):
    def _set_response(self, status_code=200, content_type='text/plain'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self._set_response()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))
        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self._set_response(content_type='application/json')
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self._set_response()
            self.wfile.write("OK".encode('utf-8'))
        else:
            self._set_response(status_code=404)
            self.wfile.write("Endpoint not found".encode('utf-8'))

def run(server_class=HTTPServer, handler_class=APIServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

