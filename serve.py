#!/usr/bin/env python3
"""Tiny static server that tolerates trailing slashes on files (for browser previews)."""
import http.server
import os
import socketserver

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def _strip_trailing_slash_for_file(self):
        # Browser-preview URLs sometimes carry a trailing slash. If that path
        # points to an actual file, drop the slash so the file is served.
        if self.path.endswith('/'):
            file_path = self.translate_path(self.path.rstrip('/'))
            if os.path.isfile(file_path):
                self.path = self.path.rstrip('/')

    def do_GET(self):
        self._strip_trailing_slash_for_file()
        return super().do_GET()

    def do_HEAD(self):
        self._strip_trailing_slash_for_file()
        return super().do_HEAD()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

if __name__ == '__main__':
    with socketserver.TCPServer(('localhost', PORT), Handler) as httpd:
        print(f'Serving at http://localhost:{PORT}/')
        httpd.serve_forever()
