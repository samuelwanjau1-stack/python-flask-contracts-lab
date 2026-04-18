from flask import Flask

app = Flask(__name__)

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},
             {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
             {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob", "bill", "john", "sarah"]

# 1. '/contract/<id>' route
@app.route('/contract/<int:id>')
def get_contract(id):
    contract = next((c for c in contracts if c["id"] == id), None)
    if contract:
        # 200 response: Contract found
        return contract, 200
    # 404 response: Contract not found
    return {"error": "Not found"}, 404

# 2. '/customer/<customer_name>' route
@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    # Check if customer exists
    if customer_name in customers:
        # 204 response: Customer found, no information
        return "", 204
    # 404 response: Customer not found
    return {"error": "Not found"}, 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)