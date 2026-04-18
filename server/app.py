from flask import Flask

app = Flask(__name__)

# Data arrays
contracts = [{"id": 1, "info": "Service agreement"}, {"id": 2, "info": "NDA"}]
customers = ["Alice", "Bob"]

@app.route('/contract/<int:id>')
def get_contract(id):
    contract = next((c for c in contracts if c["id"] == id), None)
    if contract:
        return {"contract": contract}, 200
    return {"error": "Not found"}, 404

@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    if customer_name in customers:
        # 204: Success, no content
        return "", 204
    return {"error": "Not found"}, 404

if __name__ == '__main__':
    app.run(port=5555)