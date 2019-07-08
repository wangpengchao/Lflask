from flask import Flask
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField()


@app.errorhandler(404)
def page_not_fount(e):
    return render_template('404.html'), 404


def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
    # response = make_response('<h1>hello world!!!!!</h1>')
    # response.set_cookie('answer', '42')
    # return response
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    # return '<h1>hello, {}!</h1>'.format(name)
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run()




