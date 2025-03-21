import requests

# Step 1: Get base currency
base_currency = input().strip().lower()

# Step 2: Fetch rates from floatrates
url = f"http://www.floatrates.com/daily/{base_currency}.json"
response = requests.get(url)
rates = response.json()

# Step 3: Initialize cache with USD and EUR
cache = {}
for code in ['usd', 'eur']:
    if code in rates:
        cache[code] = rates[code]['rate']

# Step 4: Interactive input loop
while True:
    target_currency = input().strip().lower()
    if not target_currency:
        break

    amount_str = input().strip()
    if not amount_str:
        break
    amount = float(amount_str)

    print("Checking the cache...")

    if target_currency in cache:
        print("Oh! It is in the cache!")
        rate = cache[target_currency]
    else:
        print("Sorry, but it is not in the cache!")
        rate = rates[target_currency]['rate']
        cache[target_currency] = rate

    received = amount * rate
    print(f"You received {round(received, 2)} {target_currency.upper()}.")