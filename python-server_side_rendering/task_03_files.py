from flask import Flask, render_template, request
import json
import csv

# Initialize Flask app
app = Flask(__name__)

# Example function to load JSON data
def load_json_data():
    with open("products.json", "r") as file:
        return json.load(file)

# Example function to load CSV data
def load_csv_data():
    products = []
    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products

# Route to display products
@app.route("/products")
def display_products():
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)
    products = []
    error_message = None

    # Check if the source is valid
    if source == "json":
        try:
            products = load_json_data()
        except Exception:
            error_message = "Error loading JSON data."
    elif source == "csv":
        try:
            products = load_csv_data()
        except Exception:
            error_message = "Error loading CSV data."
    else:
        error_message = "Wrong source. Please choose either 'json' or 'csv'."

    # If an id is provided, filter by id
    if product_id and not error_message:
        products = [p for p in products if p["id"] == product_id]
        if not products:
            error_message = "Product not found."

    return render_template("product_display.html", products=products, error_message=error_message)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
