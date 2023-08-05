import logging
import datetime
from functools import partial
from .client import DrHTTPClient

#https://www.python.org/dev/peps/pep-0333/#middleware-components-that-play-both-sides
"""
    TODO
    Make sure last record is sent when server is shut down
    set content-length in response headers if not set by app
    handle exception
    catch correctly 5xx status codes
    get datetime from request header
    thread safety
"""


class WSGIMiddleware:
    # idenfify is a function that takes request headers as a single parameter
    # and returns a string identifying the user issuing the request
    def __init__(self, app, dsn, identify=None):
        self.app = app
        self.client = DrHTTPClient(dsn=dsn)
        self.identify = identify

    def __call__(self, environ, start_response):
        # Extract request infos
        request_body_size = 0
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except ValueError:
            pass

        self.request = {
            'datetime': datetime.datetime.now(),
            'method': environ['REQUEST_METHOD'],
            'url': self.reconstruct_url(environ),
            'headers': {self.format_header_name(k): v for k,v in environ.items() if k.startswith('HTTP_')},
            'data': bytearray(),
            'length': request_body_size
        }
        
        if self.identify:
            self.request['user'] = self.identify(self.request['headers'])

        ## Request body capture
        self.wsgi_input = environ['wsgi.input'] = ReadableProxy(environ['wsgi.input'], self.on_request_data_read)

        # Extract response infos
        self.response = {
            'status_code': 0,
            'headers': {},
            'data': bytearray()
        }

        ## Capture response
        try:
            app_response_iteratable = self.app(environ, self.captured_start_response(start_response))
        except Exception as exception:
            self.on_app_exception(exception)
            raise exception
        return IteratableProxy(app_response_iteratable, self.on_response_data_iterated, self.on_response_data_end) 
        
    def captured_start_response(self, start_response):
        def captured(status, headers, exc_info=None):
            self.response['status_code'] = int(status.split()[0])
            self.response['headers'] = {k: v for k, v in headers}
            return start_response(status, headers, exc_info)
        return captured

    def on_request_data_read(self, data):
        self.request['data'].extend(data)

    def on_response_data_iterated(self, data):
        self.response['data'].extend(data)

    def on_response_data_end(self):
        self.send_record()

    def on_app_exception(self, exception):
        self.response['status_code'] = 500
        self.send_record()

    def send_record(self):
        # Make sure request body has been read
        self.wsgi_input.read(self.request['length'] - len(self.request['data']))

        self.client.record(self.request['datetime'], self.request.get('user'),
            self.request['method'], self.request['url'], self.request['headers'], self.request['data'],
            self.response['status_code'], self.response['headers'], self.response['data'])

    def reconstruct_url(self, environ):
        from urllib.parse import quote
        url = environ['wsgi.url_scheme']+'://'

        if environ.get('HTTP_HOST'):
            url += environ['HTTP_HOST']
        else:
            url += environ['SERVER_NAME']

            if environ['wsgi.url_scheme'] == 'https':
                if environ['SERVER_PORT'] != '443':
                    url += ':' + environ['SERVER_PORT']
            else:
                if environ['SERVER_PORT'] != '80':
                    url += ':' + environ['SERVER_PORT']

        url += quote(environ.get('SCRIPT_NAME', ''))
        url += quote(environ.get('PATH_INFO', ''))
        if environ.get('QUERY_STRING'):
            url += '?' + environ['QUERY_STRING']
        return url

    def format_header_name(self, header):
        prefix = 'HTTP_'
        if header.startswith(prefix):
            header = header[len(prefix):]
        header = header.replace('_', '-')
        header = header.capitalize()
        return header

class ReadableProxy:
    """
        This class proxies a readable file-like object and calls callback
        each time the proxied object is read
        read_callback takes an argument : the bytes being read
    """
    def __init__(self, proxied, read_callback):
        self.proxied = proxied
        self.read_callback = read_callback
    
    def __getattr__(self, name):
        if name in ['read', 'readline', 'readlines']:
            return getattr(self, name)
        else:
            return getattr(self.proxied, name)

    def read(self, *args, **kwargs):
        return self.proxied_method('read', *args, **kwargs)

    def readline(self, *args, **kwargs):
        return self.proxied_method('readline', *args, **kwargs)

    def readlines(self, *args, **kwargs):
        return self.proxied_method('readlines', *args, **kwargs)

    def proxied_method(self, method_name, *args, **kwargs):
        method = getattr(self.proxied, method_name)
        data = method(*args, **kwargs)
        if method_name == 'readlines':
            for d in data:
                self.read_callback(d)
        else:
            self.read_callback(data)
        return data
        
class IteratableProxy:
    """
        This class proxies a iteratable object and calls callback
        each time the proxied object is iterated
        iterated_callback takes an argument : the data being returned by iteration
        iteration_ended_callback take no argument
    """
    def __init__(self, proxied, iterated_callback, iteration_ended_callback):
        self.proxied = iter(proxied)
        self.iterated_callback = iterated_callback
        self.iteration_ended_callback = iteration_ended_callback

    def __iter__(self):
        return self

    def __next__(self):
        try:
            data = next(self.proxied)
            self.iterated_callback(data)
            return data
        except StopIteration as exception:
            self.iteration_ended_callback()
            raise exception