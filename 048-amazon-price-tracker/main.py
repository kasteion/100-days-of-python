import requests
from bs4 import BeautifulSoup
import smtplib
import os

PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
TARGET_PRICE = 200

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.8"
}


response = requests.get(PRODUCT_URL, headers=headers)
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")
product_title = soup.find(name="span", id="productTitle")
price_symbol = soup.find(name="span", class_="a-price-symbol")
price_whole = soup.find(name="span", class_="a-price-whole")
price_fraction = soup.find(name="span", class_="a-price-fraction")

price = float(f"{price_whole.text}{price_fraction.text}")

if price < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
        conn.starttls()
        conn.login(user=EMAIL, password=PASSWORD)
        conn.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{product_title.text.encode('utf-8').strip()} is now ${price} {response.url}"
        )
