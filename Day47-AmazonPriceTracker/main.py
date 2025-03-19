from bs4 import BeautifulSoup
import requests
import pprint as pp
from dotenv import load_dotenv
import os
import smtplib


load_dotenv() # Load testing env variables from .env file - referenced by os
URL = "https://appbrewery.github.io/instant_pot/"
HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Accept-Language":"en-US"
}


response = requests.get(url=URL, headers=HEADERS)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

text_price = soup.find("span", class_="a-offscreen").text
price_symbol = soup.find("span", class_="a-price-symbol").text
num_price = float(text_price.strip(price_symbol).replace(",",""))

# pp.pprint(num_price)
# pp.pprint(frac_price)



# Email alert when price is below a target
def send_quote(message, target_email, source_email, source_psw):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=source_email, password=source_psw)
        connection.sendmail(
            from_addr=source_email,
            to_addrs=target_email,
            msg=f'Subject:Price Drop!\n\n{message}'
        )

target = 100.00

alert = False
if num_price < target:
    alert = True


if alert:
    print('sending email...')
    source_email = os.getenv('EMAIL_ADDRESS')
    source_psw = os.getenv('EMAIL_PASSWORD')
    target_email = os.getenv('SMTP_ADDRESS')
    msg = f"Item price dropped to {num_price}!"
    send_quote(message=msg, target_email=target_email,source_email=source_email,source_psw=source_psw)

