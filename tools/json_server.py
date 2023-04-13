from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _do_request(self):
        if self.headers.get('Content-type', None) != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        length = int(self.headers.get('Content-length', 0))
        messages = json.loads(self.rfile.read(length))

        for k, v in messages.items():
            print(k, v)

        self._set_headers()
        self.wfile.write(bytes(json.dumps(messages), 'utf-8'))

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        print('** GET **')
        self._do_request()

    def do_POST(self):
        print('** POST **')
        self._do_request()
    

def run(server_class=HTTPServer, handler_class=Server):
    server_address = ('', 8008)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()