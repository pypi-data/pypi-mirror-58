"""Main module for pact_state_provider package."""
import http.server
import importlib
import json
import logging
import socketserver
from typing import Callable, Optional

import click

INVALID_CHARS = [' ', ',', ';', '{', '}', '(', ')', '\n', '\t', '=']
TRANS_TABLE = str.maketrans({k: '_' for k in INVALID_CHARS})


def import_state_func(base_module: str, state: str) -> Optional[Callable]:
    """Translate the state name to a function name and get it from the base module."""
    logging.debug(f'Importing {base_module}')
    try:
        pkg = importlib.import_module(base_module)
        func = getattr(pkg, state.lower().translate(TRANS_TABLE), None)
    except ModuleNotFoundError:
        return None
    return func


class StateProviderHandler(http.server.SimpleHTTPRequestHandler):
    """Handler to translate the request into a function and call it."""

    def __init__(self, request, client_address, server):
        """Store the servers base module for convenience."""
        self.base_module = server.base_module
        super().__init__(request, client_address, server)

    def do_POST(self):
        """Call the imported function based on the input dict."""
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        self.send_response(200)

        data = json.loads(self.data_string)
        consumer = data['consumer']
        state = data['state']

        state_func = import_state_func(self.base_module, state)
        if not state_func:
            logging.debug(f'No function {state} found in {self.base_module}')
            return
        logging.debug(f'Calling provider state')
        state_func(consumer)

        # prepare response
        self.send_head()  # pytype: disable=attribute-error


class StateProviderServer(socketserver.TCPServer):
    """TCPServer extended with the base module to load state providers from."""

    def __init__(self, server_address, bind_and_activate=True, base_module=''):
        """Store the provided base module on top of the TCPServer initialization."""
        # pytype: disable=wrong-arg-types
        super().__init__(
            server_address,
            StateProviderHandler,
            bind_and_activate
        )
        # pytype: enable=wrong-arg-types
        self.base_module = base_module


@click.command()
@click.option(
    '--base-module',
    default='pact_state_provider.example',
    help='Module containing the state providers.'
)
@click.option('--host', default='127.0.0.1', help='Host for the endpoint. Default: 127.0.0.1')
@click.option('--port', default=1235, help='Port for the endpoint. Default: 1235')
def pact_state_provider(base_module, host, port):
    """Start the state provider server on the specified host and port."""
    logging.info('start' + base_module)
    httpd = StateProviderServer((host, port), base_module=base_module)
    logging.info(
        f'Serving at {host}:{port}. Using module {base_module}'
    )
    httpd.serve_forever()
    httpd.shutdown()


if __name__ == '__main__':
    pact_state_provider()
