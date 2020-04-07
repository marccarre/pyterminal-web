import sys
import traceback
from StringIO import StringIO
from bottle import route, run, template, view, get, post, request

@get('/')
@post('/')
@view('index')
def index():
    reset = request.forms.get('reset', '').lower()
    if (reset == 'reset'): resetTerminal()

    command = request.forms.get('command', defaultCommand)
    output = runPython(command if (command.strip() != '') else defaultCommand)
    return dict(output=output)

@get('/sources')
@view('sources')
def sources():
    python = readSources('index.py')
    header = readSources('header.tpl')
    index = readSources('index.tpl')
    sources = readSources('sources.tpl')
    footer = readSources('footer.tpl')
    return dict(python=python,header=header,index=index,sources=sources,footer=footer)

defaultCommand = 'print(\'Welcome!\')'
hiddenContext = ('hiddenContext', 'resetTerminal', 'runPython', 'clean', 'precompile', 'execute', 'redirectOutputTo', 'readSources', 'index', 'sources', 'get', 'post', 'request', 'route', 'run', 'template', 'view', 'context', 'StringIO', '__doc__', '__file__', '__name__', '__package__', 'defaultCommand', 'history', 'sys', 'traceback')
context = {}
history = []

def resetTerminal():
    global context
    context = dict(globals().items() + locals().items())
    for hiddenEntry in hiddenContext:
        if hiddenEntry in context:
            del context[hiddenEntry]
    global history
    history = []

def runPython(command):
    buffer = StringIO()

    def clean(command):
        ''' Remove Windows-style line ending and make sure single-line expressions evaluate. '''
        return command.replace('\r\n', '\n') + '\n\n'

    @redirectOutputTo(buffer)
    def precompile(command):
        return compile(command, '<string>', 'single')

    @redirectOutputTo(buffer)
    def execute(command):
        exec(command) in context, context
        return

    execute(precompile(clean(command)))
    global history
    history += [(command, buffer.getvalue())]
    return history

class redirectOutputTo(object):
    def __init__(self, buffer):
        self.buffer = buffer

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            (out, err, sys.stdout, sys.stderr) = (sys.stdout, sys.stderr, self.buffer, self.buffer)
            try:
                return f(*args, **kwargs)
            except:
                self.buffer.write(traceback.format_exc())
            finally:
                (sys.stdout, sys.stderr) = (out, err)
        return wrapper

def readSources(filename):
    return ''.join(open(filename,'r').readlines())

run(host=sys.argv[1], port=sys.argv[2], debug=True)