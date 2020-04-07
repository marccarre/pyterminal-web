#!/usr/bin/env python
import sys
import traceback
from io import StringIO
from bottle import route, run, template, view, get, post, request


@get('/')
@post('/')
@view('index')
def index():
    reset = request.forms.get('reset', '').lower()
    if reset == 'reset':
        reset_terminal()
    command = request.forms.get('command', DEFAULT_COMMAND)
    return {
        'output': run_python(command if command.strip() else DEFAULT_COMMAND),
    }


@get('/sources')
@view('sources')
def sources():
    return {
        'python': read_sources('index.py'),
        'header': read_sources('header.tpl'),
        'index': read_sources('index.tpl'),
        'sources': read_sources('sources.tpl'),
        'footer': read_sources('footer.tpl'),
    }


DEFAULT_COMMAND = 'print(\'Welcome!\')'
HIDDEN_CONTEXT = (
    'CONTEXT',
    'DEFAULT_COMMAND',
    'HIDDEN_CONTEXT',
    'HISTORY',
    'StringIO',
    '__doc__',
    '__file__',
    '__name__',
    '__package__',
    'clean',
    'execute',
    'get',
    'index',
    'post',
    'precompile',
    'read_sources',
    'redirect_output_to',
    'request',
    'reset_terminal',
    'route',
    'run',
    'run_python',
    'sources',
    'sys',
    'template',
    'traceback',
    'view',
)
CONTEXT = {}
HISTORY = []


def reset_terminal():
    global CONTEXT
    CONTEXT = {**globals(), **locals()}
    for hiddenEntry in HIDDEN_CONTEXT:
        if hiddenEntry in CONTEXT:
            del CONTEXT[hiddenEntry]
    global HISTORY
    HISTORY = []


def run_python(command):
    buffer = StringIO()

    def clean(command):
        ''' Remove Windows-style line ending and make sure single-line expressions evaluate. '''
        return command.replace('\r\n', '\n') + '\n\n'

    @redirect_output_to(buffer)
    def precompile(command):
        return compile(command, '<string>', 'single')

    @redirect_output_to(buffer)
    def execute(command):
        exec(command, CONTEXT)
        return

    execute(precompile(clean(command)))
    global HISTORY
    HISTORY += [(command, buffer.getvalue())]
    return HISTORY


class redirect_output_to:
    def __init__(self, buffer):
        self.buffer = buffer

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            out, err, sys.stdout, sys.stderr = sys.stdout, sys.stderr, self.buffer, self.buffer
            try:
                return f(*args, **kwargs)
            except:
                self.buffer.write(traceback.format_exc())
            finally:
                sys.stdout, sys.stderr = out, err
        return wrapper


def read_sources(filename):
    return ''.join(open(filename, 'r').readlines())


run(host=sys.argv[1], port=sys.argv[2], debug=True)
