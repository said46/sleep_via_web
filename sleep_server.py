import http.server
import socketserver
import time
import os
import ctypes

class WebHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/sleep':
            print(f"Sleep request from: {self.client_address[0]}")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''
                <html><body>
                <h1>Computer Sleep</h1>
                <p>Putting computer to sleep in 3 seconds...</p>
                </body></html>
            ''')
            
            time.sleep(3)
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            print("Computer going to sleep!")
        elif self.path == '/lock':
            print(f"Lock request from: {self.client_address[0]}")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''
                <html><body>
                <h1>Computer Lock</h1>
                <p>Locking computer in 3 seconds...</p>
                </body></html>
            ''')
            
            time.sleep(3)
            ctypes.windll.user32.LockWorkStation()
            print("Computer going to be locked!")            
        elif self.path == '/':
            print(f"Status request from: {self.client_address[0]}")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''
                <html><body>
                <h1>Web Sleep/Lock Server</h1>
                <p>Server is running!</p>
                <p>Use <a href="/sleep">/sleep</a> to put computer to sleep</p>
                <p>Use <a href="/lock">/lock</a> to lock computer</p>
                </body></html>
            ''')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''
                <html><body>
                <h1>404 - Not Found</h1>
                <p>Use <a href="/sleep">/sleep</a> path to put computer to sleep</p>
                <p>Use <a href="/lock">/lock</a> path to lock computer</p>
                </body></html>
            ''')

print("Setting up web server...")
print("Web server started on port 9999")
print("Access via: http://localhost:9999/sleep")

with socketserver.TCPServer(("", 9999), WebHandler) as httpd:
    httpd.serve_forever()