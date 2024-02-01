import requests
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():

    blog_data = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_posts = blog_data.json()

    return render_template("index.html", posts=blog_posts)

@app.route("/post/<int:post_id>")
def get_post(post_id):

    blog_data = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_post = [post for post in blog_data.json() if post["id"] == post_id][0]
    print(blog_post)
    return render_template("post.html", post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
