from flask import Flask, render_template
from flask_sqlalchemy import sqlalchemy
from datetime import datetime

app = Flask(__name__)

#configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#initialise database
db = SQLALCHEMY(app)

class todo(db.model):
    id = db.column(db.integer, primary_key=True)
    content = db.column(db.string(200), nullable=flase)
    completed = db.column(db.integer, defult=0)
    date_created = db.column(db.datetime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
