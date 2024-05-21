from flask import Flask
from flask import *
import hashlib
import sqlite3


app = Flask(__name__)

conn = sqlite3.connect('pos.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (name, password, role)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS products (name, price, stock)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (transaction_id)''')

passwordadmin = 'admin123'
passwordseller = 'seller123'
passwordcustomer = 'customer123'

hashed_password_admin = hashlib.scrypt(passwordadmin.encode('utf-8'), salt=b'secret_spice', n=2**14, r=8, p=1)
hashed_password_seller = hashlib.scrypt(passwordseller.encode('utf-8'), salt=b'secret_spice', n=2**14, r=8, p=1)
hashed_password_customer = hashlib.scrypt(passwordcustomer.encode('utf-8'), salt=b'secret_spice', n=2**14, r=8, p=1)

users = [('rafa-admin', hashed_password_admin, 'Admin'),('rafa-seller', hashed_password_seller, 'Seller'),('rafa-customer', hashed_password_customer, 'Customer')]
cursor.executemany('INSERT INTO users (name, password, role) VALUES (?, ?, ?)', users)
conn.commit()

products = [('Shampoo', 100.00, 20), ('Ice', 5.00, 40), ('Soda', 20.00, 50)]
cursor.executemany('INSERT INTO products (name, price, stock) VALUES (?, ?, ?)', products)
conn.commit()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/admin')
def admin_control():
    return render_template('admin.html', username='rafa-admin', users= users)

@app.route('/seller')
def seller_control():
    return render_template('seller.html', username='rafa-seller', users = users)

@app.route('/customer')
def customer_control():
    return render_template('customer.html', username='rafa-customer', users = users)


if __name__ == '__main__':
    app.run(debug=True, port=3000)

conn.close()
