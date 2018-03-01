# Python 3
# Example coin from binance fees JSON call:
# {'resetAddressStatus': False, 'blockUrl': 'https://chainz.cryptoid.info/pivx/block.dws?', 'commissionRate': 0.0, 'dynamicFeeStatus': False, 'depositTipStatus': False, 'chargeDescCn': None, 'chineseName': 'PIVX', 'seqNum': '105', 'regExTag': '', 'feeRate': None, 'isLegalMoney': False, 'feeReferenceAsset': '', 'depositTipCn': None, 'minProductWithdraw': '0.100000000000000000', 'depositTipEn': None, 'freeAuditWithdrawAmt': 0.0, 'confirmTimes': '6', 'reconciliationAmount': 0.0, 'url': 'https://chainz.cryptoid.info/pivx/tx.dws?', 'withdrawIntegerMultiple': '0E-18', 'supportMarket': None, 'logoUrl': '/file/resources/img/20180123/image_1516677190423.png', 'assetLabel': None, 'sameAddress': False, 'test': 0, 'enableWithdraw': True, 'legalMoney': False, 'freeUserChargeAmount': 10000000.0, 'regEx': '^(D)[0-9A-za-z]{33}$', 'assetName': 'PIVX', 'createTime': None, 'transactionFee': 0.02, 'chargeDescEn': None, 'id': '150', 'feeDigit': None, 'assetLabelEn': None, 'addressUrl': 'https://chainz.cryptoid.info/pivx/address.dws?', 'enableCharge': True, 'parentCode': 'PIVX', 'enLink': '', 'unit': '', 'forceStatus': False, 'assetCode': 'PIVX', 'gas': 1.0, 'cnLink': ''}

import json
import requests


BINANCE_FEES_URL = 'https://www.binance.com/assetWithdraw/getAllAsset.html'
BITTREX_FEES_API_URL = 'https://bittrex.com/api/v1.1/public/getcurrencies'
COINMARKETCAP_API_URL = 'https://api.coinmarketcap.com/v1/ticker'
CRYPTOCOMPARE_API_URL = 'https://min-api.cryptocompare.com/'


# Returns a dictionary from a JSON API call
def get_json_dict(json_url) -> dict:
    
    # HTTP Request
    try:
        response = requests.get(json_url)
    except requests.exceptions.RequestException() as err:
        print("Other Error:", err)
        return None
    
    # JSON decode
    try:
        dictionary = json.loads(response.content.decode('utf-8'))
    except ValueError as err:
        print("Value Error: ", err)
        return None
    
    print("Request + JSON decode succeded")
    return(dictionary)





# Main execution + Use examples
def main():
    
    # Binance-fees non-official JSON API
    binance_fees = get_json_dict(BINANCE_FEES_URL)
    print(binance_fees[0]['assetCode'])
    print(binance_fees[0]['transactionFee'])
    
    # Coinmarketcap API
    coinmarketcap_api = get_json_dict(COINMARKETCAP_API_URL)
    print(coinmarketcap_api[0]['symbol'])
    print(coinmarketcap_api[0]['price_usd'])    

    # Bittrex currencies API
    bittrex_currencies = get_json_dict(BITTREX_FEES_API_URL)
    print(bittrex_currencies['result'][0]['Currency'])
    print(bittrex_currencies['result'][0]['TxFee'])   

if __name__ == "__main__":
	main()