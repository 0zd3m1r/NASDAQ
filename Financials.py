import json
import time
import random
import requests
from requests import Request, Session

markets = 'Markets'
url = "https://api.nasdaq.com/api/company/"
path = "Financials"
open(path, 'w').close()

headers = {
    'authority': 'api.nasdaq.com',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'origin': 'https://www.nasdaq.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.nasdaq.com/',
    'accept-language': 'en-US,en;q=0.9',
}
session = Session()
session.headers.update(headers)

with open(markets) as fp:
    writefile = open(path, "a")
    lines = fp.read().splitlines()
    rangeindex = int(len(lines)/1)+1
    count = 0
    for line in range(1, rangeindex):
        time.sleep(random.uniform(1,2))
        symbol = lines[count]
        print(symbol)
        response = session.get(url+symbol+"/financials")
        response_json = response.json()
        try:
###incomeStatementTable
                rowsincome = response_json["data"]["incomeStatementTable"]["rows"]
                lengthrowsincome  = len(rowsincome)
                for i in range(0, lengthrowsincome -1):
                        riv1 = rowsincome[i]["value1"]
                        riv2 = rowsincome[i]["value2"]
                        riv3 = rowsincome[i]["value3"]
                        riv4 = rowsincome[i]["value4"]
                        riv5 = rowsincome[i]["value5"]
                        ri = symbol + ":Income Statement:" + riv1 + ":" + riv2 + ":" + riv3 + ":" + riv4 + ":" + riv5
                        writefile.write(ri+"\n")
###balanceSheetTable
                rowsbalance = response_json["data"]["balanceSheetTable"]["rows"]
                lengthrowsbalance = len(rowsbalance)
                for i in range(0, lengthrowsbalance-1):
                        rbv1 = rowsbalance[i]["value1"]
                        rbv2 = rowsbalance[i]["value2"]
                        rbv3 = rowsbalance[i]["value3"]
                        rbv4 = rowsbalance[i]["value4"]
                        rbv5 = rowsbalance[i]["value5"]
                        rb = symbol + ":Balance Sheet:" + rbv1 + ":" + rbv2 + ":" + rbv3 + ":" + rbv4 + ":" + rbv5
                        writefile.write(rb+"\n")
###cashFlowTable
                rowscash = response_json["data"]["cashFlowTable"]["rows"]
                lengthrowscash = len(rowscash)
                for i in range(0, lengthrowscash-1):
                        rcv1 = rowscash[i]["value1"]
                        rcv2 = rowscash[i]["value2"]
                        rcv3 = rowscash[i]["value3"]
                        rcv4 = rowscash[i]["value4"]
                        rcv5 = rowscash[i]["value5"]
                        rc = symbol + ":Cash Flow:" + rcv1 + ":" + rcv2 + ":" + rcv3 + ":" + rcv4 + ":" + rcv5
                        writefile.write(rc+"\n")
###financialRatiosTable
                rowsfinancial = response_json["data"]["financialRatiosTable"]["rows"]
                lengthrowsfinancial = len(rowsfinancial)
                for i in range(0, lengthrowsfinancial-1):
                        rfv1 = rowsfinancial[i]["value1"]
                        rfv2 = rowsfinancial[i]["value2"]
                        rfv3 = rowsfinancial[i]["value3"]
                        rfv4 = rowsfinancial[i]["value4"]
                        rfv5 = rowsfinancial[i]["value5"]
                        rf = symbol + ":Financial Ratios:" + rfv1 + ":" + rfv2 + ":" + rfv3 + ":" + rfv4 + ":" + rfv5
                        writefile.write(rf+"\n")
                count += 1
                time.sleep(random.uniform(1,3))
        except Exception as exp:
            count +=1
            print(exp.status_code, flush=True)
            print(exp.message, flush=True)
