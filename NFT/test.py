from web3 import Web3

web3 = Web3(
    Web3.HTTPProvider('https://sepolia.infura.io/v3/d56b20c82b3c4b50a963365334ee401c')
)


def get_value(account):
    address = web3.to_checksum_address(account)
    w_balance = web3.eth.get_balance(address)
    return(web3.from_wei(w_balance, 'ether'))
