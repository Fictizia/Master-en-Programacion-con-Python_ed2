from jinja2 import Environment, FileSystemLoader, select_autoescape
from flask import Flask, request, jsonify


env = Environment(
    loader=FileSystemLoader('template')
    
)
title = 'A TITLE'
name = 'KAOS'
elements = ['alberto', 'silvia','gonzalo']


template = env.get_template('index.html')
my_html = template.render(title=title, name='KAOS', elements=elements)


app = Flask(__name__)

@app.route('/users', methods=['GET'])
def hello_world():
         
    if request.method == 'GET':
        return my_html

if __name__ == "__main__":
    app.run()