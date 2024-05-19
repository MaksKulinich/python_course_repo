from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import urllib.parse
import pathlib
import mimetypes
import socket
import json
import threading


UDP_IP = "127.0.0.1"
UDP_PORT = 5000
WRITE_FILE = "storage/data.json"


class HttpHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data_parse = urllib.parse.unquote_plus(data.decode())
        data_dict = {
            key: value for key, value in [el.split("=") for el in data_parse.split("&")]
        }

        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_sock.sendto(json.dumps(data_dict).encode(), (UDP_IP, UDP_PORT))
        udp_sock.close()

        self.send_response(302)
        self.send_header("Location", "/")
        self.end_headers()

    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        if pr_url.path == "/":
            self.send_html_file("index.html")
        elif pr_url.path == "/message.html":
            self.send_html_file("message.html")
        else:
            if pathlib.Path().joinpath(pr_url.path[1:]).exists():
                self.send_static()
            else:
                self.send_html_file("error.html", 404)

    def send_html_file(self, filename, responce=200):
        self.send_response(responce)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(filename, "rb") as fd:
            self.wfile.write(fd.read())

    def send_static(self):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", "text/plain")
        self.end_headers()
        with open(f".{self.path}", "rb") as file:
            self.wfile.write(file.read())


def run(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ("", 3000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


def socket_server():
    upd_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    upd_sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, address = upd_sock.recvfrom(1024)
        message = json.loads(data.decode())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")

        # with open(WRITE_FILE, "r+") as w_file:
        #     data_file = json.load(w_file)
        #     data_file[timestamp] = message
        #     json.dump(data_file, w_file)

        with open(WRITE_FILE, "r") as r_file:
            try:
                data_file = json.load(r_file)
            except json.JSONDecodeError:
                data_file = {}

        data_file[timestamp] = message

        with open(WRITE_FILE, "w") as w_file:
            json.dump(data_file, w_file, indent=4)

    upd_sock.close()


if __name__ == "__main__":
    http_thread = threading.Thread(target=run)
    socket_thread = threading.Thread(target=socket_server)

    http_thread.start()
    socket_thread.start()

    http_thread.join()
    socket_thread.join()
