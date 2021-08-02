from flask import Flask
from flask import render_template
from flask import request
from model import onion
from model import sprout
from model import kale
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
        user_onion = request.form['onion']
        user_kale = request.form['kale']
        user_sprout = request.form['sprout']
        user_broccoli = request.form['broccoli']
        user_carrot = request.form['carrot']
        user_potato = request.form['potato']
        user_apple = request.form['apple']
        user_bannana = request.form['bannana']
        user_orange = request.form['orange']
        onions = onion(user_onion)
        kales = kale(user_kale)
        sprouts = sprout(user_sprout)
        broccolis = broccoli(user_broccoli)
        carrots = carrot(user_carrot)
        potatoes = potato(user_potato)
        apples = apple(user_apple)
        bannanas = bannana(user_bannana)
        oranges = orange(user_orange)
        items = [float(user_bannana) * float('1.49'), float(user_orange) * float('1.99'), float(user_broccoli) * float('1.99'), float(user_apple) * float('1.99'), float(user_carrot)
                 * float('1.99'), float(user_potato) * float('1.49'), float(user_sprout) * float('1.99'), float(user_kale) * float('1.99'), float(user_onion) * float('1.99')]

        total_price = round(sum(items),2)
        print(total_price)

        return render_template('bag.html', user_onion=user_onion, user_kale=user_kale, user_sprout=user_sprout,
                               user_carrot=user_carrot, user_potato=user_potato, user_apple=user_apple, user_bannana=user_bannana, user_orange=user_orange, user_broccoli=user_broccoli,
                               onions=onions, kales=kales, sprouts=sprouts, broccolis=broccolis, carrots=carrots, potatoes=potatoes, apples=apples, oranges=oranges, bannanas=bannanas, total_price=total_price, items=items)
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
    # return Order Sent

    # orders = order.find({'pizza', 'chicken', 'burger', 'apple',
    #                     'orange', 'bannana', 'broccoli', 'carrot', 'potato'})


@app.route('/order')
def vegetables():
    return render_template('order.html')

@app.route('/sign')
def sign():
    return render_template('sign.html')

