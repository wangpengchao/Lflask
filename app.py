from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name

@app.route('/test')
def test_url_for():
    print(url_for('hello_world'))
    print(url_for('user_page', name='wpc'))
    print(url_for('user_page', name='ll'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'

if __name__ == '__main__':
    app.run()



