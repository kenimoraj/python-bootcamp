from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def angela():
    return render_template("index.htm")

if __name__ == "__main__":
    app.run(debug=True)