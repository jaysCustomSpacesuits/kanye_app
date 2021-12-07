from flask import Flask, render_template
import requests
from jinja2 import Template
import json

# create application object
app = Flask(__name__)

# route for kanye quote page
@app.route('/kanye')
def kanyeroute():
    quote = requests.get('https://api.kanye.rest').json()
    kanye_quote = quote['quote']
    author = '- Kanye West'
    return render_template('kanye.html', final_quote = kanye_quote, who = author)

# dont forget to run the app
if __name__ == '__main__':
    app.run(debug=True)