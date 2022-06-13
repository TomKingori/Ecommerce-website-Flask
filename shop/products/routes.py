from optparse import TitledHelpFormatter
from flask import redirect, render_template, url_for, flash, request, session
from shop import db, app
from .models import Brand, Category
from .forms import Addproducts
import secrets


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
   if 'email' not in session:
      flash('Please log in first', category="error")
      return redirect(url_for('login'))
   if request.method == 'POST':
      getbrand = request.form.get('brand')
      brand = Brand(name=getbrand)
      db.session.add(brand)
      flash(f'The Brand {getbrand} was added to your database!', category='success')
      db.session.commit()
      return redirect(url_for('addbrand'))

   return render_template('products/addbrand.html', brands='brands')

@app.route('/updatebrand/<int:id>',methods=['GET','POST'])
def updatebrand(id):
   if 'email' not in session:
      flash('Login first please', category="error")
      return redirect(url_for('login'))
   updatebrand = Brand.query.get_or_404(id)
   brand = request.form.get('brand')
   if request.method =="POST":
      updatebrand.name = brand
      flash(f'The brand {updatebrand.name} was changed to {brand}','success')
      db.session.commit()
      return redirect(url_for('brands'))
   brand = updatebrand.name
   return render_template('products/addbrand.html', title='Update brand', rands='brands',updatebrand=updatebrand)


@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
   if 'email' not in session:
      flash('Please log in first', category="error")
      return redirect(url_for('login'))
   if request.method == 'POST':
      getcat = request.form.get('category')
      cat = Category(name=getcat)
      db.session.add(cat)
      flash(f'The Category {getcat} was added to your database!', category='success')
      db.session.commit()
      return redirect(url_for('addcat'))

   return render_template('products/addbrand.html')

@app.route('/updatecat/<int:id>',methods=['GET','POST'])
def updatecat(id):
    if 'email' not in session:
        flash('Login first please', category="error")
        return redirect(url_for('login'))
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')  
    if request.method =="POST":
        updatecat.name = category
        flash(f'The category {updatecat.name} was changed to {category}','success')
        db.session.commit()
        return redirect(url_for('categories'))
    category = updatecat.name
    return render_template('products/addbrand.html', title='Update Category', updatecat=updatecat)

@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
   form = Addproducts(request.form)
   return render_template('products/addproduct.html', title='Add Product', form=form)