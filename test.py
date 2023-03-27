from web3 import Web3

web3 = Web3.IPCProvider('https://mainnet.infura.io/v3/d56b20c82b3c4b50a963365334ee401c')

web3.is_connected()