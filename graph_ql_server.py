from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class GraphQLHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length).decode('utf-8')
        
        # Parse the incoming GraphQL query
        query = json.loads(data)['query']
        
        # Process the query (For simplicity, this example just echoes back the query)
        response = {'data': {'result': query}}
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        self.wfile.write(json.dumps(response).encode('utf-8'))

def run_server():
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, GraphQLHandler)
    print('Starting server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
