import json
import requests
convert = requests.get("http://www.floatrates.com/daily/usd.json")
usd_dict = json.loads(convert.text)
convert = requests.get("http://www.floatrates.com/daily/eur.json")
eur_dict = json.loads(convert.text)
cache = {"cache": 0} # to have a non-empty dictionary for first cache check

currency_code = input().lower()
while True:
    convert_to = input().lower()
    if not convert_to:
        exit()
    amount = float(input())
    if convert_to is None:
        exit()
    print("Checking the cache...")
    if list(usd_dict)[0] != convert_to and list(eur_dict)[0] != convert_to and convert_to not in cache:
        print("Sorry, but it is not in the cache!")
        convert = requests.get(f"http://www.floatrates.com/daily/{convert_to}.json")
        convert_to_dict = json.loads(convert.text)
        conversion = round(amount / float(convert_to_dict[currency_code]["rate"]), 2)
        cache[convert_to] = convert_to_dict[currency_code]["rate"]
        print(f"You received {conversion} {convert_to.upper()}.")
        continue

    else:
        print("Oh! It is in the cache!")
        if convert_to.upper() == "USD":
            conversion = round(amount / float(usd_dict[currency_code]["rate"]), 2)
            print(f"You received {conversion} {convert_to.upper()}.")
            continue
        elif convert_to.upper() == "EUR":
            conversion = round(amount / float(eur_dict[currency_code]["rate"]), 2)
            print(f"You received {conversion} {convert_to.upper()}.")
            continue
        elif convert_to in cache:
            conversion = round(amount / cache[convert_to], 2)
            print(f"You received {conversion} {convert_to.upper()}.")
            continue
