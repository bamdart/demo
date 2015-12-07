from bottle import run, route, template, static_file,view

@route('/')
@view ('static/index.html')
def index():
	post = [
		{
			'author':'bamdart'
			'message':'Hello,bottle.py'
		}
	]

	for i in range (10):
		posts.append({
			'author': 'User #%d' % (i + 100),
			'message': 'I Love Python. ' * (i + 1)
			})
	return {'posts':posts}


@route('/static/<filename:path>')
def static(filename):
	return static_file(filename, root='static')

run()