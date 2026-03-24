from flask import Flask, render_template
import requests

app = Flask(__name__)
blogs = []

def fetch_blogs():
    global blogs
    if not blogs: 
        response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
        blogs = response.json()

@app.route('/', methods=["GET"])
def home():
    fetch_blogs()
    return render_template("index.html", blogs=blogs)

@app.route("/blogs/<int:id>", methods=["GET"])
def get_blog(id):
    fetch_blogs() 
    blog = next((b for b in blogs if b["id"] == id), None)
    if blog is None:
        return "Blog not found", 404
    return render_template("post.html", blog=blog)

if __name__ == "__main__":
    app.run(debug=True)