from flask import Flask, render_template, request, redirect, url_for
from models import db, User
from forms import UsersForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5433/usersdb'
db.init_app(app)

app.secret_key = "e14a-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():

    form = UsersForm()
    if request.method == 'GET':
        return render_template('add_user.html', form=form)
    else:
        if form.validate_on_submit():
            first_name = request.form['first_name']
            age = request.form['age']
            new_user = User(first_name=first_name, age=age)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))

@app.route('/read')
def show_user():
    users = User.query.all()
    return render_template('read.html', users=users)

@app.route('/delete-user/<int:user_id>')
def delete_user(user_id):
    userToDelete = db.session.query(User).filter_by(user_id=user_id).first()
    db.session.delete(userToDelete)
    db.session.commit()
    return redirect(url_for('show_user'))






		









if __name__ == "__main__":
  app.run(debug=True)
