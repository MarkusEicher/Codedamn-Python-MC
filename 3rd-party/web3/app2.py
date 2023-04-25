from flask import Flask, render_template
from web3 import Web3
from web3.middleware.geth_poa import geth_poa_middleware

app = Flask(__name__)

# Connect to the local Ethereum node
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Inject the default Metamask provider
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

@app.route('/')
def index():
    if web3.eth.account in web3.eth.accounts:
        address = web3.eth.accounts[0]
        return render_template('index.html', address=address)
    else:
        return render_template('index.html', address='')

if __name__ == '__main__':
    app.run(debug=True)
