from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    name = request.form['name']
    phone = request.form['phone']
    item = request.form['item']
    quantity = request.form['quantity']
    address = request.form['address']

    message = f"""
    New Order from Zaika Dhaba Website

    Name: {name}
    Phone: {phone}
    Item: {item}
    Quantity: {quantity}
    Address: {address}
    """

    sender = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASS")
    receiver = "restaurantowner@gmail.com"

    msg = MIMEText(message)
    msg['Subject'] = "New Order - Zaika Dhaba"
    msg['From'] = sender
    msg['To'] = receiver

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()

    return "Order Sent Successfully!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
