from flask import Flask, Response
import requests
import json
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
#@app.route("/")
#def hello_world():
#    return "<p>Hello, World!</p>"

@app.route("/get-price/<ticker>")

def get_price(ticker):
    
    url = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/DIS?modules=price%2CsummaryDetail%2CpageViews%2CfinancialsTemplate"
    headers={'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url,headers=headers)
    print(r.status_code)
    result = r.json()

    #print(result)

    if r.status_code > 400:
        app.logger.info(f"Problema de Yahoo con ticker: {ticker}.")
        app.logger.info(f"Codigo Status Yahoo: {r.status_code}.")
        return Response({}, status=404, mimetype='application/json')
        
    app.logger.info(result)

    try:
        price = result['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
        company_name = result['quoteSummary']['result'][0]['price']['longName']
        exchange = result['quoteSummary']['result'][0]['price']['exchangeName']
        currency = result['quoteSummary']['result'][0]['price']['currency']

        result = {
            "price": price,
            "name": company_name,
            "exchange": exchange,
            "currency": currency
        }
        app.logger.info(result)
        #print(result)
        
        return Response(json.dumps(result), status=200, mimetype='application/json')
    except (KeyError, TypeError):
        return Response({}, status=404, mimetype='application/json')
    except Exception as e:
        app.logger.error("Excepcion ocurrida", exc_info=True)


if __name__ == '_main_':
    app.run()
