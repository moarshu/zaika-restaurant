from flask import Flask, render_template, request, redirect, url_for
import os
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)


# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template('index.html')


# ---------------- VEG PAGE ----------------
@app.route('/veg')
def veg():
    return render_template('veg.html')


# ---------------- NON-VEG PAGE ----------------
@app.route('/nonveg')
def nonveg():
    return render_template('nonveg.html')


# ---------------- CHECKOUT ----------------
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        item = request.form.get('item')
        price = request.form.get('price')
        quantity = request.form.get('quantity')

        if not item or not price or not quantity:
            return redirect(url_for('home'))

        try:
            price = int(price)
            quantity = int(quantity)
        except:
            return redirect(url_for('home'))

        total = price * quantity

        return render_template(
            'checkout.html',
            item=item,
            price=price,
            quantity=quantity,
            total=total
        )

    return redirect(url_for('home'))


# ---------------- ORDER + EMAIL ----------------
@app.route('/order', methods=['POST'])
def order():
    try:
        name = request.form.get('name')
        phone = request.form.get('phone')
        address = request.form.get('address')
        item = request.form.get('item')
        quantity = request.form.get('quantity')
        total = request.form.get('total')

        if not name or not phone or not address:
            return "<h3>Customer details missing</h3>"

        sender = os.environ.get("EMAIL_USER")
        password = os.environ.get("EMAIL_PASS")

        if not sender or not password:
            return "<h3>Email credentials not configured in Render</h3>"

        message = f"""
New Order Received

Item: {item}
Quantity: {quantity}
Total: ₹{total}

Customer Name: {name}
Phone: {phone}
Address: {address}
"""

        msg = MIMEText(message)
        msg['Subject'] = "New Order - Zaika Dhaba"
        msg['From'] = sender
        msg['To'] = sender

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender, password)
        server.sendmail(sender, sender, msg.as_string())
        server.quit()

        return "<h2>Order Placed Successfully! Email Sent ✅</h2>"

    except Exception as e:
        return f"<h3>Server Error: {str(e)}</h3>"


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
