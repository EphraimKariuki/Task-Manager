from flask import Flask, render_template, requests, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#initialise database
db = SQLAlchemy(app)

class todo(db.Model):
    id = db.column(db.Integer, primary_key=True)
    content = db.column(db.String(200), nullable=False)
    completed = db.column(db.Integer, default=0)
    date_created = db.column(db.DateTime, datetime=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST''GET'])
def index():
    if request=='POST'
      task_content= request..form['content']
      new_task= todo(content=task_content)

      try:
          db.session.add(new_task)
          db.session.commit()
          return redirect('/')
      except:
          return 'There was an issue adding a string'
    else
      task= = todo.query.order_by(todo.date_dreated).all()
      return render_template("index.html", taks=tasks)



@app.route('/delete/<int:id>')
   def delete(id):
       task_to_delete = todo.query.get_or_delete(id)

       try:
           db.session.delete(task_to_delete)
           db.session.commmit()
           return redirect('/')
       except:
           return 'There was a problem deleting that task'


@app.route('/update/<int:id>')
   def delete(id):
       task = todo.query.get_or_404(id)

       if request.method == 'POST':
           task.content = request.form['content']

           try:
               db.session.commit()
               return redirect('/')
          except:
              return 'There was an issue updating your task'


       else:
          return render_template('update.html'task=task)



if __name__ == "__main__":
    app.run(debug = True)
