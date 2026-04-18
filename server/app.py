from flask import Flask

app = Flask(__name__)

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},
             {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
             {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob", "bill", "john", "sarah"]

@app.route('/contract/<int:id>')
def get_contract(id):
    contract = next((c for c in contracts if c["id"] == id), None)
    if contract:
        # RETURN ONLY THE STRING VALUE
        return contract["contract_information"], 200
    return {"error": "Not found"}, 404

@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    if customer_name in customers:
        return "", 204
    return {"error": "Not found"}, 404

if __name__ == '__main__':
    app.run(port=5555)