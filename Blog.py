import os
from flask import Flask, render_template
import markdown

app = Flask(__name__)

@app.route('/')
def home():
    posts = []
    for file in os.listdir('posts'):
        if file.endswith('.md'):
            title = file[:-3]
            posts.append(title)
    return render_template('index.html',posts=posts)

@app.route("/posts/<path:path>",methods=['POST','GET'])
def post(path):
    with open(f'posts/{path}.md','r',encoding='utf-8') as file:
        content = file.read()
        title = path
        html = markdown.markdown(content)
        return render_template('post.html',content=html,title=title)


if __name__ == '__main__':
    app.run(debug=True)