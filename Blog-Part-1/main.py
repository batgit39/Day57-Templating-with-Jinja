import requests
from flask import Flask, render_template

app = Flask(__name__)

def get_all_posts():
    blog_url = "https://api.npoint.io/504688570642f0a0370a"
    response = requests.get(blog_url)
    return response.json()
    
all_posts = get_all_posts()

@app.route('/')
def home():
    return render_template("index.html", posts = all_posts)

@app.route('/blog/<id>')
def get_blog(id):
    id = int(id)
    return render_template("post.html", post = all_posts[id-1])

if __name__ == "__main__":
    app.run(debug=True)
