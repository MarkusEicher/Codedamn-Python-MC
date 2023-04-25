from flask import Flask, render_template, request
from web3 import Web3
from web3.middleware.geth_poa import geth_poa_middleware

app = Flask(__name__)

# # Connect to the local Ethereum node
# web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Connect to a Goerli node
web3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/your-project-id'))

# Check if the connection was successful
if web3.isConnected():
    print("Connected to Goerli!")
else:
    print("Failed to connect to Goerli")


# Inject the default Metamask provider
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

@app.route('/')
def index():
    if 'HTTP_X_ETHEREUM_ADDRESS' in request.headers:
        # User has a wallet connected
        address = request.headers['HTTP_X_ETHEREUM_ADDRESS']
        return render_template('index.html', address=address)
    else:
        # User does not have a wallet connected
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
