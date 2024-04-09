from flask import Flask # importing Flask class
app = Flask(__name__) #instantiated flask application

@app.route("/") # home page
@app.route("/home")
def home():
    return "<h2>Home page!</h2>"


@app.route('/about')
def about():
    return "<h2>About page!</h2>"


if __name__ == '__main__':
    app.run(debug=True)

