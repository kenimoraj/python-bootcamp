from flask import Flask, render_template
import requests

blog_posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
app = Flask(__name__)


@app.route("/")
def get_home():
    return render_template("index.html", blog_posts=blog_posts)

@app.route("/post/<int:post_id>")
def get_post(post_id):
    post = [p for p in blog_posts if p['id']==post_id][0]
    return render_template("post.html", post=post)
@app.route("/about")
def get_about():
    return render_template("about.html")

@app.route("/contact")
def get_contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
