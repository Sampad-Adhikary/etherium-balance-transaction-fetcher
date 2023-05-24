from web3 import Web3
from web3.utils.address import to_checksum_address
import requests

web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/81fdcda012c44f43bbbdcca542ba6959'))

def get_balance(ethereum_address):
    checksum_address = web3.to_checksum_address(ethereum_address)

    balance_wei = web3.eth.get_balance(checksum_address)
    balance_eth = web3.from_wei(balance_wei, 'ether')

    return balance_eth

def convert_eth_to_inr(eth_amount):
    endpoint = f'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=inr'

    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            conversion_rate = response.json().get('ethereum', {}).get('inr')
            if conversion_rate:
                inr_amount = eth_amount * conversion_rate
                return inr_amount, conversion_rate
            else:
                print("Conversion rate not found in the response")
        else:
            print(f"Error: {response.status_code} - {response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")

    return None, None


def get_balance_inr(ethereum_address):
    checksum_address = web3.to_checksum_address(ethereum_address)

    balance_wei = web3.eth.get_balance(checksum_address)
    balance_eth = web3.from_wei(balance_wei, 'ether')

    balance_inr, conversion_rate = convert_eth_to_inr(balance_eth)

    return balance_inr, conversion_rate


def get_recent_transactions(ethereum_address):
    api_key = 'H5HAWKR5VJXXSX53B721NEUDZT8DUAAJ41'

    endpoint = f'https://api.etherscan.io/api?module=account&action=txlist&address={ethereum_address}&sort=desc&apikey={api_key}'

    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            transactions = response.json()['result'][:5]

            extracted_transactions = []
            for transaction in transactions:
                extracted_transaction = {
                    'blockNumber': transaction['blockNumber'],
                    'hash': transaction['hash'],
                    'transactionIndex': transaction['transactionIndex'],
                    'from': transaction['from'],
                    'to': transaction['to'],
                    'value': transaction['value'],
                }
                extracted_transactions.append(extracted_transaction)

            return extracted_transactions
        else:
            print(f"Error: {response.status_code} - {response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")

    return []