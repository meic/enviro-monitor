import json

from http.server import BaseHTTPRequestHandler, HTTPServer

from dht22 import DHT22


hostname = ""
server_port = 8000


dht22 = DHT22()


class EnviroMonitorServer(BaseHTTPRequestHandler):
    def do_GET(self):
        temperature, humidity = dht22.get_reading()

        if temperature is None or humidity is None:
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"error": "DHT22 reading failed."}
            self.wfile.write(bytes(json.dumps(data), "utf-8"))
            return

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        data = {"temperature": temperature, "humidity": humidity}
        self.wfile.write(bytes(json.dumps(data), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostname, server_port), EnviroMonitorServer)
    print("Webserver started")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
