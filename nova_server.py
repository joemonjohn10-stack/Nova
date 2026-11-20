#!/usr/bin/env python3
"""NOVA local web server and same-origin AI proxy (Python standard library only)."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from pathlib import Path
import json, os, socket

ROOT = Path(__file__).resolve().parent
MAX_BODY = 1_000_000

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt, *args):
        # Do not log request bodies, prompts, or credentials.
        super().log_message(fmt, *args)

    def _json(self, status, payload):
        raw = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(raw)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        if self.path == '/api/status':
            return self._json(200, {'ok': True, 'service': 'NOVA local AI proxy'})
        return super().do_GET()

    def do_POST(self):
        if self.path != '/api/chat':
            return self._json(404, {'error': {'message': 'Endpoint not found'}})
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if length <= 0 or length > MAX_BODY:
                return self._json(413, {'error': {'message': 'Request is empty or too large'}})
            body = json.loads(self.rfile.read(length))
            endpoint = str(body.get('endpoint', '')).strip()
            model = str(body.get('model', '')).strip()
            key = str(body.get('key', '')).strip()
            messages = body.get('messages', [])
            if not endpoint or not model or not key or not isinstance(messages, list):
                return self._json(400, {'error': {'message': 'Endpoint, model, API key and messages are required'}})
            parsed = urlparse(endpoint)
            if parsed.scheme != 'https' or not parsed.netloc:
                return self._json(400, {'error': {'message': 'Provider endpoint must be a valid HTTPS URL'}})
            payload = json.dumps({'model': model, 'messages': messages, 'temperature': 0.7}).encode()
            req = Request(endpoint, data=payload, headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + key,
                'User-Agent': 'NOVA-Personal-Assistant/1.0'
            }, method='POST')
            try:
                with urlopen(req, timeout=50) as response:
                    result = json.loads(response.read().decode('utf-8'))
                    return self._json(response.status, result)
            except HTTPError as exc:
                detail = exc.read(12000).decode('utf-8', 'replace')
                try:
                    parsed_error = json.loads(detail)
                except Exception:
                    parsed_error = {'error': {'message': detail[:1500]}}
                return self._json(exc.code, parsed_error)
            except URLError as exc:
                return self._json(502, {'error': {'message': 'Could not reach provider: ' + str(exc.reason)}})
        except (ValueError, json.JSONDecodeError) as exc:
            return self._json(400, {'error': {'message': 'Invalid request: ' + str(exc)}})
        except Exception as exc:
            return self._json(500, {'error': {'message': 'NOVA server error: ' + str(exc)}})

if __name__ == '__main__':
    port = int(os.environ.get('NOVA_PORT', '8000'))
    server = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    print(f'NOVA is running at http://127.0.0.1:{port}')
    print('AI proxy is available at /api/chat. Press Ctrl+C to stop.')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nNOVA stopped.')
    finally:
        server.server_close()
