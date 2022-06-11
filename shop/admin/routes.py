from flask import render_template, session, redirect, request, url_for, flash
from shop import app, db
from .forms import RegistrationForm

@app.route("/")
def home():
    return "<p>Home page of shop</p>"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # user = User(form.username.data, form.email.data,
        #             form.password.data)
        # db_session.add(user)
        flash('Registration success!!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Registration')