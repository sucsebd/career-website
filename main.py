from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p><h1 style=color:red>Dejan Chandra Gope!</h1></p>"

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)