from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html")

@app.route("/seelanfly")
def seelanfly():
   return "Hello, Seelanfly"

if __name__ == "__main__":
   app.run(debug=True)
