import json
from flask import Flask, request
from wallet_balance_service.wallet_balance.wallet_balance import get_token_balance

app = Flask(__name__)


@app.route('/')
def home_page():
    return "Why hello there"


@app.route('/get_token_balance', methods=['GET'])
def get_token_balance_endpoint():
    public_key = request.args.get('public_key')
    token_symbol = request.args.get('token_symbol')
    if isinstance(public_key, str):
        return json.dumps(get_token_balance(public_key, token_symbol))


if __name__ == "__main__":
    app.run()
