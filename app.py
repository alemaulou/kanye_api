from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Retrieve a quote from the Kanye West API
    response = requests.get('https://api.kanye.rest')
    quote = response.json()['quote']

    # Render the template with the quote and Kanye's picture
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run()