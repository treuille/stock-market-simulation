"""Used to output data (tables, charts, and text) to a web browser."""

import os
import time
import threading
import html
from http.server import HTTPServer, BaseHTTPRequestHandler

class Notebook:
    _IP = '127.0.0.1'
    _PORT = 8314
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

        # this is the list of dynamic html elements
        self._dynamic_elts = []

        # create the webserver
        class NotebookHandler(BaseHTTPRequestHandler):
            def do_GET(s):
                resource = self._get_resource(s.path)
                if resource == None:
                    s.send_error(404)
                else:
                    s.send_response(200)
                    s.send_header("Content-type", "text/html")
                    s.end_headers()
                    s.wfile.write(resource)
        self._httpd = \
            HTTPServer((Notebook._IP, Notebook._PORT), NotebookHandler)

    def __enter__(self):
        # run the webserver and display the results
        threading.Thread(target=self._run_server).start()
        print('Started server at http://%s:%s' % (Notebook._IP, Notebook._PORT))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Destructor closes down the webserver."""
        self._keep_running = False
        time.sleep(Notebook._FINAL_SHUTDOWN_SECONDS)
        self._httpd.server_close()
        print('Closed down server.')

    def _run_server(self):
        self._keep_running = True
        while self._keep_running:
            self._httpd.handle_request()

    def _get_resource(self, path):
        """Returns a static / dynamic resource, or none if path is invalid."""
        if path in Notebook._STATIC_PATHS:
            return self._static_resources[path]
        elif path == Notebook._DYNAMIC_PATH:
            return bytes('<div class="w-100"></div>'.join(
                f'<div class="col mb-2">{elt}</div>'
                    for elt in self._dynamic_elts), 'utf-8')
        else:
            return None

    def _wrap_args(self, tag, args, classes=[]):
        """Esacapes and wraps the text in an html tag."""
        escaped_text = html.escape(' '.join(str(arg) for arg in args)) \
            .replace('\n', '<br/>')
        tag_class = ''
        if classes:
            tag_class = ' class="%s"' % ' '.join(classes)
        self._dynamic_elts.append(
            f'<{tag}{tag_class}>{escaped_text}<{tag}>')

    def text(self, *args):
        """Renders out plain text in a fixed width font."""
        self._wrap_args('samp', args)

    def header(self, *args):
        """Renders out text as an h4 header."""
        # self._wrap_args('div', '\n')
        self._wrap_args('h4', args, classes=['mt-3'])
