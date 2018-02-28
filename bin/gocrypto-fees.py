# Python 3
# Example coin from binance fees JSON call:
# {'resetAddressStatus': False, 'blockUrl': 'https://chainz.cryptoid.info/pivx/block.dws?', 'commissionRate': 0.0, 'dynamicFeeStatus': False, 'depositTipStatus': False, 'chargeDescCn': None, 'chineseName': 'PIVX', 'seqNum': '105', 'regExTag': '', 'feeRate': None, 'isLegalMoney': False, 'feeReferenceAsset': '', 'depositTipCn': None, 'minProductWithdraw': '0.100000000000000000', 'depositTipEn': None, 'freeAuditWithdrawAmt': 0.0, 'confirmTimes': '6', 'reconciliationAmount': 0.0, 'url': 'https://chainz.cryptoid.info/pivx/tx.dws?', 'withdrawIntegerMultiple': '0E-18', 'supportMarket': None, 'logoUrl': '/file/resources/img/20180123/image_1516677190423.png', 'assetLabel': None, 'sameAddress': False, 'test': 0, 'enableWithdraw': True, 'legalMoney': False, 'freeUserChargeAmount': 10000000.0, 'regEx': '^(D)[0-9A-za-z]{33}$', 'assetName': 'PIVX', 'createTime': None, 'transactionFee': 0.02, 'chargeDescEn': None, 'id': '150', 'feeDigit': None, 'assetLabelEn': None, 'addressUrl': 'https://chainz.cryptoid.info/pivx/address.dws?', 'enableCharge': True, 'parentCode': 'PIVX', 'enLink': '', 'unit': '', 'forceStatus': False, 'assetCode': 'PIVX', 'gas': 1.0, 'cnLink': ''}

import json
import requests


BINANCE_FEES_URL = 'https://www.binance.com/assetWithdraw/getAllAsset.html'
COINMARKETCAP_API_URL = 'https://api.coinmarketcap.com/v1/'
CRYPTOCOMPARE_API_URL = 'https://min-api.cryptocompare.com/'

# Returns an object in JSON format with coin information from binance
def get_binance_fees():
    response = requests.get(BINANCE_FEES_URL)

    if response.status_code == 200:
        coins = json.loads(response.content.decode('utf-8'))
        return coins
    else:
        return None



# Main execution + Use examples
def main():
    binance_fees = get_binance_fees()
    print(binance_fees[0]['assetCode'])
    print(binance_fees[0]['transactionFee'])


if __name__ == "__main__":
	main()