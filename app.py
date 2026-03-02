from flask import Flask, render_template, request
import os
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/veg')
def veg():
    return render_template('veg.html')


@app.route('/nonveg')
def nonveg():
    return render_template('nonveg.html')


@app.route('/checkout', methods=['POST'])
def checkout():
    item = request.form.get('item')
    price = int(request.form.get('price'))
    quantity = int(request.form.get('quantity'))

    total = price * quantity

    return render_template(
        'checkout.html',
        item=item,
        price=price,
        quantity=quantity,
        total=total
    )


@app.route('/order', methods=['POST'])
def order():
    name = request.form.get('name')
    phone = request.form.get('phone')
    address = request.form.get('address')
    item = request.form.get('item')
    quantity = request.form.get('quantity')
    total = request.form.get('total')

    message = f"""
New Order Received

Item: {item}
Quantity: {quantity}
Total: ₹{total}

Customer: {name}
Phone: {phone}
Address: {address}
"""

    sender = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASS")

    msg = MIMEText(message)
    msg['Subject'] = "New Order - Zaika Dhaba"
    msg['From'] = sender
    msg['To'] = sender

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender, password)
    server.sendmail(sender, sender, msg.as_string())
    server.quit()

    return "<h2>Order Placed Successfully!</h2>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)    name = request.form.get("name")
    phone = request.form.get("phone")
    address = request.form.get("address")
    item = request.form.get("item")
    quantity = request.form.get("quantity")
    total = request.form.get("total")

    sender = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASS")

    message = f"""
New Order Received

Item: {item}
Quantity: {quantity}
Total: ₹{total}

Customer: {name}
Phone: {phone}
Address: {address}
"""

    msg = MIMEText(message)
    msg["Subject"] = "New Order - Zaika Dhaba"
    msg["From"] = sender
    msg["To"] = sender

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender, password)
    server.sendmail(sender, sender, msg.as_string())
    server.quit()

    return "<h2>Order Placed Successfully!</h2>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)    name = request.form['name']
    phone = request.form['phone']
    address = request.form['address']
    item = request.form['item']
    quantity = request.form['quantity']
    total = request.form['total']

    message = f"""
    New Order Received

    Item: {item}
    Quantity: {quantity}
    Total: ₹{total}

    Customer: {name}
    Phone: {phone}
    Address: {address}
    """

    sender = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASS")

    msg = MIMEText(message)
    msg['Subject'] = "New Order - Zaika Dhaba"
    msg['From'] = sender
    msg['To'] = sender

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender, password)
    server.sendmail(sender, sender, msg.as_string())
    server.quit()

    return "<h2>Order Placed Successfully!</h2>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
