"""Used to output data (tables, charts, and text) to a web browser."""

import os
import time
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

class Notebook:
    _PORT = 8314
    # _STATIC_ROOT = 'html'
    _STATIC_PATHS = {
        '/': 'html/notebook.html',
        '/notebook.js': 'html/notebook.js'
    }
    _DYNAMIC_PATH = '/dynamic.html'
    _FINAL_SHUTDOWN_SECONDS = 1

    def __init__(self):
        # load the template html
        self._static_resources = {}
        for http_path, resource_path in Notebook._STATIC_PATHS.items():
            with open(resource_path) as data:
                self._static_resources[http_path] = bytes(data.read(), 'utf-8')

        # create the webserver
        class NotebookHandler(BaseHTTPRequestHandler):
            def do_GET(s):
                print('do_GET:', s.path)
                resource = self._get_resource(s.path)
                if resource == None:
                    print('Failing', s.path)
                    s.send_error(404)
                else:
                    print('Returning sucessfully', s.path)
                    print(resource)
                    s.send_response(200)
                    s.send_header("Content-type", "text/html")
                    s.end_headers()
                    s.wfile.write(resource)
        self._httpd = \
            HTTPServer(("127.0.0.1", Notebook._PORT), NotebookHandler)

    def __enter__(self):
        print('Created server', id(self._httpd))

        # run the webserver and display the results
        threading.Thread(target=self._run_server).start()
        # threading.Thread(target=self.httpd.serve_forever).start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Destructor closes down the webserver."""
        self._keep_running = False
        print('Closing the notepad.')
        print('exc_type', exc_type)
        print('exc_val', exc_val)
        print('exc_tb', exc_tb)
        # self._httpd.shutdown()
        print('About to start sleeping.')
        time.sleep(Notebook._FINAL_SHUTDOWN_SECONDS)
        print('Finished sleeping.')
        self._httpd.server_close()
        print('The server is closed.')

    def _run_server(self):
        self._keep_running = True
        print('About to start the server.')
        while self._keep_running:
            self._httpd.handle_request()
        print('The server shutdown naturally.')

    def _get_resource(self, path):
        """Returns a static / dynamic resource, or none if path is invalid."""
        if path in Notebook._STATIC_PATHS:
            return self._static_resources[path]
        elif path == Notebook._DYNAMIC_PATH:
            return bytes('Not yet implemented!', 'utf-8')
        else:
            return None
