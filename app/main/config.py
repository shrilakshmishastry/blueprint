from flask import Blueprint
main = Blueprint('main',__name__)
@main.route('/main')
def hello():
    return "hello world"
