from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)


def json_reader(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


def csv_reader(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/products')
def reader():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error='Wrong source')

    data = []
    if source == 'json':
        data = json_reader('products.json')
    elif source == 'csv':
        data = csv_reader('products.csv')

    if product_id:
        filtered_data = [product for product in data if str(
            product['id']) == product_id]
        if not filtered_data:
            return render_template('product_display.html', error='Product not found')
        data = filtered_data

    return render_template('product_display.html', products=data)


@app.route('/items')
def items():
    with open("items.json") as file:
        data = json.load(file)
    item_list = data.get("items", [])
    return render_template('items.html', items=item_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
