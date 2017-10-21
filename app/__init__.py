from flask import Flask
from app.admin.config import admin
from app.main.config import main
app=Flask(__name__)
@app.route('/')
def hello():
    return 'hello'
app.register_blueprint(admin)
app.register_blueprint(main)
