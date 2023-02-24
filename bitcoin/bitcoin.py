import sys
import requests

if len(sys.argv)==2:
    try:
        meghdar=float(sys.argv[1])
    except:
        print('Command-line argument is not a number')
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    dastrasi = r.json()
    dastrasibebcusd = dastrasi['bpi']['USD']['rate_float']
    gheymat= dastrasibebcusd*meghdar
    print(f"${gheymat:,.4f}")
except requests.RequestException:
    print('Request Exception')
    sys.exit(1)

