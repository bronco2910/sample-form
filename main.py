from flask import Flask, render_template

app = Flask(__name__)

PRODUCTS=[
  {
    'id':1,
    'name':'Pressure Gauge'
  },
    {
    'id':2,
    'name':'Temperature Gauge'
  },
    {
    'id':3,
    'name':'Level Gauge'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', products=PRODUCTS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)