from flask import Flask, render_template# importing Flask class
app = Flask(__name__) #instantiated flask application

posts = [
    {
        'author': 'Sam Wanyua',
        'title': 'The new Earth',
        'content': 'Have you had the new earth that is coming',
        'date-posted': 'April 20, 2023'
    },
    {
        'author': 'Jetlifer Ikioe',
        'title': 'The arise of Cybertrucks',
        'content': '$3453 new cybertrucks',
        'date-posted': 'June 20, 2023'
    }
]

@app.route("/") # home page
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)

