from flask import Flask, render_template
import markdown

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/posts/<path:path>",methods=['POST'])
def post(path):
    with open(f'posts/{path}.md','r') as file:
        content = file.read()
        html = markdown.markdown(content)
        return render_template('post.html',content=html)
