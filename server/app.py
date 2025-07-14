from flask import Flask, request, jsonify
from flask_cors import CORS
from scrape import get_tickpix_price_from_url

#app config
app = Flask(__name__)
CORS(app)

@app.route('/scrape', methods=['POST'])
def scrape():
    args = request.json
    print(args)

