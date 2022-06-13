from flask import redirect, render_template, url_for, flash, request, session
from shop import db, app
from .models import Brand, Category
from .forms import Addproducts
import secrets


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
   if request.method == 'POST':
      getbrand = request.form.get('brand')
      brand = Brand(name=getbrand)
      db.session.add(brand)
      flash(f'The Brand {getbrand} was added to your database!', category='success')
      db.session.commit()
      return redirect(url_for('addbrand'))

   return render_template('products/addbrand.html', brands='brands')


@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
   if request.method == 'POST':
      getcat = request.form.get('category')
      category = Category(name=getcat)
      db.session.add(category)
      flash(f'The Category {getcat} was added to your database!', category='success')
      db.session.commit()
      return redirect(url_for('addcat'))

   return render_template('products/addbrand.html')



@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
   brands = Brand.query.all()
   categories = Category.query.all()
   form = Addproducts(request.form)
   return render_template('products/addproduct.html', title='Add Product', form=form, brands=brands, categories=categories)