import requests
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/79.0.3945.130 Safari/537.36",
    "Referer": "https://www.bilibili.com/"
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):        
        url_parts = urlparse(self.path)
        query_params = parse_qs(url_parts.query)
        
        # 获取特定参数的值
        # 12352380
        uid = query_params.get('uid', [''])[0]
        response = requests.get(f'https://api.bilibili.com/x/relation/stat?vmid={uid}', headers=DEFAULT_HEADERS)
        self.send_response(200)
        self.send_header('Content-type', 'application/json;')
        self.end_headers()
        self.wfile.write(response.text.encode())