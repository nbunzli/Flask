from flask import Flask
from flask import request

app = Flask(__name__)

# Test endpoint, can be used to check if the service is up.
@app.route('/')
def test_endpoint() -> str:
	return 'Hello, this is the test endpoint!'

# Adds two ints, passed as url params.
# Returns the equation as a string.
# Example request: /sum?a=2&b=5
# Example return: "2 + 5 = 7"
@app.route('/sum')
def sum() -> str:
	a = request.args.get('a', default = 0, type = int)
	b = request.args.get('b', default = 0, type = int)
	return f'{a} + {b} = {a + b}'
