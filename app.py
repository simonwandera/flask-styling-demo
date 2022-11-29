from flask import Flask, jsonify, json, request, render_template, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@127.0.0.1/contact'
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import Blogs


# create a route for webhook
@app.route('/home', methods=['GET', 'POST'])
def webhook():
    

    blog = Blogs.query.all()
    return render_template("page.html", blogs = blog)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get("title")
    body = request.form.get("body")
    author = request.form.get("author")

    blog = Blogs(title = title, body=body, author = author)
    db.session.add(blog)
    db.session.commit()

    return redirect(url_for("webhook"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
