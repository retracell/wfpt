from pt_app import app, db
from models import Price
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    prices = Price.query.filter_by(
        good_name = 'bread',
        location_name = 'syria').all()
    return render_template("index.html",
            prices = prices)

@app.route('/price')
def get_price():
    good = request.args.get('good', '')
    location = request.args.get('location', '')
    prices = Price.query.filter_by(
        good_name = good,
        location_name = location).all()
    return render_template("index.html",
        prices = prices)

