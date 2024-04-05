from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency, amount):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={amount}"
    content = requests.get(url).text
    soup = BeautifulSoup(content,  "html.parser")
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])
    rate = round(rate,2)

    return rate

in_currency = input("From which currency?: ")
out_currency = input("To which currency?: ")
amount = input("How much? ")

current_rate = get_currency(in_currency, out_currency, amount)
print(current_rate)
