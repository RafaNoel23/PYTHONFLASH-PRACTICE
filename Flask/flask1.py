from flask import Flask
from flask import *
import sqlite3


app = Flask(__name__)

conn = sqlite3.connect('flask.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS personal_info (name, age, course)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS foods (name, image)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS animals (name, image)''')

personal_info = ('Rafael Noel', '23', 'BSIT')
cursor.execute('INSERT INTO personal_info VALUES (?,?,?)', personal_info)
conn.commit()

foods = [('Buttered Shrimp', 'buttshrimp.jpg'),('Buttered Crab', 'buttcrab.jpg'),('Fish Fillet', 'fishfillet.jpg')]
cursor.executemany('INSERT INTO foods (name, image) VALUES (?, ?)', foods)
conn.commit()

animals = [('Owl','owl.jpg'),('Turtle', 'turtle.jpg'),('Panda','panda.jpg')]
cursor.executemany('INSERT INTO animals (name, image) VALUES (?, ?)', animals)
conn.commit()

@app.route('/')
def index():
    return render_template('personal_info.html', username='Rafa',info=personal_info)

@app.route('/foods')
def hello_world():
    food_image_urls = [url_for('static', filename='image/' + food[1]) for food in foods]
    print(food_image_urls)  # Print generated URLs to the console
    return render_template('foods.html', username='Rafa', food=foods)


@app.route('/animals')
def jinja():
    animal_image_urls = [url_for('static', filename='image/' + animal[1]) for animal in animals]
    print(animal_image_urls)
    return render_template('animals.html', username='Rafa', animal=animals)


# Always keep this line at the end
if __name__ == '__main__':
    app.run(debug=True, port=5000)

conn.close()
