from locale import currency
import requests
import json

url = "https://currencyconverter.p.rapidapi.com/"

currency_1 = "INR"
currency_2 = "USD"
amount = "1000"

querystring = {"amount":amount,"from":currency_1,"to":currency_2}

headers = {
	"X-RapidAPI-Key": "7c7c74b4damshc04a2629cca9616p1c4341jsnc4d3e10fe551",
	"X-RapidAPI-Host": "currencyconverter.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
converted_amount = data["result"]["convertedAmount"]
formatted = "{:,.2f}".format(converted_amount)

print(converted_amount, formatted)