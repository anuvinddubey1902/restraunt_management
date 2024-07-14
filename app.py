from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'menu.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM menu")
    menu = cur.fetchall()
    return render_template('index.html', menu=menu)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        food_name = request.form['food_name']
        price = request.form['price']
        in_stock = request.form['in_stock']
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO menu (food_name, price, in_stock) VALUES (?, ?, ?)",
                    (food_name, price, in_stock))
        conn.commit()
        return redirect(url_for('index'))
    return render_template('add_item.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    conn = get_db()
    cur = conn.cursor()
    if request.method == 'POST':
        food_name = request.form['food_name']
        price = request.form['price']
        in_stock = request.form['in_stock']
        cur.execute("UPDATE menu SET food_name = ?, price = ?, in_stock = ? WHERE id = ?",
                    (food_name, price, in_stock, id))
        conn.commit()
        return redirect(url_for('index'))
    cur.execute("SELECT * FROM menu WHERE id = ?", (id,))
    menu = cur.fetchone()
    return render_template('edit_item.html', menu=menu)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_transaction(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM menu WHERE id = ?", (id,))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
