import requests
import sys
import json

def main():
  if len(sys.argv) == 2:
    try:
      n = float(sys.argv[1])
    except ValueError:
      print("Command-line argument is not a number")
      sys.exit(1)
  else:
    print("Missing command-line argument")
    sys.exit(1)

  try:
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
  except requests.RequestException:
    print("API request fail")
    sys.exit()


  # print(json.dumps(response.json(), indent=2))
  o = response.json()
  current_price = o["data"]["priceUsd"]
  amount = float(current_price) * n
  print(f"${amount:,.4f}")
  # print(response)



main()
