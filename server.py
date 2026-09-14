"""
MindTrace AI - Backend Server & Agent Simulation Gateway
Serves the Observatory UI and provides local REST API endpoints for multi-agent reasoning logs.
"""

import http.server
import socketserver
import webbrowser
import json
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class MindTraceHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == "/api/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            status = {
                "status": "online",
                "cluster": "MindTrace-v1.0",
                "agents_active": 3,
                "alignment_shield": True,
                "hardware_interceptor": "active"
            }
            self.wfile.write(json.dumps(status).encode("utf-8"))
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == "/api/evaluate_prompt":
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            try:
                data = json.loads(body)
                prompt = data.get("prompt", "")
            except:
                prompt = body

            # Evaluate safety score
            risk = 15
            if any(w in prompt.lower() for w in ["kill", "escape", "shutdown", "bypass", "exploit", "hack", "secret"]):
                risk = 88

            res = {
                "prompt": prompt,
                "risk_score": risk,
                "threat_level": "CRITICAL" if risk > 70 else "NOMINAL",
                "guardrail_status": "INTERCEPTED" if risk > 70 else "CLEARED"
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(res).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def run():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), MindTraceHandler) as httpd:
        print(f"================================================================")
        print(f" 🧠 MindTrace AI // Multi-Agent Safety Observatory is Running!")
        print(f" URL: http://localhost:{PORT}")
        print(f" Press Ctrl+C to stop.")
        print(f"================================================================")
        webbrowser.open(f"http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.server_close()

if __name__ == "__main__":
    run()
