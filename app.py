from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "service": "Currency Converter API",
        "status": "Online"
    })

@app.route('/convert')
def convert():

    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = request.args.get('amount')

    if not from_currency or not to_currency or not amount:
        return jsonify({
            "error": "Please provide from, to and amount"
        })

    amount = float(amount)

    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    response = requests.get(url)

    data = response.json()

    rate = data['rates'][to_currency]

    converted_amount = amount * rate

    return jsonify({
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "exchange_rate": rate,
        "converted_amount": round(converted_amount, 2)
    })

if __name__ == "__main__":
    app.run()
