from flask import Flask, render_template, redirect, url_for
import sqlite3
import requests
from jinja2 import Template
import json

# create application object
app = Flask(__name__)

# route for kanye quote page

@app.route('/kanye')
def kanyeroute():
    quote = requests.get('https://api.kanye.rest').json()
    json_quote = quote
    kanye_quote = quote['quote']
    author = '- Kanye West'
    return render_template('kanye.html', final_quote = kanye_quote, who = author)

# dont forget to run the app
if __name__ == '__main__':
    app.run(debug=True)
