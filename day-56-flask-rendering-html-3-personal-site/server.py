from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.htm")

@app.route("/<subsite>")
def sub(subsite):
    return render_template(f"{subsite}.htm")


if __name__ == "__main__":
    app.run(debug=True)