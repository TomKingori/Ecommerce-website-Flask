from flask import render_template, session, redirect, request, url_for, flash
from matplotlib.pyplot import title
from shop import app, db, bcrypt
from .forms import RegistrationForm
from .models import User

@app.route("/")
def home():
    return render_template('index.html', title='Admin Page')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)

        user = User(name=form.name.data, 
                    username=form.username.data, 
                    email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Thanks for registering {form.name.data}!!', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form, title='Registration')