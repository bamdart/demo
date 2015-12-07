from bottle import run, route


@route('/hello/<name>')
def hello(name):
        return 'Hello, <u>%s</u>' % name

run()