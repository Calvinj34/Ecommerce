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


# @app.route('/products', methods=["GET"])
# def getProducts():
#     cart = Product.query.all()
#     html_form = AddtocartForm()

#     if request.method == "POST":
#         # if loginForm.validate():
#             url = "https://fakestoreapi.com/products"


          
#             response = requests.request("GET", url)

#             print(response.text)
#             return render_template('products.html') 
            
   
#     if current_user.is_authenticated:
#         my_products = products.query.filter_by(user_id=current_user.id).all()
#         products = {products.product_id for products in my_products}

#         for products in cart:
#             if products.id in cart:
#                 products = True
    
#     return render_template('products.html', cart=cart, html_form = html_form)

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
            url = 'https://fakestoreapi.com/products'
            result = requests.get(url)
            data = result.json()
            print (result.ok)
            if result.ok:
                data = result.json()
                items = data[0]['title']
                prices = data[0]['price']
                categories = data[0]['category']
                images = data[0]['image']
                
                purchase = Product(items, prices, categories, images)
                shop = {
                    'item': items,
                    'price': prices,
                    'category':categories,
                    'image': images,
                    }
                
            return render_template('products.html', html_form = my_form, shop = shop, purchase = purchase)

    return render_template('products.html', html_form = my_form)






# @app.route('/pokemon', methods=["GET","POST"])    
# def pokemon():
#     pokemon = Pokemon.query.all()
#     if current_user.is_authenticated:
#         my_pokemon = Catch.query.filter_by(user_id=current_user.id).all()
#         # pokemon = {pokemon.pokemon_id for pokemon in my_pokemon}
#         for p in my_pokemon:
#             print(p)
#             if p.id in pokemon:
#                 p.caught = True
#     form = pokemonform()
#     if request.method == 'POST':
#         pokeName = form.pokemon.data
#         pokemon = Pokemon.query.filter_by(name=pokeName).first()
#         print(pokemon)
        
#         if pokemon:
#             return render_template('pokemon.html', form = form, pokemon = pokemon)
#         url = 'https://pokeapi.co/api/v2/pokemon/'
#         response = requests.get(url + pokeName)
#         print (response)
#         print (response.ok)
#         if response.ok:
#             data = response.json()
#             names = data['forms'][0]['name']
#             abilities = data['abilities'][0]['ability']['name']
#             sprites = data['sprites']['front_shiny']
#             hp_stats = data['stats'][0]['base_stat']
#             attack_stats = data['stats'][1]['base_stat']
#             defense_stats = data['stats'][2]['base_stat']
#             moves = data['moves'][0]['move']['name']
#             pokemon=Pokemon(names, abilities, sprites, hp_stats, attack_stats, defense_stats, moves)
#             pokemon.saveToDB()
#             # pokemon = {
#             #     'name': names,
#             #     'ability': abilities,
#             #     'experience': experience,
#             #     'sprite': sprites,
#             #     'hp_stat': hp_stats,
#             #     'attack_stat': attack_stats,
#             #     'defense_stat': defense_stats,
#             #     'move': moves
#             # }
#             return render_template('pokemon.html', form = form, pokemon = pokemon)
#         # return(f'Pokemon:\nName: {names}, ability: {drivers}, base-experience: {experience}, sprite: {sprites}, and stats: {hp_stats}, {attack_stats}, {defense_stats}.')
#     return render_template('pokemon.html', form = form)
# # @app.route('/my_pokemon', methods=["GET"])
# # def caught():
    
# #      if len(my_pokemon) == 5:
# #             print('Stop')
# #     else:
# #         print(my_pokemon)
# # return render_template('my_pokemon.html')


#     # source <venv>/bin/activate