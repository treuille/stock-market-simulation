"""Used to output data (tables, charts, and text) to a web browser."""

import os
import time
import threading
import html
import uuid
from bokeh.embed import components as bokeh_components
from http.server import HTTPServer, BaseHTTPRequestHandler

class Notebook:
    _IP = '127.0.0.1'
    _PORT = 8314
    _STATIC_PATHS = {
        '/': 'html/notebook.html',
        '/notebook.js': 'html/notebook.js'
    }
    _DYNAMIC_PATH = '/dynamic.html'
    _OPEN_WEBPAGE_SECONDS = 1
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
        # run the webserver
        threading.Thread(target=self._run_server).start()
        print(f'Started server at http://{Notebook._IP}:{Notebook._PORT}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Shut down the server."""
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
            elts = '<div class="w-100"></div>'.join(
                f'<div class="col mb-2">{elt}</div>'
                    for elt in self._dynamic_elts)
            # scroll_to_bottom = '<script>notebook.scroll_to_bottom()</script>'
            # return bytes(f'{elts}{scroll_to_bottom}', 'utf-8')
            return bytes(elts, 'utf-8')
        else:
            return None

    def _wrap_args(self, tag, args, classes=[]):
        """Esacapes and wraps the text in an html tag."""
        escaped_text = html.escape(' '.join(str(arg) for arg in args)) \
            .replace(' ', '&nbsp;').replace('\n', '<br/>')
        tag_class = ''
        if classes:
            tag_class = ' class="%s"' % ' '.join(classes)
        self._dynamic_elts.append(
            f'<{tag}{tag_class}>{escaped_text}<{tag}>')

    def open_webpage(self):
        """Opens the webpage for this notebook using 'open' the command line."""
        os.system(f'open http://{Notebook._IP}:{Notebook._PORT}')
        time.sleep(Notebook._OPEN_WEBPAGE_SECONDS)

    def text(self, *args):
        """Renders out plain text in a fixed width font."""
        self._wrap_args('samp', args)

    def header(self, *args):
        """Renders out text as an h4 header."""
        # self._wrap_args('div', '\n')
        self._wrap_args('h4', args, classes=['mt-3'])

    def plot(self, p):
        """Adds a Bokeh plot to the notebook."""
        self._dynamic_elts.append('\n'.join(bokeh_components(p)))

    def data_frame(self, df):
        """Render a Pandas dataframe as html."""
        id = f'dataframe-{uuid.uuid4()}'
        pandas_table = '<table border="1" class="dataframe">'
        notebook_table = f'<table id="{id}">'
        table_html = df.to_html(bold_rows=False) \
            .replace(pandas_table, notebook_table)
        table_script = f'<script>notebook.style_data_frame("{id}");</script>'
        self._dynamic_elts.append(f'{table_html}\n{table_script}')
