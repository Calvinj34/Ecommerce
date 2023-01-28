from app import app
from flask import render_template, request, redirect, url_for
from .forms import AddtocartForm, SearchForm, loginForm, signupform
from .models import Product, User
from flask_login import current_user, login_required, logout_user, login_user
import requests
import os

@app.route('/')
def homePage():
    links = ['Home', 'Login', 'Signup', 'Products']
    return render_template('index.html', links = links, )

@app.route('/signup', methods=["GET", "POST"])
def signUpPage():
    form = signupform()
    print(request.method)
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            print(username, email, password)

            # add user to database
            user = User(username, email, password)
            print(user)

            user.saveToDB()

    return render_template('signup.html', form = form)    

@app.route('/login')
def loginPage():
    form = loginForm()
    if request.method == "Post":
        if form.validate():
            username = form.username.data
            password = form.password.data

            user = User.query.filter_by(username=username).first()
            if user:
                if user.password == password:
                    login_user(user)
                else:
                    print('wrong password')
            else:
                print('user does not exist')

    return render_template('login.html', form=form)


@app.route('/products', methods=["GET"])
def getProducts():
    cart = products.query.all()

    if request.method == "POST":
        # if loginForm.validate():
            url = "https://kohls.p.rapidapi.com/products/list"

            querystring = {"limit":"24","offset":"1","dimensionValueID":"AgeAppropriate:Teens"}

            headers = {
                "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
                "X-RapidAPI-Host": "kohls.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)
            return render_template('products.html') 
            # , html_form = loginForm,
   
    if current_user.is_authenticated:
        my_products = products.query.filter_by(user_id=current_user.id).all()
        products = {products.product_id for products in my_products}

        for products in cart:
            if products.id in cart:
                products = True
    
    return render_template('products.html', cart=cart)

@app.route('/products/delete', methods=["GET"])
@login_required
def deleteProducts(product_id):
    product = Product.query.get(product_id)
    if current_user.id != product.author.id:
        return redirect(url_for('products'))

    product.deleteFromDB()
    
    
    return redirect(url_for('Products'))

@app.route('/products', methods = ["GET", "POST"])
def productsPage():
    my_form = SearchForm()
    
    if request.method == "POST":
        if my_form.validate():
            rl = f'https://newsapi.org/v2/everything?q={search_term}&apiKey={NEWS_API_KEY}&pageSize=20'
            result = requests.get(url)

            data = result.json()
            
            articles = data['articles']
            return render_template('products.html', html_form = my_form, articles = articles)

    return render_template('products.html', html_form = my_form)