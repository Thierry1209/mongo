from flask import Flask
from flask import render_template
from flask import request
from model import pizza
from model import chicken
from model import burger
from model import apple
from model import orange
from model import bannana
from model import potato
from model import broccoli
from model import carrot
from flask_pymongo import PyMongo





app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'HCHEATS'
app.config['MONGO_URI'] = 'mongodb+srv://Thierry:Smartypants1209@cluster0.vahci.mongodb.net/HCHEATS?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/bag', methods=['GET', 'POST'])
def bag():
    if request.method == 'POST':
        print(request.form)
        user_pizza = request.form['pizza']
        user_chicken = request.form['chicken']
        user_burger = request.form['burger']
        user_broccoli = request.form['broccoli']
        user_carrot = request.form['carrot']
        user_potato = request.form['potato']
        user_apple = request.form['apple']
        user_bannana = request.form['bannana']
        user_orange = request.form['orange']
        pizzas = pizza(user_pizza)
        chickens = chicken(user_chicken)
        burgers = burger(user_burger)
        broccolis = broccoli(user_broccoli)
        carrots = carrot(user_carrot)
        potatoes = potato(user_potato)
        apples = apple(user_apple)
        bannanas = bannana(user_bannana)
        oranges = orange(user_orange)
        items = [float(user_bannana) * float('1.49'), float(user_orange) * float('0.99'), float(user_broccoli) * float('0.99'), float(user_apple) * float('0.99'), float(user_carrot)
                 * float('0.99'), float(user_potato) * float('1.49'), float(user_chicken) * float('8.99'), float(user_burger) * float('6.99'), float(user_pizza) * float('3.99')]

        total_price = sum(items)
        print(total_price)

        return render_template('bag.html', user_pizza=user_pizza, user_chicken=user_chicken, user_burger=user_burger,
                               user_carrot=user_carrot, user_potato=user_potato, user_apple=user_apple, user_bannana=user_bannana, user_orange=user_orange, user_broccoli=user_broccoli,
                               pizzas=pizzas, chickens=chickens, burgers=burgers, broccolis=broccolis, carrots=carrots, potatoes=potatoes, apples=apples, oranges=oranges, bannanas=bannanas, total_price=total_price, items=items)
    else:
        return 'You have nothing in the bag'


# def add():
#     order = mongo.db.HCHEATS.orders
#     user_pizza = request.form['pizza']
#     user_chicken = request.form['chicken']
#     user_burger = request.form['burger']
#     user_broccoli = request.form['broccoli']
#     user_carrot = request.form['carrot']
#     user_potato = request.form['potato']
#     user_apple = request.form['apple']
#     user_bannana = request.form['bannana']
#     user_orange = request.form['orange']
    # orders.insert({'pizza': user_pizza, 'chicken': user_chicken, 'burger': user_burger, 'broccoli': user_broccoli,
    #               'carrot': user_carrot, 'potato': user_potato, 'apple': user_apple, 'bannana': user_bannana, 'orange': user_orange})
    # return "Order Sent"

    # orders = order.find({'pizza', 'chicken', 'burger', 'apple',
    #                     'orange', 'bannana', 'broccoli', 'carrot', 'potato'})


@app.route('/order')
def vegetables():
    return render_template('order.html')

