from flask import Flask, render_template, request
import os

app = Flask(__name__)

# -------------------- HOME --------------------

@app.route('/')
def home():
    return render_template('index.html')


# -------------------- MENU PAGES --------------------

@app.route('/veg')
def veg():
    return render_template('veg.html')


@app.route('/nonveg')
def nonveg():
    return render_template('nonveg.html')


# -------------------- CHECKOUT PAGE --------------------

@app.route('/checkout')
def checkout():
    food_item = request.args.get("food")
    return render_template('checkout.html', food=food_item)


# -------------------- PLACE ORDER --------------------

@app.route('/place_order', methods=['POST'])
def place_order():
    name = request.form.get("name")
    address = request.form.get("address")
    food_item = request.form.get("food")

    return f"""
    <h2>Order Placed Successfully!</h2>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Food Item:</strong> {food_item}</p>
    <p><strong>Address:</strong> {address}</p>
    <a href="/">Go Back Home</a>
    """


# -------------------- RUN APP --------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
