from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db.init_app(app)
migrate = Migrate(app, db)

#                           _          _       
#                          | |        | |      
#   _ __ ___     ___     __| |   ___  | |  ___ 
#  | '_ ` _ \   / _ \   / _` |  / _ \ | | / __|
#  | | | | | | | (_) | | (_| | |  __/ | | \__ \
#  |_| |_| |_|  \___/   \__,_|  \___| |_| |___/
# 

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref='posts')

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

#                  _            
#                 | |           
#  _ __ ___  _   _| |_ ___  ___ 
# | '__/ _ \| | | | __/ _ \/ __|
# | | | (_) | |_| | ||  __/\__ \
# |_|  \___/ \__,_|\__\___||___/
# 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/blog')
def blog():
    return 'List of blog posts'

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    return f'Blog post {post_id}'

