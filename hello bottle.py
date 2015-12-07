from bottle import run, route,template

@route('/')
def index():
        return template('static/index.html')
        
run()