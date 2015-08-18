import socket, StringIO, sys, time

print 'Please enter in a port for the server to be run on:'
input_port = int(raw_input())
server_address = (host, port) = '', input_port

class ServeMe(object):

    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 15

    def __init__(self, server_address): 
       
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        listen_socket.bind(server_address)
        listen_socket.listen(self.request_queue_size)
        
        host, port = self.listen_socket.getsockname()[:2]
        
        self.server_name = socket.getfqdn(host)
        self.server_port = port

    def set_app(self, application):
        self.application = application

    def serve_forever(self):
        listen_socket = self.listen_socket
        while True:
            self.client_connection, client_address = listen_socket.accept()
            self.handle_one_request()

    def handle_one_request(self):
        self.request_data = request_data = self.client_connection.recv(1024)
        print(''.join(
            '< {line}\n'.format(line=line)
            for line in request_data.splitlines()
        ))

        self.parse_request(request_data)
        env = self.get_environ()
        result = self.application(env, self.start_response)
        self.finish_response(result)

    def parse_request(self, text):
        request_line = text.splitlines()[0]
        request_line = request_line.rstrip('\r\n')
        
        (self.request_method,  
         self.path,           
         self.request_version
         ) = request_line.split()


    def get_environ(self):
        env = {
                'wsgi.version':      (1, 0),
                'wsgi.url_scheme':   'http',
                'wsgi.input':         StringIO.StringIO(self.request_data),
                'wsgi.errors':        sys.stderr,
                'wsgi.multithread':   False,
                'wsgi.multiprocess':  False,
                'wsgi.run_once':      False,
                'REQUEST_METHOD':     self.request_method,    
                'PATH_INFO':          self.path,             
                'SERVER_NAME':        self.server_name,       
                'SERVER_PORT':        str(self.server_port),
        }  
        return env

    def start_response(self, status, response_headers, exc_info=None):
        server_headers = [
            ('Date', time.strftime('%H:%M:%S')),
            ('Server', 'HackyServer9001.0'),
        ]
        self.headers_set = [status, response_headers + server_headers]
  
    def finish_response(self, result):
        try:

            status, response_headers = self.headers_set
            response = 'HTTP/1.1 {status}\r\n'.format(status=status)
            for header in response_headers:
                response += '{0}: {1}\r\n'.format(*header)
            response += '\r\n'
            for data in result:
                response += data
            
            self.client_connection.sendall(response)
        finally:
            self.client_connection.close()    


def make_server(server_address, application):
    server = ServeMe(server_address)
    server.set_app(application)
    return server


if __name__ == '__main__':
    try:
        app_path = sys.argv[1]
        module, application = app_path.split('-')
        module = __import__(module)
        application = getattr(module, application)
        httpd = make_server(server_address, application)
        print('Starting server on port {port} ...\n'.format(port=port))
        httpd.serve_forever()

    except KeyboardInterrupt:
        print '\n \n You killed the server :('