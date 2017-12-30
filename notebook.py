"""Used to output data (tables, charts, and text) to a web browser."""

import os
import time
import threading
import html
import uuid
import bokeh.embed
import pandas as pd
import traceback
from http.server import HTTPServer, BaseHTTPRequestHandler

class Notebook:
    _IP = '127.0.0.1'
    _PORT = 8314
    _STATIC_PATHS = {
        '/': 'html/notebook.html',
        '/notebook.js': 'html/notebook.js'
    }
    _DYNAMIC_PATH = '/dynamic.html'
    _OPEN_WEBPAGE_SECS = 0.2
    _FINAL_SHUTDOWN_SECS = 3.0

    def __init__(self):
        # load the template html and javasript
        self._static_resources = {}
        for http_path, resource_path in Notebook._STATIC_PATHS.items():
            with open(resource_path) as data:
                self._static_resources[http_path] = bytes(data.read(), 'utf-8')

        # This is the list of dynamic html elements.
        self._dynamic_elts = []

        # Number of elements transmitted via GET. (None means no GET received.)
        self._n_transmitted_elts = None

        # Create the webserver.
        class NotebookHandler(BaseHTTPRequestHandler):
            def do_GET(s):
                resource = self._get_resource(s.path)
                if resource == None:
                    s.send_error(404)
                else:
                    s.send_response(200)
                    s.end_headers()
                    s.wfile.write(resource)
        self._httpd = \
            HTTPServer((Notebook._IP, Notebook._PORT), NotebookHandler)

    def __enter__(self):
        # start the webserver
        threading.Thread(target=self._run_server).start()

        # if no gets received after a timeout, then launch the browser
        threading.Timer(Notebook._OPEN_WEBPAGE_SECS, self._open_webpage).start()

        # all done
        print(f'Started server at http://{Notebook._IP}:{Notebook._PORT}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Shut down the server."""
        # Display the stack trace if necessary.
        if exc_type != None:
            tb_list = traceback.format_list(traceback.extract_tb(exc_tb))
            print('tb_list')
            print('\n'.join(tb_list))
            self.alert('\n'.join(tb_list))

        # A small delay to flush anything left.
        time.sleep(Notebook._OPEN_WEBPAGE_SECS)

        # Delay server shutdown if we haven't transmitted everything yet
        if self._n_transmitted_elts != len(self._dynamic_elts):
            print(f'Sleeping for {Notebook._FINAL_SHUTDOWN_SECS} '
                'seconds to flush all elements.')
            time.sleep(Notebook._FINAL_SHUTDOWN_SECS)
        self._keep_running = False
        self._httpd.server_close()
        print('Closed down server.')

    def _run_server(self):
        self._keep_running = True
        while self._keep_running:
            self._httpd.handle_request()

    def _open_webpage(self):
        """Opens the webpage for this notebook using 'open' the command line."""
        if self._n_transmitted_elts == None:
            os.system(f'open http://{Notebook._IP}:{Notebook._PORT}')

    def _get_resource(self, path):
        """Returns a static / dynamic resource, or none if path is invalid."""
        if path in Notebook._STATIC_PATHS:
            return self._static_resources[path]
        elif path == Notebook._DYNAMIC_PATH:
            elts = '<div class="w-100"></div>'.join(
                f'<div class="col mb-2">{elt}</div>'
                    for elt in self._dynamic_elts)
            self._n_transmitted_elts = len(self._dynamic_elts)
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

    def text(self, *args):
        """Renders out plain text in a fixed width font."""
        self._wrap_args('samp', args)

    def header(self, *args):
        """Renders out text as an h4 header."""
        self._wrap_args('h4', args, classes=['mt-3'])

    def alert(self, *args):
        self._wrap_args('div', args, classes=['alert', 'alert-danger'])

    def plot(self, p):
        """Adds a Bokeh plot to the notebook."""
        plot_script, plot_html = bokeh.embed.components(p)
        self._dynamic_elts.append(plot_html + plot_script)

    def data(self, df):
        """Render a Pandas dataframe as html."""
        if type(df) != pd.DataFrame:
            df = pd.DataFrame(df)
        id = f'dataframe-{uuid.uuid4()}'
        pandas_table = '<table border="1" class="dataframe">'
        notebook_table = f'<table id="{id}">'
        table_html = df.to_html(bold_rows=False) \
            .replace(pandas_table, notebook_table)
        table_script = f'<script>notebook.styleDataFrame("{id}");</script>'
        self._dynamic_elts.append(table_html + table_script)
