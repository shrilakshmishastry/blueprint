from flask import Blueprint
admin = Blueprint('admin',__name__)
@admin.route('/admin')
def hello():
    return "hello world"
