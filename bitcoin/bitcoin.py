import requests
import json
import sys


try:
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
        except (ValueError,TypeError):
            sys.exit("Command-line argument is not a number")
    else:
     sys.exit("Missing command-line argument")


    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    dat=o['bpi']['USD']['rate_float']
    val=n * dat
    print(f"${val:,.4f}")


except requests.RequestException:
    sys.exit()