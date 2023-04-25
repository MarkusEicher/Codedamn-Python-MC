from web3 import Web3 
from web3.middleware.geth_poa import geth_poa_middleware 

# Connect to the local Ethereum node
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Inject the default Metamask provider
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# # Check if a Metamask wallet is connected
# if web3.isConnected():
#     print('Connected to Metamask wallet:', web3.eth.accounts[0])
# else:
#     print('Metamask wallet not detected')


# Check if a provider is set
if web3.provider:
    print('Metamask wallet detected:', web3.eth.accounts[0])
else:
    print('Metamask wallet not detected')
