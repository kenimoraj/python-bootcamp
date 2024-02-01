from flask import Flask, render_template, url_for
import random
from datetime import datetime
import requests
app = Flask(__name__)

@app.route("/")
def index():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    return render_template("index.htm", num=random_number, cr_year=year)


@app.route("/guess/<name>")
def name_guessing(name):
    #Genderize API call
    gender_resp = requests.get(url=f"https://api.genderize.io?name={name}")
    gender = gender_resp.json()["gender"]
    if gender is None:
        gender = "[Unknown]"
    #Agify API call
    age_resp = requests.get(url=f"https://api.agify.io?name={name}")
    age = age_resp.json()["age"]
    if age is None:
        age = "[Unknown]"
    #Return HTML


    return render_template("name_guessing.htm", name=name, gender=gender, age=age)


@ app.route("/blog/<int:num>")
def get_blog(num):
    print(num)
    blog_posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.htm", blog_posts=blog_posts)


if __name__ == "__main__":
    app.run(debug=True)